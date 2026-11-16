# Review agent — chấm tay

Với mỗi câu: answer_grade 0/1/2 (câu có đáp án), citation_support đúng/sai cho từng citation, abstention_correct (câu thiếu evidence). Đọc nguyên văn chunk, không chỉ nhìn ID.

## t01 · có đáp án · status `answered`
**Hỏi:** Khi cơ quan nhà nước có thẩm quyền xử lý dữ liệu cá nhân để phục vụ hoạt động của mình thì có phải thông báo cho chủ thể dữ liệu trước không?

**Đáp án chuẩn (chỉ để chấm):** Không bắt buộc. Nghĩa vụ thông báo một lần trước khi xử lý không áp dụng khi dữ liệu được cơ quan nhà nước có thẩm quyền xử lý để phục vụ hoạt động của cơ quan nhà nước theo quy định pháp luật (Điều 13 khoản 4 điểm b).

**Query đã tìm:** ['cơ quan nhà nước xử lý dữ liệu cá nhân phục vụ hoạt động thông báo chủ thể dữ liệu', 'Bên Kiểm soát dữ liệu cá nhân không cần thực hiện quy định tại khoản 1 Điều này trong các trường hợp sau', 'Điều 13 Nghị định 13/2023']
**Agent trả lời:** Khi dữ liệu cá nhân được xử lý bởi cơ quan nhà nước có thẩm quyền với mục đích phục vụ hoạt động của cơ quan nhà nước theo quy định của pháp luật, thì không phải thực hiện quy định về việc thông báo cho chủ thể dữ liệu trước khi thu thập/xử lý theo khoản 1 Điều này [nd13-2023:p11:paragraph:000].

- `[nd13-2023:p11:paragraph:000]` tr. 11:

  > 4. Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân
  > không cân thực hiện quy định tại khoản 1 Điều này trong các trường hợp sau:
  > 
  > a) Chủ thể dữ liệu đã biết rõ và đồng ý toàn bộ với nội dung quy định tại
  > khoản 1 và khoản 2 Điều này trước khi đông ý cho Bên Kiêm soát dữ liệu cá
  > nhân, Bên Kiêm soát và xử lý dữ liệu cá nhân tiên hành thu thập dữ liệu cá
  > nhân, phù hợp với các quy định tại Điêu 9 Nghị định này;
  > 
  > b) Dữ liệu cá nhân được xử lý bởi cơ quan nhà nước có thẩm quyền với
  > mục đích phục vụ hoạt động của cơ quan nhà nước theo quy định của pháp luật.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## t02 · có đáp án · status `answered`
**Hỏi:** Nếu tôi rút lại sự đồng ý thì việc xử lý dữ liệu của tôi trước đó có bị coi là bất hợp pháp không?

**Đáp án chuẩn (chỉ để chấm):** Không. Rút lại sự đồng ý không ảnh hưởng đến tính hợp pháp của việc xử lý dữ liệu đã được đồng ý trước khi rút lại (Điều 12 khoản 1).

**Query đã tìm:** ['rút lại sự đồng ý xử lý dữ liệu trước đó hợp pháp']
**Agent trả lời:** Việc rút lại sự đồng ý không ảnh hưởng đến tính hợp pháp của việc xử lý dữ liệu đã được đồng ý trước khi rút lại sự đồng ý [nd13-2023:p10:paragraph:001].

- `[nd13-2023:p10:paragraph:001]` tr. 10:

  > Điều 12. Rút lại sự đồng ý
  > 
  > 1. Việc rút lại sự đồng ý không ảnh hưởng đến tính hợp pháp của việc xử
  > lý dữ liệu đã được đông ý trước khi rút lại sự đông ý.
  > 
  > 2. Việc rút lại sự đồng ý phải được thể hiện ở một định dạng có thể được
  > in, sao chép băng văn bản, bao gồm cả dưới dạng điện tử hoặc định dạng kiểm
  > chứng được.
  > 
  > 3. Khi nhận yêu cầu rút lại sự đồng ý của chủ thể dữ liệu, Bên Kiểm soát dữ
  > liệu cá nhân, Bên Kiêm soát và xử lý dữ liệu cá nhân thông báo cho chú thê dữ
  > liệu vê hậu quả, thiệt hại có thê xây ra khi rút lại sự đông ý.
  > 
  > 4. Sau khi thực hiện quy định tại khoản 2 Điều này, Bên Kiểm soát dữ
  > liệu, Bên Xử lý dữ liệu, Bên Kiểm soát và xử lý dữ liệu, Bên thứ ba phải ngừng
  > và yêu cầu các tổ chức, cá nhân có liên quan ngừng xử lý dữ liệu của chủ thể
  > dữ liệu đã rút lại sự đồng ý.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## t03 · có đáp án · status `abstain`
**Hỏi:** Trước khi xóa không thể khôi phục hoặc hủy thiết bị chứa dữ liệu cá nhân, cần kiểm tra gì?

**Đáp án chuẩn (chỉ để chấm):** Kiểm tra an ninh mạng đối với hệ thống và phương tiện, thiết bị phục vụ xử lý dữ liệu cá nhân (Điều 27 khoản 4).

**Query đã tìm:** ['xóa không thể khôi phục hoặc hủy thiết bị chứa dữ liệu cá nhân', 'xóa không thể khôi phục thiết bị chứa dữ liệu cá nhân', 'xóa không thể khôi phục hoặc hủy thiết bị chứa dữ liệu cá nhân']
**Agent trả lời:** Không đủ bằng chứng để trả lời.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## t04 · có đáp án · status `answered`
**Hỏi:** Trong kinh doanh dịch vụ tiếp thị, giới thiệu sản phẩm quảng cáo, ai phải chứng minh việc sử dụng dữ liệu cá nhân của khách hàng là đúng quy định?

**Đáp án chuẩn (chỉ để chấm):** Tổ chức, cá nhân kinh doanh dịch vụ tiếp thị, giới thiệu sản phẩm quảng cáo (Điều 21 khoản 3).

**Query đã tìm:** ['kinh doanh dịch vụ tiếp thị giới thiệu sản phẩm quảng cáo chứng minh việc sử dụng dữ liệu cá nhân', 'chứng minh việc sử dụng dữ liệu cá nhân của khách hàng đúng với quy định', 'Tổ chức cá nhân kinh doanh dịch vụ tiếp thị giới thiệu sản phẩm quảng cáo có trách nhiệm chứng minh']
**Agent trả lời:** Trong kinh doanh dịch vụ tiếp thị, giới thiệu sản phẩm quảng cáo, tổ chức, cá nhân kinh doanh dịch vụ tiếp thị, giới thiệu sản phẩm quảng cáo có trách nhiệm chứng minh việc sử dụng dữ liệu cá nhân của khách hàng được giới thiệu sản phẩm đúng với quy định [nd13-2023:p17:paragraph:000].

- `[nd13-2023:p17:paragraph:000]` tr. 17:

  > 3. Tỗ chức, cá nhân kinh doanh dịch vụ tiếp thị, giới thiệu sản phẩm quảng
  > cáo có trách nhiệm chứng minh việc sử dụng dữ liệu cá nhân của khách hàng
  > được giới thiệu sản phẩm đúng với quy định tại khoản 1 và khoản 2 Điều này.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## t05 · có đáp án · status `answered`
**Hỏi:** Biện pháp bảo vệ dữ liệu cá nhân phải được áp dụng từ thời điểm nào?

**Đáp án chuẩn (chỉ để chấm):** Ngay từ khi bắt đầu và trong suốt quá trình xử lý dữ liệu cá nhân (Điều 26 khoản 1).

**Query đã tìm:** ['Biện pháp bảo vệ dữ liệu cá nhân phải được áp dụng từ thời điểm nào', 'Biện pháp bảo vệ dữ liệu cá nhân được áp dụng ngay từ khi bắt đầu', 'Biện pháp bảo vệ dữ liệu cá nhân được áp dụng ngay từ khi bắt đầu']
**Agent trả lời:** Biện pháp bảo vệ dữ liệu cá nhân phải được áp dụng ngay từ khi bắt đầu và trong suốt quá trình xử lý dữ liệu cá nhân [nd13-2023:p21:paragraph:003].

- `[nd13-2023:p21:paragraph:003]` tr. 21:

  > Mục 4
  > BIỆN PHÁP, ĐIỀU KIỆN BẢO ĐÁM BẢO VỆ DỮ LIỆU CÁ NHÂN
  > 
  > Điều 26. Biện pháp báo vệ dữ liệu cá nhân
  > 1, Biện pháp bảo vệ dữ liệu cá nhân được áp dụng ngay từ khi bắt đầu và
  > trong suôt quá trình xử lý dữ liệu cá nhân.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## u03 · THIẾU EVIDENCE · status `abstain`
**Hỏi:** Nhân sự phụ trách bảo vệ dữ liệu cá nhân phải có bằng cấp hoặc chứng chỉ gì?

**Lý do thiếu:** Grep 'chứng chỉ', 'bằng cấp', 'trình độ' = 0 kết quả. Điều 28 khoản 2 chỉ yêu cầu chỉ định nhân sự phụ trách, không nêu tiêu chuẩn bằng cấp.

**Query đã tìm:** ['nhân sự phụ trách bảo vệ dữ liệu cá nhân bằng cấp chứng chỉ', 'Điều 30 Nghị định 13 2023 nhân sự phụ trách bảo vệ dữ liệu cá nhân', 'Điều 30 Nghị định 13 2023 chứng chỉ bằng cấp']
**Agent trả lời:** Không đủ bằng chứng để trả lời.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## u04 · THIẾU EVIDENCE · status `abstain`
**Hỏi:** Lệ phí thẩm định hồ sơ đánh giá tác động xử lý dữ liệu cá nhân là bao nhiêu?

**Lý do thiếu:** Grep 'lệ phí', 'thẩm định' = 0 kết quả; 'phí' chỉ có 'chi phí thực tế để in, sao, chụp' khi cung cấp dữ liệu (tr. 12) và 'kinh phí' (Điều 31). Không có lệ phí cho hồ sơ đánh giá tác động.

**Query đã tìm:** ['lệ phí thẩm định hồ sơ đánh giá tác động xử lý dữ liệu cá nhân', 'lệ phí thẩm định đánh giá tác động xử lý dữ liệu cá nhân', 'lệ phí phí thẩm định đánh giá tác động xử lý dữ liệu cá nhân']
**Agent trả lời:** Không đủ bằng chứng để trả lời.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---
