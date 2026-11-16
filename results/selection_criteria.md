# Tiêu chí chọn cấu hình (ghi trước khi chạy các cấu hình cải thiện)

Ghi ngày 2026-11-16, sau baseline agent dev `agent-dev-dense-k3-b2400-s3`, **trước** khi chạy bất kỳ cấu hình cải thiện nào và trước mọi lần chạy test.

Chỉ dùng dev (22 câu có đáp án + 2 câu thiếu evidence). So sánh theo thứ tự, chỉ xét tiêu chí sau khi tiêu chí trước hòa:

1. **Context Evidence Rate của agent** (context cuối gửi model có chunk chứa evidence gold) — không được giảm so với baseline.
2. **Hành vi đúng** = số câu có đáp án được trả lời + số câu thiếu evidence bị từ chối (tự động từ status; tối đa 24).
3. **Citation trúng gold** (proxy tự động: ít nhất một chunk được trích chứa evidence gold) / số câu trả lời.
4. **Chi phí**: tổng token và thời gian trung vị mỗi câu; ưu tiên cấu hình rẻ hơn nếu 1–3 hòa.

Chấm tay (answer_grade, citation_support) dùng để xác nhận cấu hình đã chọn và báo cáo, không thay các tiêu chí tự động ở trên khi chọn. Với 24 câu dev, chênh lệch 1 câu ≈ 4 điểm phần trăm nên không kết luận thống kê.

## Giả thuyết các cấu hình

| Tên | Thay đổi so với cấu hình trước | Giả thuyết (từ lỗi dev) |
|---|---|---|
| baseline `dense-k3-b2400-s3` | Gemini tự viết query, luôn được nhắc "còn N lượt tìm" | — |
| cải thiện 1 `dense-orig-early` | Lượt tìm đầu dùng nguyên câu hỏi; prompt cho phép trả lời ngay khi context đủ | Sửa q17 (query viết lại làm mất tr. 25) và giảm token/thời gian (24/24 câu đang dùng hết 3 lượt) |
| cải thiện 2 `dense-orig-early-strict` | + quy tắc: hỏi con số mà context chỉ có nguyên tắc chung thì phải từ chối | Sửa u02 (trả lời bằng nguyên tắc thay vì nói không có số năm) mà không tăng từ chối nhầm |
| phương pháp 3 `hybrid-orig-early-strict` | Đổi retriever dense → hybrid RRF (dense + BM25) | Hybrid có Hit@1 dev 17/22 so với 16/22 của dense; kiểm tra lợi ích này có giữ ở mức agent không |
