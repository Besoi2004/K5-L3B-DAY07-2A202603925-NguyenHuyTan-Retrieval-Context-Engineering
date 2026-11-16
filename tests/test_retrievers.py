"""Offline checks for Day 7 code (BM25, filter, RRF fusion, gold scoring). No DB or API needed."""
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from retrievers import BM25Retriever, HybridRetriever  # noqa: E402
from score_agent import score  # noqa: E402

CHUNKS = [
    {"id": "a", "text": "Thông báo vi phạm trong 72 giờ.", "source_id": "doc", "source": "doc.pdf", "page": 1,
     "metadata": {"chuong": "II", "document_type": "nghi_dinh"}},
    {"id": "b", "text": "Hồ sơ đánh giá tác động gửi trong 60 ngày.", "source_id": "doc", "source": "doc.pdf", "page": 2,
     "metadata": {"chuong": "II", "document_type": "nghi_dinh"}},
    {"id": "c", "text": "Mẫu số 04 hồ sơ đánh giá tác động.", "source_id": "doc", "source": "doc.pdf", "page": 3,
     "metadata": {"chuong": None, "document_type": "phu_luc"}},
]


class FixedDense:
    """Stands in for dense retrieval in offline tests only (never used for benchmark numbers)."""
    name = "dense"
    def __init__(self, order): self.order = order
    def search(self, query, *, filters=None, top_k=3):
        return [c for c in self.order if all(c["metadata"].get(k) == v for k, v in (filters or {}).items())][:top_k]


class RetrieverTests(unittest.TestCase):
    def test_bm25_ranks_exact_terms_first(self):
        self.assertEqual(BM25Retriever(CHUNKS).search("72 giờ")[0]["id"], "a")

    def test_bm25_filter_and_no_match(self):
        bm = BM25Retriever(CHUNKS)
        rows = bm.search("hồ sơ đánh giá tác động", filters={"document_type": "phu_luc"})
        self.assertEqual([r["id"] for r in rows], ["c"])
        self.assertEqual(bm.search("khôngkhớpgìcả"), [])

    def test_bm25_top_k_and_schema(self):
        rows = BM25Retriever(CHUNKS).search("hồ sơ", top_k=1)
        self.assertEqual(len(rows), 1)
        self.assertTrue({"id", "text", "source_id", "source", "page", "metadata", "score"} <= rows[0].keys())

    def test_rrf_fuses_ranks_and_keeps_unique_ids(self):
        hybrid = HybridRetriever(FixedDense([CHUNKS[1], CHUNKS[0], CHUNKS[2]]), BM25Retriever(CHUNKS))
        rows = hybrid.search("72 giờ", top_k=3)
        self.assertEqual(rows[0]["id"], "a")  # dense rank 2 + bm25 rank 1 beats dense rank 1 only
        self.assertEqual(rows[0]["ranks"], {"dense": 2, "bm25": 1})
        self.assertEqual(len({r["id"] for r in rows}), len(rows))

    def test_rrf_passes_filter_to_both_retrievers(self):
        hybrid = HybridRetriever(FixedDense(CHUNKS), BM25Retriever(CHUNKS))
        rows = hybrid.search("hồ sơ đánh giá", filters={"document_type": "phu_luc"})
        self.assertEqual([r["id"] for r in rows], ["c"])


class ScoreTests(unittest.TestCase):
    def test_score_uses_final_context_and_separates_errors(self):
        gold = {"q1": [{"source_id": "doc", "page": 1, "evidence": "72 giờ"}]}
        cases = {"q1": {"answerable": True}, "u1": {"answerable": False}, "q2": {"answerable": True}}
        traces = [
            {"query_id": "q1", "status": "answered", "citations": ["a"], "n_searches": 1, "elapsed_s": 1,
             "tokens_in": 10, "tokens_out": 2, "model_calls": [],
             "events": [{"event": "search", "context_ids": ["a", "b"]}, {"event": "answer"}]},
            {"query_id": "u1", "status": "abstain", "citations": [], "n_searches": 1, "elapsed_s": 1,
             "tokens_in": 10, "tokens_out": 2, "model_calls": [], "events": [{"event": "search", "context_ids": ["b"]}]},
            {"query_id": "q2", "status": "error", "citations": [], "n_searches": 0, "elapsed_s": 1,
             "tokens_in": 0, "tokens_out": 0, "model_calls": [], "events": []},
        ]
        s = score(traces, cases, gold, {c["id"]: c for c in CHUNKS})
        self.assertEqual((s["context_evidence"], s["answerable"]), (1, 1))
        self.assertEqual((s["abstained_unanswerable"], s["errors"]), (1, 1))
        self.assertEqual((s["cited_gold"], s["correct_behaviour"]), (1, 2))


if __name__ == "__main__":
    unittest.main()
