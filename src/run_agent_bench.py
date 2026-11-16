"""Run the real agent (Gemini + retriever) over one split and save traces.

    .venv/Scripts/python src/run_agent_bench.py --split dev --retriever dense --name dense-k3-b2400

Reads data/cases.json (no gold). Each question's errors are caught and saved as status "error"
(never replaced by fake output). Output: results/agent-<split>-<name>/traces.json, summary.json,
review.md (answers next to the cited chunk text, for manual citation/answer grading).
"""
import argparse
import json
import statistics
import time
import traceback
from collections import Counter
from pathlib import Path

from agent import GeminiController, run_agent

ROOT = Path(__file__).resolve().parents[1]


def make_retriever(name: str):
    from retrievers import BM25Retriever, DenseRetriever, HybridRetriever
    chunks = json.loads((ROOT / "data/chunks.json").read_text(encoding="utf-8"))
    if name == "bm25":
        return BM25Retriever(chunks)
    dense = DenseRetriever()
    return dense if name == "dense" else HybridRetriever(dense, BM25Retriever(chunks))


def write_review(path: Path, traces: list[dict], cases: dict, questions: dict) -> None:
    """Grader sheet only: expected answers are shown here, never to the agent."""
    lines = ["# Review agent — chấm tay", "",
             "Với mỗi câu: answer_grade 0/1/2 (câu có đáp án), citation_support đúng/sai cho từng citation, "
             "abstention_correct (câu thiếu evidence). Đọc nguyên văn chunk, không chỉ nhìn ID.", ""]
    for t in traces:
        c = cases[t["query_id"]]
        lines += [f"## {t['query_id']} · {'có đáp án' if c['answerable'] else 'THIẾU EVIDENCE'} · status `{t['status']}`",
                  f"**Hỏi:** {c['question']}", ""]
        q = questions.get(t["query_id"])
        lines.append(f"**Đáp án chuẩn (chỉ để chấm):** {q['expected_answer']}" if q else f"**Lý do thiếu:** {c['absence_reason']}")
        lines += ["", f"**Query đã tìm:** {[e['query'] for e in t['events'] if e['event'] == 'search']}",
                  f"**Agent trả lời:** {t.get('answer') or t.get('error')}", ""]
        chunks = {r["id"]: r for e in t["events"] if e["event"] == "search" for r in e["results"]}
        for cid in t.get("citations", []):
            ch = chunks.get(cid, {})
            lines += [f"- `[{cid}]` tr. {ch.get('page')}:", "", "  > " + ch.get("text", "").replace("\n", "\n  > "), ""]
        lines += ["Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: ", "", "---", ""]
    path.write_text("\n".join(lines), encoding="utf-8")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("--retriever", default="dense", choices=("dense", "bm25", "hybrid_rrf"))
    ap.add_argument("--name", required=True, help="config name, used for the output folder")
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--budget", type=int, default=2400)
    ap.add_argument("--max-searches", type=int, default=3)
    ap.add_argument("--only", help="comma-separated question ids (debug)")
    args = ap.parse_args()

    all_cases = json.loads((ROOT / "data/cases.json").read_text(encoding="utf-8"))
    cases = [c for c in all_cases if c["split"] == args.split and (not args.only or c["id"] in args.only.split(","))]
    retriever = make_retriever(args.retriever)
    controller = GeminiController(max_searches=args.max_searches)
    config = {"split": args.split, "retriever": args.retriever, "model": controller.model, "top_k": args.top_k,
              "budget_chars": args.budget, "max_searches": args.max_searches, "temperature": 0}
    out = ROOT / "results" / f"agent-{args.split}-{args.name}"
    out.mkdir(parents=True, exist_ok=True)

    traces = []
    for i, c in enumerate(cases, 1):
        controller.log = []
        t0 = time.perf_counter()
        try:
            r = run_agent(c["question"], controller, retriever, filters=c.get("filter"),
                          max_searches=args.max_searches, top_k=args.top_k, budget=args.budget)
        except Exception as e:  # recorded, not hidden and not replaced by a fake answer
            r = {"status": "error", "answer": None, "citations": [], "events": [],
                 "error": f"{type(e).__name__}: {e}", "traceback": traceback.format_exc(limit=3)}
        r.update(query_id=c["id"], question=c["question"], filter=c.get("filter"), model_calls=controller.log,
                 elapsed_s=round(time.perf_counter() - t0, 2),
                 n_searches=sum(e["event"] == "search" for e in r["events"]),
                 tokens_in=sum(m["tokens_in"] for m in controller.log),
                 tokens_out=sum(m["tokens_out"] + m["tokens_thought"] for m in controller.log))
        traces.append(r)
        print(f"[{i}/{len(cases)}] {c['id']} {r['status']:8s} searches={r['n_searches']} {r['elapsed_s']}s "
              f"{(r.get('answer') or r.get('error') or '')[:90]!r}", flush=True)
        (out / "traces.json").write_text(json.dumps(traces, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")

    ok = [t for t in traces if t["status"] != "error"]
    answerable = {c["id"]: c["answerable"] for c in cases}
    summary = {**config, "n": len(traces), "status": dict(Counter(t["status"] for t in traces)),
               "tool_use": {"n": sum(t["n_searches"] > 0 for t in ok), "N": len(ok)},
               "searches_distribution": dict(sorted(Counter(t["n_searches"] for t in ok).items())),
               "answered_answerable": sum(t["status"] == "answered" and answerable[t["query_id"]] for t in ok),
               "abstained_unanswerable": sum(t["status"] == "abstain" and not answerable[t["query_id"]] for t in ok),
               "false_abstention": sum(t["status"] == "abstain" and answerable[t["query_id"]] for t in ok),
               "tokens_in": sum(t["tokens_in"] for t in traces), "tokens_out": sum(t["tokens_out"] for t in traces),
               "median_elapsed_s": statistics.median(t["elapsed_s"] for t in traces),
               "cost_usd": 0, "cost_note": "Gemini API free tier; token counts reported for paid-tier estimates",
               "note": "answered/abstain are automatic; answer and citation quality need the manual review in review.md"}
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    questions = {q["id"]: q for q in json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))}
    write_review(out / "review.md", traces, {c["id"]: c for c in all_cases}, questions)
    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
