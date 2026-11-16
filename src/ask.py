"""Ask the agent one question live (selected config by default) and print its full trace.

    .venv/Scripts/python src/ask.py "Bên Kiểm soát dữ liệu phải thông báo vi phạm trong bao lâu?"
    .venv/Scripts/python src/ask.py "..." --filter document_type=phu_luc --save results/ask/demo.json
    .venv/Scripts/python src/ask.py            # interactive: type questions, empty line to quit
"""
import argparse
import json
import time
import traceback
from pathlib import Path

from agent import GeminiController, run_agent
from run_agent_bench import make_retriever
from show_trace import print_trace


def ask(question, controller, retriever, filters, args) -> dict:
    controller.log = []
    t0 = time.perf_counter()
    try:
        r = run_agent(question, controller, retriever, filters=filters, max_searches=args.max_searches,
                      top_k=args.top_k, budget=args.budget)
    except Exception as e:  # shown and saved, never replaced by a fake answer
        r = {"status": "error", "answer": None, "citations": [], "events": [],
             "error": f"{type(e).__name__}: {e}", "traceback": traceback.format_exc(limit=3)}
    r.update(query_id="ask", question=question, filter=filters, model_calls=controller.log,
             elapsed_s=round(time.perf_counter() - t0, 2),
             n_searches=sum(e["event"] == "search" for e in r["events"]),
             tokens_in=sum(m["tokens_in"] for m in controller.log),
             tokens_out=sum(m["tokens_out"] + m["tokens_thought"] for m in controller.log))
    return r


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("question", nargs="?")
    ap.add_argument("--filter", action="append", default=[], help="key=value, e.g. chuong=III (user-provided)")
    ap.add_argument("--retriever", default="hybrid_rrf", choices=("dense", "bm25", "hybrid_rrf"))
    ap.add_argument("--top-k", type=int, default=3)
    ap.add_argument("--budget", type=int, default=2400)
    ap.add_argument("--max-searches", type=int, default=3)
    ap.add_argument("--full", action="store_true")
    ap.add_argument("--save", type=Path, help="append traces to this JSON file")
    args = ap.parse_args()
    filters = dict(f.split("=", 1) for f in args.filter) or None
    retriever = make_retriever(args.retriever)
    # Selected config from results/selection.json
    controller = GeminiController(max_searches=args.max_searches, first_query="original",
                                  early_stop=True, strict_abstain=True)
    questions = [args.question] if args.question else iter(lambda: input("\nHỏi (Enter để thoát): ").strip(), "")
    saved = []
    for q in questions:
        r = ask(q, controller, retriever, filters, args)
        print()
        print_trace(r, args.full)
        saved.append(r)
    if args.save:
        args.save.parent.mkdir(parents=True, exist_ok=True)
        old = json.loads(args.save.read_text(encoding="utf-8")) if args.save.exists() else []
        args.save.write_text(json.dumps(old + saved, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
