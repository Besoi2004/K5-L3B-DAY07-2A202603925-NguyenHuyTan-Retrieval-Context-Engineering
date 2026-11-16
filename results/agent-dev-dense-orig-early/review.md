# Review agent — chấm tay

Với mỗi câu: answer_grade 0/1/2 (câu có đáp án), citation_support đúng/sai cho từng citation, abstention_correct (câu thiếu evidence). Đọc nguyên văn chunk, không chỉ nhìn ID.

## q01 · có đáp án · status `answered`
**Hỏi:** Chủ thể dữ liệu là ai?

**Đáp án chuẩn (chỉ để chấm):** Là cá nhân được dữ liệu cá nhân phản ánh.

**Query đã tìm:** ['Chủ thể dữ liệu là ai?']
**Agent trả lời:** Chủ thể dữ liệu là cá nhân được dữ liệu cá nhân phản ánh [nd13-2023:p03:paragraph:002].

- `[nd13-2023:p03:paragraph:002]` tr. 3:

  > 6. Chủ thể dữ liệu là cá nhân được dữ liệu cá nhân phản ánh.
  > 
  > 7. Xử lý dữ liệu cá nhân là một hoặc nhiều hoạt động tác động tới dữ liệu
  > cá nhân, như: thu thập, ghi, phân tích, xác nhận, lưu trữ, chỉnh sửa, công khai,
  > kết hợp, truy cập, truy xuất, thu hồi, mã hóa, giải mã, sao chép, chia sẻ, truyền
  > đưa, cung cấp, chuyển giao, xóa, hủy dữ liệu cá nhân hoặc các hành động khác
  > có liên quan.
  > 
  > 8.Sự đồng ý của chủ thể dữ liệu là việc thể hiện rõ ràng, tự nguyện, khẳng
  > định việc cho phép xử lý dữ liệu cá nhân của chủ thê dữ liệu.
  > 
  > 9, Bên Kiểm soát dữ liệu cá nhân là tổ chức, cá nhân quyết định mục đích và
  > phương tiện xử lý dữ liệu cá nhân.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q02 · có đáp án · status `answered`
**Hỏi:** Thông tin về nhóm máu có được xem là dữ liệu cá nhân nhạy cảm về sức khỏe không?

**Đáp án chuẩn (chỉ để chấm):** Không. Tình trạng sức khỏe trong hồ sơ bệnh án là dữ liệu nhạy cảm nhưng không bao gồm thông tin về nhóm máu.

**Query đã tìm:** ['Thông tin về nhóm máu có được xem là dữ liệu cá nhân nhạy cảm về sức khỏe không?']
**Agent trả lời:** Không, thông tin về nhóm máu không bao gồm trong dữ liệu cá nhân nhạy cảm về tình trạng sức khỏe [nd13-2023:p02:paragraph:002].

- `[nd13-2023:p02:paragraph:002]` tr. 2:

  > 4. Dữ liệu cá nhân nhạy cảm là dữ liệu cá nhân gắn liền với quyền riêng
  > tư của cá nhân mà khi bị xâm phạm sẽ gây ảnh hưởng trực tiếp tới quyền và lợi
  > ích hợp pháp của cá nhân gồm:
  > 
  > a) Quan điểm chính trị, quan điểm tôn giáo;
  > 
  > b) Tình trạng sức khỏe và đời tư được ghỉ trong hồ sơ bệnh án, không bao
  > gôm thông tin về nhóm máu;

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q03 · có đáp án · status `answered`
**Hỏi:** Nếu người dùng không trả lời gì thì có được coi là đã đồng ý cho xử lý dữ liệu không?

**Đáp án chuẩn (chỉ để chấm):** Không. Sự im lặng hoặc không phản hồi không được coi là sự đồng ý.

**Query đã tìm:** ['Nếu người dùng không trả lời gì thì có được coi là đã đồng ý cho xử lý dữ liệu không?']
**Agent trả lời:** Không, sự im lặng hoặc không phản hồi của chủ thể dữ liệu không được coi là sự đồng ý [nd13-2023:p09:paragraph:001].

- `[nd13-2023:p09:paragraph:001]` tr. 9:

  > 4. Sự đồng ý phải được tiến hành cho cùng một mục đích. Khi có nhiều
  > mục đích, Bên Kiểm soát dữ liệu cá nhân, Bên Kiêm soát và xử lý dữ liệu cá
  > nhân liệt kê các mục đích đê chủ thê dữ liệu đồng ý với một hoặc nhiêu mục
  > đích nêu ra.
  > 
  > _.5. Sự đồng ý của chủ thể dữ liệu phải được thể hiện ở một định dạng có
  > thê được in, sao chép băng văn bản, bao gồm cả dưới dạng điện tử hoặc định
  > 
  > dạng kiểm chứng được.
  > 
  > 6. Sự im lặng hoặc không phản hồi của chủ thể dữ liệu không được coi là
  > sự đông ý.
  > 
  > 7. Chủ thế dữ liệu có thể đồng ý một phần hoặc với điều kiện kèm theo.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q04 · có đáp án · status `answered`
**Hỏi:** Khi phát hiện vi phạm quy định bảo vệ dữ liệu cá nhân, Bên Kiểm soát dữ liệu phải thông báo cho Bộ Công an trong thời hạn nào?

**Đáp án chuẩn (chỉ để chấm):** Chậm nhất 72 giờ sau khi xảy ra hành vi vi phạm, theo Mẫu số 03.

**Query đã tìm:** ['Khi phát hiện vi phạm quy định bảo vệ dữ liệu cá nhân, Bên Kiểm soát dữ liệu phải thông báo cho Bộ Công an trong thời hạn nào?']
**Agent trả lời:** Khi phát hiện xảy ra vi phạm quy định bảo vệ dữ liệu cá nhân, Bên Kiểm soát dữ liệu cá nhân (và Bên Kiểm soát và xử lý dữ liệu cá nhân) phải thông báo cho Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao) chậm nhất là 72 giờ sau khi xảy ra hành vi vi phạm. Trường hợp thông báo sau 72 giờ thì phải kèm theo lý do thông báo chậm, muộn [nd13-2023:p17:paragraph:002].

- `[nd13-2023:p17:paragraph:002]` tr. 17:

  > Điều 23. Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân
  > 
  > 1. Trường hợp phát hiện xảy ra vi phạm quy định bảo vệ dữ liệu cá nhân,
  > Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân thông
  > báo cho Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng
  > công nghệ cao) chậm nhất 72 giờ sau khi xảy ra hành vi vi phạm theo Mẫu số
  > 03 tại Phụ lục của Nghị định này. Trường hợp thông báo sau 72 giờ thì phải
  > kèm theo lý do thông báo chậm, muộn.
  > 
  > 2. Bên Xử lý dữ liệu cá nhân phải thông báo cho Bên Kiểm soát dữ liệu
  > cá nhân một cách nhanh nhất có thể sau khi nhận thấy có sự vi phạm quy định
  > về bảo vệ dữ liệu cá nhân.
  > 
  > 3. Nội dung thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân:
  > 
  > a) Mô tả tính chất của việc vi phạm quy định bảo vệ dữ liệu cá nhân, bao

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q05 · có đáp án · status `answered`
**Hỏi:** Nếu thông báo vi phạm gửi muộn hơn 72 giờ thì phải làm gì thêm?

**Đáp án chuẩn (chỉ để chấm):** Phải kèm theo lý do thông báo chậm, muộn.

**Query đã tìm:** ['Nếu thông báo vi phạm gửi muộn hơn 72 giờ thì phải làm gì thêm?']
**Agent trả lời:** Trường hợp thông báo sau 72 giờ thì phải kèm theo lý do thông báo chậm, muộn [nd13-2023:p17:paragraph:002].

- `[nd13-2023:p17:paragraph:002]` tr. 17:

  > Điều 23. Thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân
  > 
  > 1. Trường hợp phát hiện xảy ra vi phạm quy định bảo vệ dữ liệu cá nhân,
  > Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân thông
  > báo cho Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng
  > công nghệ cao) chậm nhất 72 giờ sau khi xảy ra hành vi vi phạm theo Mẫu số
  > 03 tại Phụ lục của Nghị định này. Trường hợp thông báo sau 72 giờ thì phải
  > kèm theo lý do thông báo chậm, muộn.
  > 
  > 2. Bên Xử lý dữ liệu cá nhân phải thông báo cho Bên Kiểm soát dữ liệu
  > cá nhân một cách nhanh nhất có thể sau khi nhận thấy có sự vi phạm quy định
  > về bảo vệ dữ liệu cá nhân.
  > 
  > 3. Nội dung thông báo vi phạm quy định về bảo vệ dữ liệu cá nhân:
  > 
  > a) Mô tả tính chất của việc vi phạm quy định bảo vệ dữ liệu cá nhân, bao

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q06 · có đáp án · status `answered`
**Hỏi:** Trẻ em từ bao nhiêu tuổi thì việc xử lý dữ liệu cá nhân cần có sự đồng ý của chính trẻ em?

**Đáp án chuẩn (chỉ để chấm):** Từ đủ 7 tuổi trở lên (kèm sự đồng ý của cha, mẹ hoặc người giám hộ).

**Query đã tìm:** ['Trẻ em từ bao nhiêu tuổi thì việc xử lý dữ liệu cá nhân cần có sự đồng ý của chính trẻ em?']
**Agent trả lời:** Việc xử lý dữ liệu cá nhân của trẻ em cần có sự đồng ý của chính trẻ em trong trường hợp trẻ em từ đủ 7 tuổi trở lên [nd13-2023:p16:paragraph:001].

- `[nd13-2023:p16:paragraph:001]` tr. 16:

  > Điều 20. Xử lý dữ liệu cá nhân của trẻ em
  > 
  > 1. Xử lý dữ liệu cá nhân của trẻ em luôn được thực hiện theo nguyên tắc
  > bảo vệ các quyên và vì lợi ích tôt nhật của trẻ em.
  > 
  > 2. Việc xử lý dữ liệu cá nhân của trẻ em phải có sự đồng ý của trẻ em trong
  > trường hợp trẻ em từ đủ 7 tuổi trở lên và có sự đồng ý của cha, mẹ hoặc người
  > giám hộ theo quy định, trừ trường hợp quy định tại Điều 17 Nghị định này. Bên
  > Kiểm soát dữ liệu cá nhân, Bên Xử lý dữ liệu cá nhân, Bên Kiểm soát và xử lý
  > dữ liệu cá nhân, Bên thứ ba phải xác mình tuổi của trẻ em trước khi xử lý dữ
  > liệu cá nhân của trẻ em.
  > 
  > 3. Ngừng xử lý dữ liệu cá nhân của trẻ em, xóa không thể khôi phục hoặc
  > hủy dữ liệu cá nhân của trẻ em trong trường hợp:

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q07 · có đáp án · status `answered`
**Hỏi:** Muốn xử lý dữ liệu cá nhân của người đã chết thì cần ai đồng ý?

**Đáp án chuẩn (chỉ để chấm):** Vợ, chồng hoặc con thành niên của người đó; nếu không có thì cha, mẹ.

**Query đã tìm:** ['Muốn xử lý dữ liệu cá nhân của người đã chết thì cần ai đồng ý?', 'người đã chết Điều 19', 'Điều 19 Xử lý dữ liệu cá nhân của người bị tuyên bố mất tích đã chết']
**Agent trả lời:** Việc xử lý dữ liệu cá nhân của người đã chết phải được sự đồng ý của vợ, chồng hoặc con thành niên của người đó; trường hợp không có những người này thì phải được sự đồng ý của cha, mẹ của người đã chết, trừ trường hợp quy định tại Điều 17 và Điều 18 Nghị định này [nd13-2023:p15:paragraph:004, nd13-2023:p16:paragraph:000]. Trường hợp không có tất cả những người này thì được coi là không có sự đồng ý [nd13-2023:p16:paragraph:000]. [nd13-2023:p15:paragraph:004]

- `[nd13-2023:p15:paragraph:004]` tr. 15:

  > Điều 19. Xử lý dữ liệu cá nhân của người bị tuyên bố mất tích, đã chết
  > 1. Việc xử lý dữ liệu cá nhân liên quan đến dữ liệu cá nhân của người bị
  > tuyên bô mật tích, người đã chêt phải được sự đông ý của vợ, chông hoặc con
  > thành niên của người đó, trường hợp không có những người này thì phải được

- `[nd13-2023:p16:paragraph:000]` tr. 16:

  > sự đồng ý của cha, mẹ của người bị tuyên bố mắt tích, người đã chết, trừ trường
  > hợp quy định tại Điều 17 và Điều 18 Nghị định này.
  > 
  > 2. Trường hợp không có tất cả những người được nêu tại khoản 1 Điều này
  > thì được coi là không có sự đông ý.
  > 
  > .À . ổn ự ~ TA H ˆ + >

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q08 · có đáp án · status `answered`
**Hỏi:** Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải gửi Bộ Công an trong thời hạn bao lâu?

**Đáp án chuẩn (chỉ để chấm):** Trong 60 ngày kể từ ngày tiến hành xử lý dữ liệu cá nhân, theo Mẫu số 04.

**Query đã tìm:** ['Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải gửi Bộ Công an trong thời hạn bao lâu?']
**Agent trả lời:** Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải được gửi đến Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao) trong thời gian 60 ngày kể từ ngày tiến hành xử lý dữ liệu cá nhân [nd13-2023:p19:paragraph:002].

- `[nd13-2023:p19:paragraph:002]` tr. 19:

  > 3. Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân quy định tại khoản 1 và
  > khoản 2 Điều này được xác lập bằng văn bản có giá trị pháp lý của Bên Kiểm
  > soát dữ liệu cá nhân, Bên Kiếm soát và xử lý dữ liệu cá nhân hoặc Bên Xử lý
  > dữ liệu cá nhân.
  > 
  > 4. Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải luôn có sẵn để phục
  > vụ hoạt động kiếm tra, đánh giá của Bộ Công an và gửi Bộ Công an (Cục An
  > ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao) 01 bản chính theo
  > Mẫu số 04 tại Phụ lục của Nghị định này trong thời gian 60 ngày kể từ ngày tiền
  > hành xử lý dữ liệu cá nhân.
  > 
  > 5. Bộ Công an (Cục An ninh mạng và phòng, chống tội phạm sử dụng công
  > nghệ cao) đánh giá, yêu câu Bên Kiêm soát dữ liệu cá nhân, Bên Kiêm soát và

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q09 · có đáp án · status `answered`
**Hỏi:** Bộ Công an kiểm tra việc chuyển dữ liệu cá nhân ra nước ngoài với tần suất nào?

**Đáp án chuẩn (chỉ để chấm):** 01 lần/năm, trừ khi phát hiện vi phạm hoặc để lộ, mất dữ liệu.

**Query đã tìm:** ['Bộ Công an kiểm tra việc chuyển dữ liệu cá nhân ra nước ngoài với tần suất nào?']
**Agent trả lời:** Căn cứ tình hình cụ thể, Bộ Công an quyết định việc kiểm tra chuyển dữ liệu cá nhân ra nước ngoài 01 lần/năm, trừ trường hợp phát hiện hành vi vi phạm quy định của pháp luật về bảo vệ dữ liệu cá nhân tại Nghị định này hoặc để xảy ra sự cố lộ, mất dữ liệu cá nhân của công dân Việt Nam. [nd13-2023:p21:paragraph:002]

- `[nd13-2023:p21:paragraph:002]` tr. 21:

  > 7. Căn cứ tình hình cụ thể, Bộ Công an quyết định việc kiểm tra chuyển
  > dữ liệu cá nhân ra nước ngoài 01 lằn/năm, trừ trường hợp phát hiện hành vi vi
  > phạm quy định của pháp luật về bảo vệ dữ liệu cá nhân tại Nghị định này hoặc
  > để xảy ra sự có lộ, mất dữ liệu cá nhân của công dân Việt Nam.
  > 
  > 8. Bộ Công an quyết định yêu cầu Bên chuyến dữ liệu ra nước ngoài ngừng
  > chuyên dữ liệu cá nhân ra nước ngoài trong trường hợp:
  > 
  > a) Khi phát hiện dữ liệu cá nhân được chuyển được sử dụng vào hoạt động
  > vi phạm lợi ích, an ninh quốc gia của nước Cộng hòa xã hội chủ nghĩa Việt Nam;
  > 
  > b)Bên chuyên dữ liệu ra nước ngoài không chấp hành quy định tại khoản 5,
  > khoản 6 Điều này;
  > c) Để xảy ra sự có lộ, mất dữ liệu cá nhân của công dân Việt Nam.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q10 · có đáp án · status `answered`
**Hỏi:** Nghị định 13/2023 có hiệu lực thi hành từ ngày nào?

**Đáp án chuẩn (chỉ để chấm):** Từ ngày 01 tháng 7 năm 2023.

**Query đã tìm:** ['Nghị định 13/2023 có hiệu lực thi hành từ ngày nào?']
**Agent trả lời:** Nghị định 13/2023 có hiệu lực thi hành từ ngày 01 tháng 7 năm 2023 [nd13-2023:p27:paragraph:004].

- `[nd13-2023:p27:paragraph:004]` tr. 27:

  > Chương IV
  > ĐIỀU KHOẢN THỊ HÀNH
  > 
  > Điều 43. Hiệu lực thi hành
  > 
  > 1. Nghị định này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2023.
  > 
  > 2. Các doanh nghiệp siêu nhỏ, doanh nghiệp nhỏ, doanh nghiệp vừa, doanh
  > nghiệp khởi nghiệp được quyền lựa chọn miễn trừ quy định về chỉ định cá nhân
  > 
  > và bộ phận bảo vệ dữ liệu cá nhân trong thời gian 02 năm đầu kết từ khi thành
  > lập doanh nghiệp.
  > 
  > 3. Các doanh nghiệp siêu nhỏ, doanh nghiệp nhỏ, doanh nghiệp vừa, doanh
  > nghiệp khởi nghiệp trực tiệp kinh doanh hoạt động xử lý dữ liệu cá nhân không
  > áp dụng quy định tại khoản 2 Điều này.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q11 · có đáp án · status `answered`
**Hỏi:** Doanh nghiệp khởi nghiệp được miễn chỉ định cá nhân, bộ phận bảo vệ dữ liệu cá nhân trong bao lâu?

**Đáp án chuẩn (chỉ để chấm):** Trong 02 năm đầu kể từ khi thành lập, trừ doanh nghiệp trực tiếp kinh doanh hoạt động xử lý dữ liệu cá nhân.

**Query đã tìm:** ['Doanh nghiệp khởi nghiệp được miễn chỉ định cá nhân, bộ phận bảo vệ dữ liệu cá nhân trong bao lâu?']
**Agent trả lời:** Doanh nghiệp khởi nghiệp được quyền lựa chọn miễn trừ quy định về chỉ định cá nhân và bộ phận bảo vệ dữ liệu cá nhân trong thời gian 02 năm đầu kể từ khi thành lập doanh nghiệp (trừ trường hợp trực tiếp kinh doanh hoạt động xử lý dữ liệu cá nhân) [nd13-2023:p27:paragraph:004].

- `[nd13-2023:p27:paragraph:004]` tr. 27:

  > Chương IV
  > ĐIỀU KHOẢN THỊ HÀNH
  > 
  > Điều 43. Hiệu lực thi hành
  > 
  > 1. Nghị định này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2023.
  > 
  > 2. Các doanh nghiệp siêu nhỏ, doanh nghiệp nhỏ, doanh nghiệp vừa, doanh
  > nghiệp khởi nghiệp được quyền lựa chọn miễn trừ quy định về chỉ định cá nhân
  > 
  > và bộ phận bảo vệ dữ liệu cá nhân trong thời gian 02 năm đầu kết từ khi thành
  > lập doanh nghiệp.
  > 
  > 3. Các doanh nghiệp siêu nhỏ, doanh nghiệp nhỏ, doanh nghiệp vừa, doanh
  > nghiệp khởi nghiệp trực tiệp kinh doanh hoạt động xử lý dữ liệu cá nhân không
  > áp dụng quy định tại khoản 2 Điều này.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q12 · có đáp án · status `answered`
**Hỏi:** Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là cơ quan nào?

**Đáp án chuẩn (chỉ để chấm):** Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao - Bộ Công an.

**Query đã tìm:** ['Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là cơ quan nào?']
**Agent trả lời:** Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là Cục An ninh mạng và phòng, chống tội phạm sử dụng công nghệ cao - Bộ Công an [nd13-2023:p23:paragraph:000].

- `[nd13-2023:p23:paragraph:000]` tr. 23:

  > Điều 29. Cơ quan chuyên trách bảo vệ dữ liệu cá nhân và Công thông
  > tin quốc gia về bảo vệ dữ liệu cá nhân
  > 
  > 1. Cơ quan chuyên trách bảo vệ dữ liệu cá nhân là Cục An ninh mạng và
  > phòng, chống tội phạm sử dụng công nghệ cao - Bộ Công an, có trách nhiệm
  > giúp Bộ Công an thực hiện quản lý nhà nước về bảo vệ dữ liệu cá nhân.
  > 
  > 2. Cổng thông tin quốc gia về bảo vệ dữ liệu cá nhân:
  > 
  > a) Cung cấp thông tin về chủ trương; đường lồi, chính-sách của Đảng, pháp
  > luật của Nhà nước về bảo vệ dữ liệu cá nhân;
  > 
  > b) Tuyên truyền, phổ biến chính sách, pháp luật về bảo vệ dữ liệu cá nhân;
  > 
  > c) Cập nhật thông tin, tình hình bảo vệ dữ liệu cá nhân;
  > 
  > d) Tiếp nhận thông tin, hồ sơ, dữ liệu về hoạt động bảo vệ dữ liệu cá nhân
  > qua không gian mạng;

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q13 · có đáp án · status `answered`
**Hỏi:** Trong phần quy định trách nhiệm (Chương III), Bên Kiểm soát dữ liệu cá nhân phải ghi lại và lưu trữ gì?

**Đáp án chuẩn (chỉ để chấm):** Nhật ký hệ thống quá trình xử lý dữ liệu cá nhân.

**Query đã tìm:** ['Trong phần quy định trách nhiệm (Chương III), Bên Kiểm soát dữ liệu cá nhân phải ghi lại và lưu trữ gì?']
**Agent trả lời:** Theo Điều 38 Nghị định 13/2023/NĐ-CP, Bên Kiểm soát dữ liệu cá nhân phải ghi lại và lưu trữ nhật ký hệ thống quá trình xử lý dữ liệu cá nhân [nd13-2023:p26:paragraph:001].

- `[nd13-2023:p26:paragraph:001]` tr. 26:

  > Điều 38. Trách nhiệm của Bên Kiếm soát dữ liệu cá nhân
  > 
  > 1. Thực hiện các biện pháp tổ chức và kỹ thuật cùng các biện pháp an toàn,
  > bảo mật phù hợp đề chứng minh các hoạt động xử lý dữ liệu đã được thực hiện
  > 
  > theo quy định của pháp luật về bảo vệ dữ liệu cá nhân, rà soát và cập nhật các
  > biện pháp này khi cân thiêt.
  > 
  > 2. Ghi lại và lưu trữ nhật ký hệ thống quá trình xử lý dữ liệu cá nhân.
  > 
  > 3. Thông báo hành vi vi phạm quy định về bảo vệ dữ liệu cá nhân theo
  > quy định tại Điêu 23 Nghị định này.
  > 
  > 4. Lựa chọn Bên Xử lý dữ liệu cá nhân phù hợp với nhiệm vụ rõ ràng và
  > chỉ làm việc với Bên Xử lý dữ liệu cá nhân có các biện pháp bảo vệ phù hợp.
  > 
  > 5. Bảo đảm các quyền của chủ thể dữ liệu theo quy định tại Điều 9 Nghị
  > định này.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q14 · có đáp án · status `answered`
**Hỏi:** Trong biểu mẫu phụ lục, Phiếu yêu cầu cung cấp dữ liệu cá nhân dành cho cá nhân cho phép những phương thức nhận dữ liệu nào?

**Đáp án chuẩn (chỉ để chấm):** Nhận tại nơi yêu cầu, qua bưu điện, qua mạng điện tử, hoặc hình thức khác.

**Query đã tìm:** ['Trong biểu mẫu phụ lục, Phiếu yêu cầu cung cấp dữ liệu cá nhân dành cho cá nhân cho phép những phương thức nhận dữ liệu nào?']
**Agent trả lời:** Trong Phiếu yêu cầu cung cấp dữ liệu cá nhân (dành cho cá nhân), các phương thức nhận dữ liệu cá nhân bao gồm:
- Nhận tại nơi yêu cầu cung cấp [nd13-2023:p30:paragraph:000]
- Nhận qua bưu điện (ghi rõ địa chỉ nhận) [nd13-2023:p30:paragraph:001]
- Nhận qua mạng điện tử (ghi rõ địa chỉ nhận) [nd13-2023:p30:paragraph:001]
- Hình thức khác (ghi rõ) [nd13-2023:p30:paragraph:001]

- `[nd13-2023:p30:paragraph:000]` tr. 30:

  > Ì ĩ : Ñ Mẫu số 01
  > CỘNG HÒA XÃ HỘI CHỦ NGHĨA VIỆT NAM
  > Độc lập - Tự do - Hạnh phúc
  > .„, Hgửy … tháng … năm …
  > PHIẾU VÊU CÀU CUNG CÁP DỮ LIỆU CÁ NHÂN
  > (Dành cho cá nhân)
  > Kính gửi: …eeeeeeeeeueeee
  > 
  > 1. Họ, tên cá nhân yêu cầu cung se dữ liệu cá nhân: …
  > 
  > 2. Người đại diện/Ng: gười giám n hột: HN
  > 
  > 3. SỐ CMTND/Thẻ căn cước công dân/Hộ chiếu…
  > 
  > Lo km
  > 4. Nơi cư trú:
  > 
  > 5. Số điện thoại. … :Fax …Á… :E-mail:… `
  > 
  > 6. Dữ liệu cá nhân yêu cầu cung Lo... HN
  > 
  > 7. Mục đích yêu cầu cung cấp: no NI
  > 
  > 8. Yêu cầu cung cấp dữ liệu cá nhân lần thứ:
  > 
  > a) Lần đầu b) Khác:… (ghi rõ số lần đã yêu cầu cung cấp
  > thông tin có nội dung nêu trên)
  > 
  > 9, Số lượng bản”:…
  > 
  > 10. Phương thức nhận dữ liệu cá nhân:
  > 
  > [L1 Nhận tại nơi yêu cầu cung cấp

- `[nd13-2023:p30:paragraph:001]` tr. 30:

  > [.] Nhận qua bưu điện (ghi rõ địa chỉ nhận):…
  > mẽ 2/0200 0 3 HG
  > L ] Nhận qua mạng điện tử (ghi rõ địa chỉ nhận):…
  > [1 Hình thức khác (ghi rÕ):…neneeneneeneeneeneeeeneeeeeene
  > 11. Văn bản kèm theo (trong trường hợp có điều kiện):…
  > 
  > NGƯỜI YÊU CẢU
  > (Kỷ, ghi rõ họ tên)
  > 
  > † Theo quy định của Bộ luật Dân sự về người đại diện, người giám hộ đối với người yêu cầu cung cấp
  > thông tin là người chưa thành niên, người hạn chế năng lực hành vi dân sự, người mắt năng lực hành vi dân sự,
  > người có khó khăn trong nhận thức và làm chủ hành vi..
  > 
  > 2 Ghi nơi cư trú của người đại điện/người giám hộ.
  > 
  > 3 Ghi số điện thoại, fax, email của người đại diện/giám hộ.
  > 
  > “ Ghi rõ tên chủ thể dữ liệu và các thông tin liên quan cần cung cấp.
  > 
  > 5 In, sao, chụp hoặc ñle dữ liệu.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q15 · có đáp án · status `answered`
**Hỏi:** Trong trường hợp nào Bên Kiểm soát dữ liệu được từ chối cung cấp dữ liệu cá nhân?

**Đáp án chuẩn (chỉ để chấm):** Khi gây tổn hại quốc phòng, an ninh, trật tự; ảnh hưởng an toàn, sức khỏe người khác; hoặc chủ thể không đồng ý cung cấp/ủy quyền.

**Query đã tìm:** ['Trong trường hợp nào Bên Kiểm soát dữ liệu được từ chối cung cấp dữ liệu cá nhân?']
**Agent trả lời:** Bên Kiểm soát dữ liệu cá nhân (và Bên Kiểm soát và xử lý dữ liệu cá nhân) không cung cấp dữ liệu cá nhân trong các trường hợp sau:
a) Gây tổn hại tới quốc phòng, an ninh quốc gia, trật tự an toàn xã hội [nd13-2023:p11:paragraph:002].
b) Việc cung cấp dữ liệu cá nhân của chủ thể dữ liệu có thể ảnh hưởng tới sự an toàn, sức khỏe thể chất hoặc tinh thần của người khác [nd13-2023:p11:paragraph:002].
c) Chủ thể dữ liệu không đồng ý cung cấp, cho phép đại diện hoặc ủy quyền nhận dữ liệu cá nhân [nd13-2023:p11:paragraph:002].

- `[nd13-2023:p11:paragraph:002]` tr. 11:

  > 3. Việc cung cấp dữ liệu cá nhân của chủ thể dữ liệu được Bên Kiểm soát dữ
  > liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân thực hiện trong 72 giờ sau
  > khi có yêu cầu của chủ thể dữ liệu, trừ trường hợp luật có quy định khác.
  > 
  > 4. Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân
  > không cung cấp dữ liệu cá nhân trong trường hợp:
  > 
  > a) Gây tồn hại tới quốc phòng, an ninh quốc gia, trật tự an toàn xã hội;
  > 
  > b) Việc cung cấp dữ liệu cá nhân của chủ thể dữ liệu có thể ảnh hưởng tới
  > sự an toàn, sức khỏe thê chât hoặc tình thân của người khác;
  > 
  > c) Chủ thể dữ liệu không đồng ý cung cấp, cho phép đại diện hoặc ủy
  > quyên nhận dữ liệu cá nhân.
  > 
  > 5. Hình thức yêu cầu cung cấp dữ liệu cá nhân:

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q16 · có đáp án · status `answered`
**Hỏi:** Có được mua bán dữ liệu cá nhân không?

**Đáp án chuẩn (chỉ để chấm):** Không được mua, bán dưới mọi hình thức, trừ trường hợp luật có quy định khác.

**Query đã tìm:** ['Có được mua bán dữ liệu cá nhân không?']
**Agent trả lời:** Dữ liệu cá nhân không được mua, bán dưới mọi hình thức, trừ trường hợp luật có quy định khác [nd13-2023:p04:paragraph:003]. Bên cạnh đó, việc mua, bán dữ liệu cá nhân không có sự đồng ý của chủ thể dữ liệu là vi phạm pháp luật [nd13-2023:p17:paragraph:001].

- `[nd13-2023:p04:paragraph:003]` tr. 4:

  > Điều 3. Nguyên tắc bảo vệ dữ liệu cá nhân
  > 1. Dữ liệu cá nhân được xử lý theo quy định của pháp luật.
  > 
  > 2. Chủ thể dữ liệu được biết về hoạt động liên quan tới xử lý dữ liệu cá
  > nhân của mình, trừ trường hợp luật có quy định khác.
  > 
  > 3. Dữ liệu cá nhân chỉ được xử lý đúng với mục đích đã được Bên Kiếm
  > soát dữ liệu cá nhân, Bên Xử lý dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ
  > liệu cá nhân, Bên thứ ba đăng ký, tuyên bố về xử lý dữ liệu cá nhân.
  > 
  > 4. Dữ liệu cá nhân thu thập phải phù hợp và giới hạn trong phạm vi, mục
  > đích cần xử lý. Dữ liệu cá nhân không được mua, bán dưới mọi hình thức, trừ
  > trường hợp luật có quy định khác.
  > 
  > 5. Dữ liệu cá nhân được cập nhật, bổ sung phù hợp với mục đích xử lý.

- `[nd13-2023:p17:paragraph:001]` tr. 17:

  > Điều 22. Thu thập, chuyễn giao, mua, bán trái phép dữ Hiệu cá nhân
  > 
  > 1. Tổ chức, cá nhân có liên quan tới xử lý dữ liệu cá nhân phải áp dụng
  > các biện pháp bảo vệ dữ liệu cá nhân đề ngăn chặn tình trạng thu thập dữ liệu
  > cá nhân trái phép từ hệ thống, trang thiết bị dịch vụ của mình.
  > 
  > 2. Việc thiết lập các hệ thống phần mềm, biện pháp kỹ thuật hoặc tổ chức
  > các hoạt động thu thập, chuyển giao, mua, bán dữ liệu cá nhân không có sự
  > đồng ý của chủ thể dữ liệu là vi phạm pháp luật.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q17 · có đáp án · status `answered`
**Hỏi:** Bộ nào phối hợp với Bộ Công an xây dựng Tiêu chuẩn bảo vệ dữ liệu cá nhân?

**Đáp án chuẩn (chỉ để chấm):** Bộ Khoa học và Công nghệ.

**Query đã tìm:** ['Bộ nào phối hợp với Bộ Công an xây dựng Tiêu chuẩn bảo vệ dữ liệu cá nhân?']
**Agent trả lời:** Bộ Khoa học và Công nghệ là cơ quan phối hợp với Bộ Công an trong việc xây dựng Tiêu chuẩn bảo vệ dữ liệu cá nhân [nd13-2023:p25:paragraph:003].

- `[nd13-2023:p25:paragraph:003]` tr. 25:

  > Điều 35. Trách nhiệm của Bộ Khoa học và Công nghệ
  > 
  > 1. Phối hợp với Bộ Công an trong xây dựng Tiêu chuẩn bảo vệ dữ liệu cá
  > nhân và các khuyên nghị áp dụng Tiêu chuân bảo vệ dữ liệu cá nhân.
  > 
  > 2. Nghiên cứu, trao đổi Bộ Công an về các biện pháp bảo vệ dữ liệu cá
  > nhân theo kịp sự phát triển của khoa học, công nghệ.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q18 · có đáp án · status `answered`
**Hỏi:** Sau khi chủ thể yêu cầu xóa dữ liệu, bên kiểm soát phải xóa trong thời hạn bao lâu?

**Đáp án chuẩn (chỉ để chấm):** Trong 72 giờ sau khi có yêu cầu, trừ trường hợp pháp luật có quy định khác.

**Query đã tìm:** ['Sau khi chủ thể yêu cầu xóa dữ liệu, bên kiểm soát phải xóa trong thời hạn bao lâu?']
**Agent trả lời:** Việc xóa dữ liệu được thực hiện trong 72 giờ sau khi có yêu cầu của chủ thể dữ liệu với toàn bộ dữ liệu cá nhân mà Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm soát và xử lý dữ liệu cá nhân thu thập được, trừ trường hợp pháp luật có quy định khác [nd13-2023:p14:paragraph:001].

- `[nd13-2023:p14:paragraph:001]` tr. 14:

  > e) Ứng phó với tình huống khẩn cấp đe dọa đến tính mạng, sức khỏe hoặc
  > sự an toàn của chủ thê dữ liệu hoặc cá nhân khác.
  > 
  > 3. Trường hợp doanh nghiệp chia, tách, sáp nhập, hợp nhất, giải thể thì dữ
  > liệu cá nhân được chuyển giao theo quy định của pháp luật.
  > 
  > 4. Trường hợp chia, tách, sáp nhập cơ quan, tổ chức, đơn vị hành chính và
  > tô chức lại, chuyên đôi hình thức sở hữu doanh nghiệp nhà nước thì dữ liệu cá
  > nhân được chuyển giao theo quy định của pháp luật.
  > 
  > 5. Việc xóa dữ liệu được thực hiện trong 72 giờ sau khi có yêu cầu của
  > chủ thể dữ liệu với toàn bộ dữ liệu cá nhân mà Bên Kiểm soát dữ liệu cá nhân,
  > Bên Kiểm soát và xử lý dữ liệu cá nhân thu thập được, trừ trường hợp pháp luật
  > có quy định khác.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q19 · có đáp án · status `answered`
**Hỏi:** Có trường hợp nào chủ thể dữ liệu đề nghị xóa nhưng dữ liệu không bị xóa không?

**Đáp án chuẩn (chỉ để chấm):** Có, ví dụ pháp luật không cho phép xóa, dữ liệu do cơ quan nhà nước xử lý, dữ liệu đã công khai, phục vụ nghiên cứu/thống kê, tình trạng khẩn cấp.

**Query đã tìm:** ['Có trường hợp nào chủ thể dữ liệu đề nghị xóa nhưng dữ liệu không bị xóa không?']
**Agent trả lời:** Có, việc xóa dữ liệu sẽ không áp dụng khi có đề nghị của chủ thể dữ liệu trong các trường hợp sau:
a) Pháp luật quy định không cho phép xóa dữ liệu;
b) Dữ liệu cá nhân được xử lý bởi cơ quan nhà nước có thẩm quyền với mục đích phục vụ hoạt động của cơ quan nhà nước theo quy định của pháp luật;
c) Dữ liệu cá nhân đã được công khai theo quy định của pháp luật;
d) Dữ liệu cá nhân được xử lý nhằm phục vụ yêu cầu pháp lý, nghiên cứu khoa học, thống kê theo quy định của pháp luật;
đ) Trong trường hợp tình trạng khẩn cấp về quốc phòng, an ninh quốc gia, trật tự an toàn xã hội, thảm họa lớn, dịch bệnh nguy hiểm; khi có nguy cơ đe dọa an ninh, quốc phòng nhưng chưa đến mức ban bố tình trạng khẩn cấp; phòng, chống bạo loạn, khủng bố, phòng, chống tội phạm và vi phạm pháp luật. [nd13-2023:p13:paragraph:003, nd13-2023:p14:paragraph:000] [nd13-2023:p13:paragraph:003] [nd13-2023:p14:paragraph:000]

- `[nd13-2023:p13:paragraph:003]` tr. 13:

  > Điều 16. Lưu trữ, xóa, hủy dữ liệu cá nhân
  > 
  > 1. Chủ thể dữ liệu được yêu cầu Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm
  > soát và xử lý dữ liệu cá nhân xóa dữ liệu cá nhân của mình trong các trường
  > hợp sau:
  > 
  > a) Nhận thấy không còn cần thiết cho mục đích thu thập đã đồng ý và chấp
  > nhận các thiệt hại có thê xảy ra khi yêu câu xóa dữ liệu;
  > 
  > b) Rút lại sự đồng ý;
  > 
  > e) Phản đối việc xử lý dữ liệu và Bên Kiểm soát dữ liệu cá nhân, Bên Kiểm
  > soát và xử lý dữ liệu cá nhân không có lý do chính đáng đề tiếp tục xử lý;
  > 
  > d) Dữ liệu cá nhân được xử lý không đúng với mục đích đã đồng ý hoặc
  > việc xử lý dữ liệu cá nhân là vi phạm quy định của pháp luật;
  > 
  > đ) Dữ liệu cá nhân phải xóa theo quy định của pháp luật.
  > 
  > 2. Việc xóa dữ liệu sẽ không áp dụng khi có đề nghị của chủ thể dữ liệu
  > trong các trường hợp:

- `[nd13-2023:p14:paragraph:000]` tr. 14:

  > a) Pháp luật quy định không cho phép xóa dữ liệu;
  > 
  > b) Dữ liệu cá nhân được xử lý bởi cơ quan nhà nước có thẩm quyền với
  > mục đích phục vụ hoạt động của cơ quan nhà nước theo quy định của pháp luật;
  > 
  > c) Dữ liệu cá nhân đã được công khai theo quy định của pháp luật;
  > 
  > d) Dữ liệu cá nhân được xử lý nhằm phục vụ yêu cầu pháp lý, nghiên cứu
  > khoa học, thống kê theo quy định của pháp luật;
  > 
  > đ) Trong trường hợp tình trạng khẩn cấp về quốc phòng, an ninh quốc gia,
  > trật tự an toàn xã hội, thảm họa lớn, dịch bệnh nguy hiểm; khi có nguy cơ đc
  > dọa an ninh, quốc phòng nhưng chưa đến mức ban bố tình trạng khẩn cấp;
  > phòng, chống bạo loạn, khủng bố, phòng, chống tội phạm và vi phạm pháp luật;

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q20 · có đáp án · status `answered`
**Hỏi:** Trong phần quy định trách nhiệm (Chương III), Bên Xử lý dữ liệu cá nhân phải làm gì với dữ liệu sau khi kết thúc xử lý?

**Đáp án chuẩn (chỉ để chấm):** Xóa, trả lại toàn bộ dữ liệu cá nhân cho Bên Kiểm soát dữ liệu cá nhân.

**Query đã tìm:** ['Trong phần quy định trách nhiệm (Chương III), Bên Xử lý dữ liệu cá nhân phải làm gì với dữ liệu sau khi kết thúc xử lý?']
**Agent trả lời:** Theo Điều 39 (Chương III) về trách nhiệm của Bên Xử lý dữ liệu cá nhân, sau khi kết thúc xử lý dữ liệu, Bên Xử lý dữ liệu cá nhân phải xóa hoặc trả lại toàn bộ dữ liệu cá nhân cho Bên Kiểm soát dữ liệu cá nhân [nd13-2023:p27:paragraph:000].

- `[nd13-2023:p27:paragraph:000]` tr. 27:

  > 4. Bên Xử lý dữ liệu cá nhân chịu trách nhiệm trước chủ thể dữ liệu về các
  > thiệt hại do quá trình xử lý dữ liệu cá nhân gây ra.
  > 
  > 5. Xóa, trả lại toàn bộ dữ liệu cá nhân cho Bên Kiểm soát dữ liệu cá nhân
  > sau khi kết thúc xử lý dữ liệu.
  > 
  > 6. Phối hợp với Bộ Công an, cơ quan nhà nước có thẩm quyền trong bảo
  > vệ dữ liệu cá nhân, cung cập thông tĩn phục vụ điều tra, xử lý hành vi vi phạm
  > quy định của pháp luật vê bảo vệ dữ liệu cá nhân.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q21 · có đáp án · status `answered`
**Hỏi:** Theo biểu mẫu phụ lục, thông báo gửi hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải khai thông tin nhân sự nào?

**Đáp án chuẩn (chỉ để chấm):** Nhân sự chịu trách nhiệm bảo vệ dữ liệu cá nhân (họ tên, số điện thoại liên lạc).

**Query đã tìm:** ['Theo biểu mẫu phụ lục, thông báo gửi hồ sơ đánh giá tác động xử lý dữ liệu cá nhân phải khai thông tin nhân sự nào?', 'Mẫu số 04 thông báo gửi hồ sơ đánh giá tác động xử lý dữ liệu cá nhân', 'Mẫu số 04 Thông báo gửi hồ sơ đánh giá tác động xử lý dữ liệu cá nhân nhân sự']
**Agent trả lời:** Theo Mẫu số 04 (Thông báo gửi hồ sơ đánh giá tác động xử lý dữ liệu cá nhân), thông tin nhân sự cần khai là:
- Nhân sự chịu trách nhiệm bảo vệ dữ liệu cá nhân [nd13-2023:p36:paragraph:001].
- Các thông tin cụ thể gồm: Họ và tên, số điện thoại liên lạc (cố định và di động), và email [nd13-2023:p36:paragraph:001].

- `[nd13-2023:p36:paragraph:001]` tr. 36:

  > - Điện thoại: … MWebsite…202./7//2//. 6.5
  > - Nhân sự chịu trách nhiệm bảo vệ dữ liệu cá nhân:…
  > Họ và tên:…11010iennen nen nen nen nen ni nen nen ni nnn nh
  > l@ ii.
  > Số điện thoại liên lạc (cố định và di động): …„
  > Email:…-111111 v11 n ni nen ni nnn k tt nh ke nen kE kh k9 ni tk n nh
  > 
  > 2. Mô tả tóm tắt thay đổi nội dung hồ sơ
  > - Nội dung thay đổi:…nnnnnnnnnnnnnnnnrnnnnnnnnn nen nen ng
  > 1
  > 
  > 3. Tài liệu kèm theo
  > 
  > 1 Tên hồ sơ: Hồ sơ đánh giá tác động xử lý dữ liệu cá nhân hoặc Hồ sơ đánh giá tác động chuyên dữ liệu cá
  > nhân ra nước ngoài.
  > 2 Tên tổ chức, doanh nghiệp.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## q22 · có đáp án · status `answered`
**Hỏi:** Cản trở hoạt động bảo vệ dữ liệu cá nhân của cơ quan có thẩm quyền có bị cấm không?

**Đáp án chuẩn (chỉ để chấm):** Có, đây là hành vi bị nghiêm cấm (Điều 8).

**Query đã tìm:** ['Cản trở hoạt động bảo vệ dữ liệu cá nhân của cơ quan có thẩm quyền có bị cấm không?']
**Agent trả lời:** Có, hành vi cản trở hoạt động bảo vệ dữ liệu cá nhân của cơ quan có thẩm quyền là hành vi bị nghiêm cấm theo quy định tại khoản 4 Điều 8 Nghị định 13/2023/NĐ-CP [nd13-2023:p06:paragraph:003].

- `[nd13-2023:p06:paragraph:003]` tr. 6:

  > Điều 8. Hành vi bị nghiêm cấm
  > 
  > 1. Xử lý dữ liệu cá nhân trái với quy định của pháp luật về bảo vệ dữ liệu
  > cá nhân.
  > 
  > 2. Xử lý dữ liệu cá nhân để tạo ra thông tin, dữ liệu nhằm chống lại Nhà
  > nước Cộng hòa xã hội chủ nghĩa Việt Nam.
  > 
  > 3. Xử lý dữ liệu cá nhân để tạo ra thông tin, dữ liệu gây ảnh hưởng tới an
  > ninh quốc gia, trật tự an toàn xã hội, quyên và lợi ích hợp pháp của tổ chức, cá
  > nhân khác.
  > 
  > 4. Cản trở hoạt động bảo vệ dữ liệu cá nhân của cơ quan có thẩm quyền.
  > 
  > 5. Lợi dụng hoạt động bảo vệ dữ liệu cá nhân để vi phạm pháp luật.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## u01 · THIẾU EVIDENCE · status `abstain`
**Hỏi:** Mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân là bao nhiêu?

**Lý do thiếu:** Grep toàn bộ 39 trang OCR: 'phạt' chỉ xuất hiện 1 lần (Điều 4, tr. 5: 'xử phạt vi phạm hành chính... theo quy định'), không có mức tiền; 'triệu', 'doanh thu', '%' = 0 kết quả. Trả lời đúng = nói Nghị định không quy định mức phạt; có thể dẫn Điều 4 nhưng không được nêu con số.

**Query đã tìm:** ['Mức phạt tiền tối đa đối với hành vi vi phạm quy định bảo vệ dữ liệu cá nhân là bao nhiêu?', 'phạt tiền mức tối đa vi phạm quy định bảo vệ dữ liệu cá nhân', 'mức phạt tiền tối đa hành vi vi phạm bảo vệ dữ liệu cá nhân']
**Agent trả lời:** Không đủ bằng chứng để trả lời.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---

## u02 · THIẾU EVIDENCE · status `answered`
**Hỏi:** Bên Kiểm soát dữ liệu được lưu trữ dữ liệu cá nhân của khách hàng tối đa bao nhiêu năm?

**Lý do thiếu:** Grep 'lưu trữ' (8 kết quả): chỉ có nguyên tắc 'chỉ được lưu trữ trong khoảng thời gian phù hợp với mục đích xử lý' (Điều 3 khoản 7, tr. 5) và Điều 16, không có số năm. Trả lời đúng = nói không quy định số năm cụ thể; không được nêu con số.

**Query đã tìm:** ['Bên Kiểm soát dữ liệu được lưu trữ dữ liệu cá nhân của khách hàng tối đa bao nhiêu năm?', 'thời gian lưu trữ dữ liệu cá nhân', 'thời gian lưu trữ dữ liệu cá nhân tối đa']
**Agent trả lời:** Dữ liệu cá nhân được lưu trữ trong khoảng thời gian phù hợp với mục đích xử lý dữ liệu, trừ trường hợp pháp luật có quy định khác [nd13-2023:p05:paragraph:000]. Nghị định không quy định một số năm tối đa cụ thể.

- `[nd13-2023:p05:paragraph:000]` tr. 5:

  > 6. Dữ liệu cá nhân được áp dụng các biện pháp bảo vệ, bảo mật trong quá
  > trình xử lý, bao gồm cả việc bảo vệ trước các hành vi vi phạm quy định về bảo
  > vệ dữ liệu cá nhân và phòng, chống sự mất mát, phá hủy hoặc thiệt hại do sự
  > cố, sử dụng các biện pháp kỹ thuật.
  > 
  > 7. Dữ liệu cá nhân chỉ được lưu trữ trong khoảng thời gian phù hợp với
  > mục đích xử lý dữ liệu, trừ trường hợp pháp luật có quy định khác.
  > 
  > 8. Bên Kiểm soát dữ liệu, Bên Kiểm soát và xử lý dữ liệu cá nhân phải
  > chịu trách nhiệm tuân thủ các nguyên tắc xử lý dữ liệu được quy định từ khoản 1
  > tới khoản 7 Điều này và chứng minh sự tuân thủ của mình với các nguyên tắc
  > xử lý dữ liệu đó.

Nhãn: answer_grade=__ · citation_support=__ · abstention_correct=__ · lý do: 

---
