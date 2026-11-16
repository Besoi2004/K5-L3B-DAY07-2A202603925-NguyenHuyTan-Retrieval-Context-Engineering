"""Connect to the Day 6 embedding model and pgvector store (code reused from the Day 6 repo)."""
import os
import sys
from pathlib import Path

from dotenv import load_dotenv

ROOT = Path(__file__).resolve().parents[1]
load_dotenv(ROOT / ".env")
DAY6_DIR = Path(os.getenv("DAY6_DIR", ""))
if not (DAY6_DIR / "starter" / "src" / "store.py").exists():
    raise RuntimeError(f"DAY6_DIR={DAY6_DIR!s} không phải repo Day 6; sửa trong .env")
sys.path.insert(0, str(DAY6_DIR / "starter"))

from src.embeddings import SentenceTransformerEmbedder  # noqa: E402  (Day 6 package)
from src.store import PgVectorStore  # noqa: E402

# Must match Day 6 src/run.py EMBEDDING exactly, or query vectors won't match the index.
EMBEDDING = {
    "model": "google/embeddinggemma-2",
    "query_prompt": "SearchQuery",
    "document_prompt": "Document",
    "load_kwargs": {"config_kwargs": {"vision_config": None, "audio_config": None},
                    "model_kwargs": {"dtype": "float32"}},
    "max_seq_length": 8192,
}
MODEL_KEY = f"{EMBEDDING['model']}:float32"
INDEX_NAME = "B"  # Day 6 selected strategy C = index B + optional filter


def load_embedder() -> SentenceTransformerEmbedder:
    return SentenceTransformerEmbedder(EMBEDDING["model"], EMBEDDING["query_prompt"],
                                       EMBEDDING["document_prompt"], EMBEDDING["load_kwargs"],
                                       max_seq_length=EMBEDDING["max_seq_length"])


def open_store(dimensions: int) -> PgVectorStore:
    return PgVectorStore(os.getenv("DATABASE_URL", ""), dimensions)
