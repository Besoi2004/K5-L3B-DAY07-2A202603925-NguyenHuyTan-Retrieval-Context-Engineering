"""Score agent runs against gold AFTER they finish (gold is used here only, never by the agent).

    .venv/Scripts/python src/score_agent.py --split dev

For every results/agent-<split>-*/traces.json prints and saves results/agent-<split>-comparison.json:
- context_evidence: answerable questions whose final context holds a chunk containing gold evidence
- correct_behaviour: answerable answered + unanswerable abstained (automatic, by status)
- cited_gold: answered questions where >=1 cited chunk contains gold evidence (proxy only; the real
  citation_support label comes from the manual review)
- searches, tokens, median time, errors
"""
import argparse
import json
import statistics
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter"))
from baseline import hit  # noqa: E402


def score(traces: list[dict], cases: dict, gold: dict, chunks: dict) -> dict:
    s = {"n": len(traces), "errors": 0, "context_evidence": 0, "answerable": 0, "answered_answerable": 0,
         "abstained_unanswerable": 0, "unanswerable": 0, "cited_gold": 0, "answered": 0}
    misses = {"context": [], "false_abstain": [], "not_abstained": [], "cited_not_gold": []}
    for t in traces:
        qid, st = t["query_id"], t["status"]
        if st == "error":
            s["errors"] += 1
            continue
        if cases[qid]["answerable"]:
            s["answerable"] += 1
            last = [e for e in t["events"] if e["event"] == "search"]
            ctx_ids = set(last[-1]["context_ids"]) if last else set()
            if any(hit(chunks[i], gold[qid]) for i in ctx_ids):
                s["context_evidence"] += 1
            else:
                misses["context"].append(qid)
            if st == "answered":
                s["answered_answerable"] += 1
            else:
                misses["false_abstain"].append(qid)
        else:
            s["unanswerable"] += 1
            if st == "abstain":
                s["abstained_unanswerable"] += 1
            else:
                misses["not_abstained"].append(qid)
        if st == "answered" and qid in gold:
            s["answered"] += 1
            if any(hit(chunks[c], gold[qid]) for c in t["citations"] if c in chunks):
                s["cited_gold"] += 1
            else:
                misses["cited_not_gold"].append(qid)
    ok = [t for t in traces if t["status"] != "error"]
    s["correct_behaviour"] = s["answered_answerable"] + s["abstained_unanswerable"]
    s["avg_searches"] = round(statistics.mean(t["n_searches"] for t in ok), 2) if ok else None
    s["llm_calls"] = sum(sum(1 for m in t["model_calls"] if m.get("source") != "original_question") for t in traces)
    s["tokens_in"] = sum(t["tokens_in"] for t in traces)
    s["tokens_out"] = sum(t["tokens_out"] for t in traces)
    s["median_elapsed_s"] = round(statistics.median(t["elapsed_s"] for t in traces), 2)
    s["misses"] = misses
    return s


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    args = ap.parse_args()
    cases = {c["id"]: c for c in json.loads((ROOT / "data/cases.json").read_text(encoding="utf-8"))}
    gold = {q["id"]: q["gold"] for q in json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))}
    chunks = {c["id"]: c for c in json.loads((ROOT / "data/chunks.json").read_text(encoding="utf-8"))}
    out = {}
    for d in sorted((ROOT / "results").glob(f"agent-{args.split}-*/traces.json"), key=lambda p: p.stat().st_mtime):
        name = d.parent.name.removeprefix(f"agent-{args.split}-")
        out[name] = s = score(json.loads(d.read_text(encoding="utf-8")), cases, gold, chunks)
        print(f"{name:26s} ctx {s['context_evidence']}/{s['answerable']}  behaviour {s['correct_behaviour']}/{s['n'] - s['errors']}"
              f"  abstain {s['abstained_unanswerable']}/{s['unanswerable']}  false-abst {len(s['misses']['false_abstain'])}"
              f"  cited_gold {s['cited_gold']}/{s['answered']}  searches {s['avg_searches']}  LLM calls {s['llm_calls']}"
              f"  tok {s['tokens_in']}+{s['tokens_out']}  {s['median_elapsed_s']}s  err {s['errors']}")
        print(f"{'':26s} misses {s['misses']}")
    (ROOT / "results" / f"agent-{args.split}-comparison.json").write_text(
        json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
