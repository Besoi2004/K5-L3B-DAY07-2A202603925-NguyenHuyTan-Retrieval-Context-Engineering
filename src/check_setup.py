"""Step 1 smoke test: Day 6 vector store + embedding, and the Gemini agent model.

Run from the repo root:  .venv/Scripts/python src/check_setup.py
"""
import os
import time

from day6 import INDEX_NAME, MODEL_KEY, load_embedder, open_store


def check_vector_store() -> None:
    t = time.perf_counter()
    embedder = load_embedder()
    print(f"[embed] {embedder.model_name} dims={embedder.dimensions} load={time.perf_counter() - t:.1f}s")
    store = open_store(embedder.dimensions)
    with store._connect() as conn:
        models = [r[0] for r in conn.execute(
            "SELECT DISTINCT model FROM chunks WHERE index_name = %s", (INDEX_NAME,))]
    if models != [MODEL_KEY]:
        raise RuntimeError(f"index {INDEX_NAME} built with {models}, expected {MODEL_KEY}")
    print(f"[store] index {INDEX_NAME}: {store.count(INDEX_NAME)} chunks, model {models[0]}")
    t = time.perf_counter()
    rows = store.search(INDEX_NAME, embedder.embed_query("Chủ thể dữ liệu là ai?"), top_k=3)
    print(f"[dense] top-3 in {(time.perf_counter() - t) * 1000:.0f} ms")
    for r in rows:
        print(f"   {r['score']:.3f} {r['chunk_id']} p{r['page']}: {r['text'][:70]!r}")


def check_gemini() -> None:
    from google import genai
    from google.genai import types

    if not os.getenv("GEMINI_API_KEY"):
        raise RuntimeError("GEMINI_API_KEY trống trong .env")
    model = os.getenv("GEMINI_MODEL", "gemini-3.5-flash-lite")
    client = genai.Client()  # reads GEMINI_API_KEY
    search = types.FunctionDeclaration(
        name="search", description="Tìm đoạn văn bản trong Nghị định 13/2023 về bảo vệ dữ liệu cá nhân.",
        parameters_json_schema={"type": "object", "properties": {"query": {"type": "string"}},
                                "required": ["query"]})
    t = time.perf_counter()
    resp = client.models.generate_content(
        model=model, contents="Chủ thể dữ liệu là ai? Hãy tìm trong tài liệu trước khi trả lời.",
        config=types.GenerateContentConfig(
            tools=[types.Tool(function_declarations=[search])],
            automatic_function_calling=types.AutomaticFunctionCallingConfig(disable=True)))
    calls = resp.function_calls or []
    print(f"[gemini] {model} {(time.perf_counter() - t):.1f}s tool_calls={[(c.name, c.args) for c in calls]}")
    print(f"   usage: {resp.usage_metadata.prompt_token_count} in / {resp.usage_metadata.candidates_token_count} out")
    if not calls:
        raise RuntimeError("model không gọi tool search; kiểm tra lại model có hỗ trợ function calling")


if __name__ == "__main__":
    check_vector_store()
    check_gemini()
    print("OK: bước 1 sẵn sàng")
