"""Retrieval methods compared in Day 7. All return chunks in the Day 7 schema:
id, text, source_id, source, page, metadata, score, strategy (+ rank info for hybrid).

- DenseRetriever : embeddinggemma-2 query vector -> Day 6 pgvector index B (exact cosine)
- BM25Retriever  : Okapi BM25 over the same chunks, syllable tokens (baseline.tokenize)
- HybridRetriever: Reciprocal Rank Fusion of dense + BM25 candidate lists
Filters (chuong / document_type) come only from the question's user-provided `filter`.
"""
import math
import sys
from collections import Counter
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "starter"))
from baseline import tokenize  # noqa: E402


def _match(chunk: dict, filters: dict | None) -> bool:
    return all(chunk["metadata"].get(k) == v for k, v in (filters or {}).items())


class DenseRetriever:
    name = "dense"

    def __init__(self, embedder=None, store=None):
        from day6 import INDEX_NAME, load_embedder, open_store
        self.embedder = embedder or load_embedder()
        self.store = store or open_store(self.embedder.dimensions)
        self.index = INDEX_NAME

    def search(self, query: str, *, filters: dict | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        rows = self.store.search(self.index, self.embedder.embed_query(query), top_k=top_k, filters=filters)
        return [{"id": r["chunk_id"], "text": r["text"], "source_id": r["document_id"], "source": r["source"],
                 "page": r["page"], "metadata": r["metadata"], "score": r["score"], "strategy": self.name}
                for r in rows]


class BM25Retriever:
    name = "bm25"

    def __init__(self, chunks: list[dict], k1: float = 1.5, b: float = 0.75):
        self.chunks, self.k1, self.b = chunks, k1, b
        self.tf = [Counter(tokenize(c["text"])) for c in chunks]
        self.len = [sum(t.values()) for t in self.tf]
        self.avg = sum(self.len) / len(self.len)
        df = Counter(term for t in self.tf for term in t)
        n = len(chunks)
        self.idf = {t: math.log(1 + (n - d + 0.5) / (d + 0.5)) for t, d in df.items()}

    def search(self, query: str, *, filters: dict | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        terms = [t for t in set(tokenize(query)) if t in self.idf]
        scored = []
        for c, tf, dl in zip(self.chunks, self.tf, self.len):
            if not _match(c, filters):
                continue
            s = sum(self.idf[t] * tf[t] * (self.k1 + 1) / (tf[t] + self.k1 * (1 - self.b + self.b * dl / self.avg))
                    for t in terms if t in tf)
            if s > 0:
                scored.append({**c, "score": round(s, 4), "strategy": self.name})
        return sorted(scored, key=lambda c: (-c["score"], c["id"]))[:top_k]


class HybridRetriever:
    """RRF: score = sum 1/(k + rank) over dense and BM25; rank-based, so no score scaling needed."""
    name = "hybrid_rrf"

    def __init__(self, dense: DenseRetriever, bm25: BM25Retriever, k: int = 60, candidates: int = 20):
        self.dense, self.bm25, self.k, self.candidates = dense, bm25, k, candidates

    def search(self, query: str, *, filters: dict | None = None, top_k: int = 3) -> list[dict[str, Any]]:
        fused: dict[str, dict] = {}
        for r in (self.dense, self.bm25):
            for rank, c in enumerate(r.search(query, filters=filters, top_k=self.candidates), 1):
                row = fused.setdefault(c["id"], {**c, "score": 0.0, "strategy": self.name, "ranks": {}})
                row["score"] += 1 / (self.k + rank)
                row["ranks"][r.name] = rank
        out = sorted(fused.values(), key=lambda c: (-c["score"], c["id"]))[:top_k]
        for c in out:
            c["score"] = round(c["score"], 5)
        return out


if __name__ == "__main__":  # self-check on toy chunks (no DB needed)
    toy = [{"id": "a", "text": "thông báo vi phạm trong 72 giờ", "metadata": {"chuong": "II"}},
           {"id": "b", "text": "hồ sơ đánh giá tác động gửi trong 60 ngày", "metadata": {"chuong": "II"}},
           {"id": "c", "text": "trách nhiệm của Bộ Công an", "metadata": {"chuong": "III"}}]
    bm = BM25Retriever(toy)
    assert bm.search("72 giờ")[0]["id"] == "a"
    assert [c["id"] for c in bm.search("Bộ Công an", filters={"chuong": "II"})] == []

    class Fake:  # fixed ranking stands in for dense in this offline check only
        name = "dense"
        def search(self, q, *, filters=None, top_k=3): return [toy[1], toy[0]][:top_k]
    h = HybridRetriever(Fake(), bm).search("72 giờ")
    assert h[0]["id"] == "a" and h[0]["ranks"] == {"dense": 2, "bm25": 1}
    print("retrievers self-check OK")
