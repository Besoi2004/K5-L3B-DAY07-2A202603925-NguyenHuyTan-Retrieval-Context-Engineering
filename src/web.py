"""Local web UI for the agent: ask live questions or browse saved benchmark traces.

    .venv/Scripts/python src/web.py            # then open http://127.0.0.1:8007

Standard library only (http.server). Binds to localhost. Each live question is appended to
results/ask/web.json. Gold answers are never sent to the agent; the page shows them only when
browsing a saved benchmark trace (grader view).
"""
import json
import threading
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from types import SimpleNamespace
from urllib.parse import parse_qs, urlparse

from agent import GeminiController
from ask import ask
from retrievers import BM25Retriever, DenseRetriever, HybridRetriever

ROOT = Path(__file__).resolve().parents[1]
RESULTS = ROOT / "results"
PAGE = Path(__file__).with_name("web.html")
LOG = RESULTS / "ask" / "web.json"
PRESETS = {  # the two configs compared on test (results/selection.json)
    "selected": {"label": "Đã chốt: hybrid-orig-early-strict", "retriever": "hybrid_rrf",
                 "controller": dict(first_query="original", early_stop=True, strict_abstain=True)},
    "baseline": {"label": "Baseline: dense-k3-b2400-s3", "retriever": "dense", "controller": {}},
}
PARAMS = SimpleNamespace(top_k=3, budget=2400, max_searches=3)

print("Đang nạp embedding model và kết nối vector store...", flush=True)
CHUNKS = json.loads((ROOT / "data/chunks.json").read_text(encoding="utf-8"))
DENSE = DenseRetriever()
BM25 = BM25Retriever(CHUNKS)
RETRIEVERS = {"dense": DENSE, "bm25": BM25, "hybrid_rrf": HybridRetriever(DENSE, BM25)}
CONTROLLERS = {k: GeminiController(max_searches=PARAMS.max_searches, **p["controller"]) for k, p in PRESETS.items()}
LOCK = threading.Lock()  # controller keeps a per-question log; serve one question at a time
CASES = {c["id"]: c for c in json.loads((ROOT / "data/cases.json").read_text(encoding="utf-8"))}
GOLD = {q["id"]: q for q in json.loads((ROOT / "data/questions.json").read_text(encoding="utf-8"))}


def list_runs() -> list[dict]:
    runs = []
    for f in sorted(RESULTS.glob("agent-*/traces.json")):
        traces = json.loads(f.read_text(encoding="utf-8"))
        runs.append({"run": f.parent.name, "queries": [{"id": t["query_id"], "status": t["status"]} for t in traces]})
    return runs


def load_trace(run: str, qid: str) -> dict:
    path = (RESULTS / run / "traces.json").resolve()
    if RESULTS.resolve() not in path.parents or not path.is_file():
        raise ValueError("run không hợp lệ")
    trace = next((t for t in json.loads(path.read_text(encoding="utf-8")) if t["query_id"] == qid), None)
    if trace is None:
        raise ValueError(f"{qid} không có trong {run}")
    reviews = path.parent / "reviews.json"
    review = next((r for r in json.loads(reviews.read_text(encoding="utf-8")) if r["query_id"] == qid), None) \
        if reviews.is_file() else None
    case, gold = CASES.get(qid, {}), GOLD.get(qid)
    trace["grader"] = {"answerable": case.get("answerable"), "expected_answer": gold and gold["expected_answer"],
                       "gold": gold and gold["gold"], "absence_reason": case.get("absence_reason"), "review": review}
    return trace


class Handler(BaseHTTPRequestHandler):
    def _send(self, code: int, body: bytes, ctype: str) -> None:
        self.send_response(code)
        self.send_header("Content-Type", ctype)
        self.send_header("Content-Length", str(len(body)))
        self.end_headers()
        self.wfile.write(body)

    def _json(self, obj, code: int = 200) -> None:
        self._send(code, json.dumps(obj, ensure_ascii=False).encode("utf-8"), "application/json; charset=utf-8")

    def do_GET(self) -> None:
        url = urlparse(self.path)
        q = {k: v[0] for k, v in parse_qs(url.query).items()}
        try:
            if url.path == "/":
                self._send(200, PAGE.read_bytes(), "text/html; charset=utf-8")
            elif url.path == "/api/meta":
                self._json({"presets": {k: p["label"] for k, p in PRESETS.items()}, "params": vars(PARAMS),
                            "model": CONTROLLERS["selected"].model, "runs": list_runs()})
            elif url.path == "/api/trace":
                self._json(load_trace(q.get("run", ""), q.get("qid", "")))
            else:
                self._json({"error": "not found"}, 404)
        except ValueError as e:
            self._json({"error": str(e)}, 400)

    def do_POST(self) -> None:
        if self.path != "/api/ask":
            return self._json({"error": "not found"}, 404)
        try:
            body = json.loads(self.rfile.read(int(self.headers.get("Content-Length", 0))) or b"{}")
            question = str(body.get("question", "")).strip()
            preset = PRESETS.get(body.get("preset", "selected"))
            if not question or len(question) > 1000 or preset is None:
                raise ValueError("câu hỏi rỗng/quá dài hoặc cấu hình không hợp lệ")
            filters = {k: v for k, v in (body.get("filter") or {}).items() if k in ("chuong", "document_type") and v} or None
        except (ValueError, json.JSONDecodeError) as e:
            return self._json({"error": str(e)}, 400)
        with LOCK:  # errors inside the agent are returned as status "error" by ask(), not hidden
            trace = ask(question, CONTROLLERS[body.get("preset", "selected")], RETRIEVERS[preset["retriever"]], filters, PARAMS)
        trace["preset"] = preset["label"]
        LOG.parent.mkdir(parents=True, exist_ok=True)
        old = json.loads(LOG.read_text(encoding="utf-8")) if LOG.exists() else []
        LOG.write_text(json.dumps(old + [trace], ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        self._json(trace)

    def log_message(self, fmt, *args) -> None:  # quieter console
        if "/api/ask" in (args[0] if args else ""):
            super().log_message(fmt, *args)


if __name__ == "__main__":
    server = ThreadingHTTPServer(("127.0.0.1", 8007), Handler)
    print("Giao diện agent: http://127.0.0.1:8007", flush=True)
    server.serve_forever()
