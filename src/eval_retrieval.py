"""Compare retrieval methods on one split (no LLM). Same corpus, questions, hit definition.

    .venv/Scripts/python src/eval_retrieval.py --split dev [--methods dense,bm25,hybrid_rrf,tfidf] [--budget 2400]

Hit@1 / Evidence Hit@3: a gold evidence string lies fully inside the rank-1 / a top-3 chunk of the
right source+page (starter baseline.hit). Context Evidence Rate: that chunk survives pack_context
under the char budget. Filter = the question's user-provided `filter` (never gold).
Writes results/retrieval-<split>/<method>_traces.json and summary.json.
"""
import argparse
import json
import statistics
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter"))
from baseline import TfidfIndex, hit, pack_context  # noqa: E402
from retrievers import BM25Retriever, DenseRetriever, HybridRetriever  # noqa: E402


class TfidfRetriever:  # starter baseline, no filter support (as documented in starter/README)
    name = "tfidf"
    def __init__(self, chunks): self.index = TfidfIndex(chunks)
    def search(self, query, *, filters=None, top_k=3): return self.index.search(query, top_k=top_k)


def evaluate(retriever, questions, budget: int, top_k: int = 3) -> list[dict]:
    traces = []
    for q in questions:
        t = time.perf_counter()
        results = retriever.search(q["question"], filters=q.get("filter"), top_k=top_k)
        ms = (time.perf_counter() - t) * 1000
        context, ids = pack_context(results, budget)
        marked = [{**c, "hit": hit(c, q["gold"])} for c in results]
        traces.append({"query_id": q["id"], "question": q["question"], "filter": q.get("filter"),
                       "method": retriever.name, "top_k": top_k, "budget_chars": budget,
                       "results": [{k: c.get(k) for k in ("id", "page", "score", "ranks", "hit", "text")} for c in marked],
                       "context_ids": ids, "context_chars": len(context), "search_ms": round(ms, 1),
                       "hit1": bool(marked and marked[0]["hit"]), "hit3": any(c["hit"] for c in marked),
                       "context_hit": any(c["hit"] and c["id"] in ids for c in marked)})
    return traces


def summarize(traces: list[dict]) -> dict:
    n = len(traces)
    def frac(key): k = sum(t[key] for t in traces); return {"n": k, "N": n, "rate": round(k / n, 3)}
    return {"hit1": frac("hit1"), "evidence_hit3": frac("hit3"), "context_evidence_rate": frac("context_hit"),
            "avg_context_chars": round(statistics.mean(t["context_chars"] for t in traces)),
            "median_search_ms": round(statistics.median(t["search_ms"] for t in traces), 1),
            "misses_at_3": [t["query_id"] for t in traces if not t["hit3"]], "cost_usd": 0}


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--split", required=True, choices=("dev", "test"))
    ap.add_argument("--methods", default="dense,bm25,hybrid_rrf,tfidf")
    ap.add_argument("--budget", type=int, default=2400)
    args = ap.parse_args()
    chunks = json.loads((ROOT / "data/chunks.json").read_text(encoding="utf-8"))
    questions = [q for q in json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))
                 if q["split"] == args.split]
    wanted = args.methods.split(",")
    bm25 = BM25Retriever(chunks)
    dense = DenseRetriever() if {"dense", "hybrid_rrf"} & set(wanted) else None
    all_methods = {"dense": dense, "bm25": bm25, "tfidf": TfidfRetriever(chunks),
                   "hybrid_rrf": dense and HybridRetriever(dense, bm25)}
    out = ROOT / "results" / f"retrieval-{args.split}"
    out.mkdir(parents=True, exist_ok=True)
    summary = {"split": args.split, "n_questions": len(questions), "budget_chars": args.budget, "top_k": 3,
               "embedding": "google/embeddinggemma-2:float32 (Day 6 index B, 113 chunks)", "methods": {}}
    for name in wanted:
        traces = evaluate(all_methods[name], questions, args.budget)
        (out / f"{name}_traces.json").write_text(json.dumps(traces, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        summary["methods"][name] = s = summarize(traces)
        print(f"{name:11s} Hit@1 {s['hit1']['n']}/{s['hit1']['N']}  Hit@3 {s['evidence_hit3']['n']}/{s['evidence_hit3']['N']}"
              f"  Context {s['context_evidence_rate']['n']}/{s['context_evidence_rate']['N']}"
              f"  {s['median_search_ms']} ms  miss@3 {s['misses_at_3']}")
    (out / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
