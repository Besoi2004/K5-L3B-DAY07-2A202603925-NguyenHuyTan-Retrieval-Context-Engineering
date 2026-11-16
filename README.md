# Day 7 — Agentic RAG

**Bài cá nhân · Python 3.11+ · tiếp nối Day 6**

Dùng embedding và vector store từ Day 6 để xây một agent biết tìm bằng chứng, trả lời có nguồn và nhận biết khi không đủ thông tin. Bạn tự chọn kiến trúc, số tool và cách tổ chức retrieval.

> **Tùy chọn:** [Gợi ý dùng AI để lập trình](AGENT_SETUP.md) giúp bạn làm lab; phần này không bắt buộc và không tính điểm.

## Bài cần làm

![Agent tìm tài liệu trong kho Day 6 và trả lời có nguồn](assets/retrieval-pipeline.svg)

1. Kết nối dữ liệu, embedding và vector store Day 6.
2. Xây agent dùng model thật và ít nhất một khả năng truy xuất dữ liệu. Agent có thể dùng nhiều tool và nhiều lượt gọi.
3. Thử **ít nhất 3 phương pháp retrieval khác nhau**, trong đó có dense retrieval dùng vector store Day 6. Tự chọn các phương pháp còn lại; xem [gợi ý](GUIDE.md#2-thử-các-phương-pháp-retrieval).
4. Thử nhiều cấu hình, benchmark, phân tích lỗi và chọn cấu hình tốt trên **dev**; sau đó đánh giá trên **test**.

Benchmark tối thiểu có **24 câu**: dev gồm 15 câu có đáp án và 2 câu thiếu bằng chứng; test gồm 5 câu có đáp án và 2 câu thiếu bằng chứng. Xem [benchmark](BENCHMARK.md) và [rubric](RUBRIC.md).

## Thử thách nâng cao · +15 điểm

Index một tài liệu thực tế từ **100 trang** có bảng, ảnh và biểu đồ; xây agent truy xuất và trả lời các câu hỏi về nội dung đó. Hoàn thành [thử thách nâng cao](ADVANCED.md) và đạt **ít nhất 90% benchmark test** để nhận 15 điểm bonus. Phần cơ bản tối đa 85 điểm; toàn bài tối đa 100 điểm.

## Bắt đầu

1. Đọc [hướng dẫn](GUIDE.md), [rubric](RUBRIC.md) và [quy tắc](RULES.md).
2. Tạo repo cá nhân theo [cách nộp bài](SUBMISSION.md), chuẩn bị đầu ra Day 6 và model hỗ trợ tool calling.
3. Dùng hoặc thay thế [starter](starter/README.md); bạn cần kết nối model và vector store thật.
4. Chạy `python -m unittest discover -s tests -v`. Test mock chỉ kiểm tra code, không phải benchmark agent thật.

![Các bước thử nghiệm trên dev và đánh giá trên test](assets/experiment-loop.svg)

Nộp code, cách chạy, cấu hình, benchmark, trace và [báo cáo](report/individual/MSSV_HoTen.md). Thời gian ở [checkpoints](CHECKPOINTS.md) là gợi ý, có thể điều chỉnh theo lớp và phạm vi thử nghiệm.

---

## Bài làm — Nguyễn Huy Tấn (2A202603925)

Agent RAG trên **Nghị định 13/2023/NĐ-CP** (corpus, chunk và vector store lấy từ Day 6). Báo cáo: [report/individual/2A202603925_NguyenHuyTan.md](report/individual/2A202603925_NguyenHuyTan.md).

| Thành phần | Lựa chọn |
|---|---|
| Embedding | `google/embeddinggemma-2` (768 chiều, float32, chạy local CPU), prompt query `SearchQuery` giống Day 6 |
| Vector store | PostgreSQL 16 + pgvector 0.8.7 của Day 6, index `B` (113 chunk theo khoản/điều), cosine exact scan |
| Retrieval | `dense`, `bm25`, `hybrid_rrf` (dense + BM25, RRF k=60), thêm `tfidf` của starter — [src/retrievers.py](src/retrievers.py) |
| Agent | Gemini `gemini-3.5-flash-lite` (free tier, temperature 0), tool `search` / `final_answer` / `abstain` — [src/agent.py](src/agent.py) |
| Cấu hình đã chốt | `hybrid-orig-early-strict` — [results/selection.json](results/selection.json) |

### Cài đặt

1. Khởi động Postgres của Day 6 (dữ liệu nằm ở volume `day6_student_starter_pg_data`, nên **phải có `-p`**):
   ```bash
   cd "<repo Day 6>/starter" && docker compose -p day6_student_starter up -d
   ```
2. Tạo môi trường và cấu hình:
   ```bash
   python -m venv .venv && .venv/Scripts/python -m pip install -r requirements.txt
   cp .env.example .env   # điền GEMINI_API_KEY (Google AI Studio) và DAY6_DIR
   ```
3. Kiểm tra kết nối (vector store + Gemini gọi tool):
   ```bash
   .venv/Scripts/python src/check_setup.py
   ```

Embedding model đã được Day 6 tải vào cache HuggingFace; `HF_HUB_OFFLINE=1` trong `.env` bỏ qua bước kiểm tra Hub.

### Chạy lại toàn bộ

```bash
.venv/Scripts/python src/prepare_data.py                      # data/chunks.json, questions.json, cases.json
.venv/Scripts/python src/eval_retrieval.py --split dev        # so sánh retrieval, không dùng LLM
.venv/Scripts/python src/run_agent_bench.py --split dev --name dense-k3-b2400-s3
.venv/Scripts/python src/run_agent_bench.py --split dev --name dense-orig-early --first-query original --early-stop
.venv/Scripts/python src/run_agent_bench.py --split dev --name dense-orig-early-strict --first-query original --early-stop --strict-abstain
.venv/Scripts/python src/run_agent_bench.py --split dev --name hybrid-orig-early-strict --retriever hybrid_rrf --first-query original --early-stop --strict-abstain
.venv/Scripts/python src/score_agent.py --split dev           # chấm tự động bằng gold sau khi chạy
# chỉ sau khi chốt cấu hình (results/selection.json):
.venv/Scripts/python src/eval_retrieval.py --split test --methods dense,hybrid_rrf
.venv/Scripts/python src/run_agent_bench.py --split test --name dense-k3-b2400-s3
.venv/Scripts/python src/run_agent_bench.py --split test --name hybrid-orig-early-strict --retriever hybrid_rrf --first-query original --early-stop --strict-abstain
.venv/Scripts/python src/score_agent.py --split test
.venv/Scripts/python starter/agent_metrics.py --cases data/cases.json --traces results/agent-test-hybrid-orig-early-strict/traces.json --reviews results/agent-test-hybrid-orig-early-strict/reviews.json --split test --output results/agent-test-hybrid-orig-early-strict/agent_metrics.json
```

Gemini free tier giới hạn 15 request/phút và 500 request/ngày; `GEMINI_MIN_INTERVAL=4.5` giãn request, lỗi 429 được chờ rồi thử lại, lỗi còn lại ghi `status: "error"` trong trace.

### Xem trace và hỏi trực tiếp

```bash
.venv/Scripts/python src/show_trace.py agent-test-hybrid-orig-early-strict t03   # tool call, kết quả, context cuối, trả lời
.venv/Scripts/python src/ask.py "Chủ thể dữ liệu có quyền phản đối việc xử lý dữ liệu không?"
```

### Kết quả và dữ liệu

- `data/new_questions.json`: 5 câu test mới + 4 câu thiếu evidence (viết cho Day 7); `data/*.json` còn lại sinh bằng `prepare_data.py`.
- `results/retrieval-<split>/`: trace và summary retrieval; `results/agent-<split>-<config>/`: `traces.json`, `summary.json`, `review.md`; test có thêm `reviews.json` (nhãn tay) và `agent_metrics.json`.
- `results/selection_criteria.md` (ghi trước khi thử cải thiện), `results/selection.json` (cấu hình chốt trước test).
- `results/agent-dev-error-demo-bad-db/`: trace khi vector store không kết nối được (ghi lỗi, không có câu trả lời giả).

### Test

```bash
PYTHONUTF8=1 .venv/Scripts/python -m unittest discover -s tests -v
```

`PYTHONUTF8=1` cần trên Windows: `tests/test_baseline.py` của starter đọc file kết quả không chỉ định encoding (cp1252 mặc định). `tests/test_retrievers.py` kiểm tra BM25, filter, RRF và cách chấm, chạy offline.
