"""Print one agent trace step by step: searches -> results -> final context -> model decisions -> answer.

    .venv/Scripts/python src/show_trace.py agent-test-hybrid-orig-early-strict t03
    .venv/Scripts/python src/show_trace.py results/agent-dev-error-demo-bad-db/traces.json q01 --full
"""
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def print_trace(r: dict, full: bool = False) -> None:
    cut = (lambda s, n: s) if full else (lambda s, n: s if len(s) <= n else s[:n] + " …")
    print(f"=== {r.get('query_id', '-')} · status: {r['status'].upper()} · {r.get('elapsed_s', '?')} s"
          f" · {r.get('n_searches', 0)} lượt tìm · token {r.get('tokens_in', 0)} vào / {r.get('tokens_out', 0)} ra")
    print(f"Hỏi: {r['question']}" + (f"   (filter người dùng: {r['filter']})" if r.get("filter") else ""))
    calls = iter(r.get("model_calls", []))
    step = 0
    for e in r["events"]:
        if e["event"] != "search":
            # starter run_agent logs a deliberate abstain (no citations) as invalid_or_missing_citations
            by_model = any(m.get("function") == "abstain" for m in r.get("model_calls", []))
            note = " (model gọi abstain: chủ động từ chối)" if e["event"] == "invalid_or_missing_citations" and by_model else ""
            print(f"\n[kết thúc] {e['event']}{note}")
            continue
        step += 1
        m = next(calls, {})
        who = "câu hỏi gốc" if m.get("source") == "original_question" else f"model ({m.get('latency_s', '?')} s)"
        print(f"\n[tool call {step}] search(query={e['query']!r}, filter={e['filter']})  ← {who}")
        for rank, c in enumerate(e["results"], 1):
            ranks = f" ranks={c['ranks']}" if c.get("ranks") else ""
            print(f"   {rank}. {c['id']}  tr.{c['page']}  score={c['score']}{ranks}")
            print(f"      {cut(' '.join(c['text'].split()), 160)}")
        print(f"   context sau lượt {step}: {len(e['context'])} ký tự, chunk {e['context_ids']}")
    final = next(calls, None)
    if final:
        label = "quyết định chưa thực hiện xong" if r["status"] == "error" else "quyết định model"
        print(f"\n[{label}] {final.get('function')}({cut(json.dumps(final.get('args'), ensure_ascii=False), 400)})"
              + (f"  · citation tự nối: {final['citations_appended']}" if final.get("citations_appended") else ""))
    searches = [e for e in r["events"] if e["event"] == "search"]
    if searches:
        print(f"\n[context cuối gửi model]\n{cut(searches[-1]['context'], 1500)}")
    if r["status"] == "error":
        print(f"\n[LỖI] {r['error']}\n{r.get('traceback', '')}")
    else:
        print(f"\n[trả lời] {r['answer']}\n[citations] {r['citations']}")


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("run", help="results folder name (agent-test-...) or path to traces.json")
    ap.add_argument("query_id")
    ap.add_argument("--full", action="store_true", help="do not shorten chunk text and context")
    args = ap.parse_args()
    path = Path(args.run)
    if not path.is_file():
        path = ROOT / "results" / args.run / "traces.json"
    traces = {t["query_id"]: t for t in json.loads(path.read_text(encoding="utf-8"))}
    if args.query_id not in traces:
        raise SystemExit(f"{args.query_id} không có trong {path}; có: {sorted(traces)}")
    print_trace(traces[args.query_id], args.full)


if __name__ == "__main__":
    main()
