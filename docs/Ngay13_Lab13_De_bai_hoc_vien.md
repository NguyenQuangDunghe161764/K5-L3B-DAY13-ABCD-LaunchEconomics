# **Ngày 13 · Lab 13 — Định giá agent và lập kế hoạch pilot** 

Đề bài cho học viên · L3A, L3B · 14:00–18:00 

## **Bối cảnh và sản phẩm phải nộp** 

Cuối buổi, mỗi nhóm nộp một bộ hồ sơ launch v0 cho trợ lý hoàn phí của LogiX-VN và bảo vệ nó trước một nhóm khác đóng vai hội đồng Gate 2a. 

LogiX-VN có 12 depot, khoảng 40 nhân viên chăm sóc khách hàng và nhận khoảng 45.000 yêu cầu hoàn phí mỗi tháng, tức 1.500 yêu cầu mỗi ngày. Trợ lý hoàn phí vừa chạy thử hai tuần ở 6 depot. Giám đốc vận hành muốn mở pilot. Nhóm bạn được giao một mẫu ngẫu nhiên 1.200 yêu cầu của đợt chạy thử để trả lời: có đáng chạy không, nhân viên có dùng không, khi hỏng thì sao, và pilot phải thiết kế thế nào để ra được quyết định. 

Toàn bộ dữ liệu là giả lập. Lab không cần khoá API. 

### **File được phát** 

|**File**|**Nội dung**|
|---|---|
|logix_runs.csv|1.624 lần chạy của agent, mỗi dòng một lần chạy:run_id,request_id,trace_id,attempt,<br>tokens_in,tokens_out,tool_calls,status(okhoặcloi)|
|logix_requests.csv|1.200 yêu cầu, mỗi dòng một yêu cầu:depot,staff_id,loai,so_tien_vnd,so_lan_chay,<br>ket_qua,duoc_xem_lai,quyet_dinh_xem_lai,phut_xem_lai_simulated,<br>phut_lam_lai_simulated,dong_trong_24h,mo_lai_trong_7_ngay|
|lab13_starter.py|Khung code có sẵn ba phép thử đáp án biết trước|



Giá trị của một số cột: 

- loai : noi_dia (nội địa thường), hang_nang (hàng nặng, cồng kềnh), quoc_te (quốc tế), doi_tac (khách đối tác có điều khoản riêng). 

- ket_qua : thanh_cong (đã đóng, không mở lại trong 7 ngày, không sai tiền), lam_lai (trả lời sai, nhân viên phải làm lại), chuyen_nhan_vien (chạy hết 3 lần vẫn lỗi, chuyển cho nhân viên). 

- quyet_dinh_xem_lai : giu , sua , bo ; để trống nếu không được xem lại. 

- Hai cột có đuôi _simulated là số phút giả lập đặt lên trace. Mọi con số tính từ hai cột này phải ghi nhãn simulated trong hồ sơ. 

### **Số liệu dùng chung** 

|**Khoản**|**Giá trị**|
|---|---|
|Token đầu vào|26 đ cho 1.000 token (bảng giá giả định)|
|Token đầu ra|130 đ cho 1.000 token (bảng giá giả định)|
|Gọi tool|15 đ mỗi lần|
|Thời gian của nhân viên|2.000 đ mỗi phút, đã gồm bảo hiểm và văn phòng|
|Nhân viên tự làm một yêu cầu|6 phút, tức 12.000 đ|
|Chi phí cố định của trợ lý|40 triệu đ mỗi tháng (vận hành, giám sát, cập nhật chính sách)|



### **Lịch buổi chiều** 

|**Giờ**|**Phút**|**Việc**|
|---|---|---|
|14:00|10|Chia nhóm 4 người, mở file, chạy thửlab13_starter.py|



AI20K · Ngày 13 · Launch & Economics · Trang 1 

|**Giờ**|**Phút**|**Việc**|
|---|---|---|
|14:10|43|Nhiệm vụ A · Mô hình chi phí (40 phút làm, 3 phút chữa)|
|14:53|27|Nhiệm vụ B · Bảng độ nhạy (25 phút làm, 2 phút chữa)|
|15:20|15|Giải lao|
|15:35|33|Nhiệm vụ C · Bảng lỗi và cách khắc phục (30 phút làm, 3 phút chữa)|
|16:08|28|Nhiệm vụ D · pilot_plan.yaml (25 phút làm, 3 phút chữa)|
|16:36|24|Nhiệm vụ E · Chỉ số, rủi ro kinh tế, hồ sơ launch v0 (20 phút làm, 4 phút chữa)|
|17:00|45|Duyệt chéo Gate 2a giữa các nhóm|
|17:45|15|Đóng gói, nộp|



Sau mỗi nhiệm vụ, giảng viên chiếu slide đáp án kèm giải thích. Nhóm đối chiếu và sửa số của mình ngay lúc đó. 

### **Nộp gì** 

Một thư mục của nhóm gồm: code mô hình chi phí, bảng độ nhạy, bảng lỗi và cách khắc phục, pilot_plan.yaml , đặc tả chỉ số, các dòng rủi ro kinh tế, và một trang hồ sơ launch v0. Điểm: 70% đối chiếu đáp án, 30% do nhóm hội đồng chấm theo thang ở cuối tài liệu. 

## **Nhiệm vụ A · Mô hình chi phí mỗi việc thành công (40 phút)** 

Mục tiêu: tính được chi phí thật cho mỗi yêu cầu được giải quyết, từ trace, và chỉ ra nó gấp bao nhiêu lần hoá đơn token. 

Chi phí mỗi việc thành công=<sup>token+tool+xem lại+làm lại</sup> số việc thành công 

Tử số tính mọi lần chạy, kể cả lần lỗi. Mẫu số chỉ đếm yêu cầu có ket_qua là thanh_cong . 

### **A1 · Ba phép thử đáp án biết trước (10 phút)** 

Viết ba hàm trong lab13_starter.py . Với p = 0,8, code phải trả đúng: 

|**Phép thử**|**Đáp án**|
|---|---|
|Số lần chạy trung bình khi cho chạy tối đa 2 lần|1,20|
|Số lần chạy trung bình khi chạy đến lúc đúng|1,25|
|Chi phí mỗi việc thành công khi cho chạy tối đa 3 lần, tính bằng bội số của giá một lần chạy|1,25|



Chưa đạt cả ba thì chưa làm tiếp: mọi con số phía sau sẽ sai theo. 

### **A2 · Tính từ trace (20 phút)** 

Viết hàm mo_hinh(runs, reqs) rồi điền bảng: 

|**Khoản**|**Số tiền (đ)**|**Nguồn**|**Nhãn**|
|---|---|---|---|
|Token||logix_runs.csv|đo từ trace|
|Tool||logix_runs.csv|đo từ trace|
|Trong đó, phần của lần chạy thứ 2 và 3||attemptlớn hơn 1|đo từ trace|
|Xem lại||phut_xem_lai_simulated|simulated|
|Làm lại||phut_lam_lai_simulated|simulated|
|Tổng chi phí||||



AI20K · Ngày 13 · Launch & Economics · Trang 2 

|**Khoản**|**Số tiền (đ)**|**Nguồn**|**Nhãn**|
|---|---|---|---|
|Số việc thành công||ket_qua||
|Chi phí mỗi việc thành công||||
|Hoá đơn token và tool chia cho số yêu cầu||||



Trả lời hai câu: 

1. Chi phí mỗi việc thành công gấp bao nhiêu lần con số “hoá đơn chia số yêu cầu”? 

2. Khoản nào chiếm tỉ trọng lớn nhất trong tổng chi phí? Bao nhiêu phần trăm? 

### **A3 · Tách theo loại yêu cầu (10 phút)** 

Chạy lại mô hình cho từng giá trị của cột loai : 

|**Loại**|**Số yêu**<br>**cầu**|**Tỉ lệ thành**<br>**công**|**Số lần chạy mỗi yêu**<br>**cầu**|**Chi phí mỗi việc thành công**|**So với 12.000**<br>**đ**|
|---|---|---|---|---|---|
|noi_dia||||||
|hang_n||||||
|ang||||||
|quoc_te||||||
|doi_tac||||||



Trả lời: loại nào không đáng để trợ lý xử lý? Với loại đó, việc cho chạy lại tới 3 lần có giúp không? Dựa vào hai cột giữa để lập luận. 

**Xong khi:** ba phép thử đạt; bảng A2 đủ 9 dòng và hai dòng giả lập có nhãn; bảng A3 đủ 4 dòng. Số của nhóm được nhận nếu lệch không quá 2% so với đáp án. 

**Lỗi hay gặp:** chỉ cộng token của lần chạy thành công; chia cho 1.200 thay vì số việc thành công; quên đổi 1.000 token; đọc file bằng pandas mà không đặt keep_default_na=False nên ô trống thành NaN. 

## **Nhiệm vụ B · Bảng độ nhạy (25 phút)** 

Mục tiêu: tìm yếu tố làm chi phí mỗi việc thành công thay đổi nhiều nhất, để biết pilot phải theo dõi gì. 

### **B1 · Đổi từng yếu tố (12 phút)** 

Mỗi dòng chỉ đổi một yếu tố, giữ nguyên các yếu tố khác như kết quả A2. 

|**Kịch bản**|**Cách tính**|**Chi phí mỗi việc thành**<br>**công**|**Thay đổi**<br>**(%)**|
|---|---|---|---|
|Giá token gấp đôi|52 đ và 260 đ cho 1.000 token; giá tool giữ<br>nguyên|||
|Giá token giảm một nửa|13 đ và 65 đ|||
|Tỉ lệ xem lại gấp đôi|Tiền xem lại × 2; tiền làm lại giữ nguyên|||
|Tỉ lệ xem lại giảm một<br>nửa|Tiền xem lại ÷ 2|||
|Số ca làm lại gấp đôi|Tiền làm lại × 2|||
|Số ca làm lại giảm một<br>nửa|Tiền làm lại ÷ 2|||
|Lương nhân viên tăng<br>25%|2.500 đ mỗi phút|||
|Chỉ cho chạy tối đa 2 lần|Xem cách tính bên dưới|||



AI20K · Ngày 13 · Launch & Economics · Trang 3 

|**Kịch bản**|**Cách tính**|**Chi phí mỗi việc thành**<br>**công**|**Thay đổi**<br>**(%)**|
|---|---|---|---|
|Chỉ cho chạy 1 lần|Xem cách tính bên dưới|||



Cách tính hai dòng cuối: bỏ các lần chạy có attempt lớn hơn giới hạn. Yêu cầu có so_lan_chay lớn hơn giới hạn coi như chuyen_nhan_vien , số phút xem lại và làm lại của yêu cầu đó bằng 0. 

### **B2 · Đổi một cặp và xếp hạng (3 phút)** 

Tính thêm kịch bản giá token gấp đôi cùng lúc tỉ lệ xem lại gấp đôi. Sau đó xếp hạng ba yếu tố ảnh hưởng mạnh nhất. 

### **B3 · Giới hạn chạy lại có thật sự rẻ hơn (5 phút)** 

Với giới hạn 1, 2 và 3 lần chạy, tính chi phí cả hệ thống cho 1.200 yêu cầu: tổng chi phí của trợ lý cộng 12.000 đ cho mỗi yêu cầu không thành công, vì nhân viên phải làm thay. Giới hạn nào rẻ nhất cho công ty? Nó có trùng với giới hạn cho chi phí mỗi việc thành công thấp nhất không? 

### **B4 · Nếu phải xem lại tất cả (5 phút)** 

Giả sử pilot chỉ nhận noi_dia và hang_nang , và tuần đầu nhân viên xem lại mọi câu trả lời trước khi gửi. Mỗi yêu cầu chạy ok được xem lại 5 phút. Câu trả lời sai bị bắt trước khi gửi, làm lại mất 9 phút mỗi ca. Tính chi phí mỗi việc thành công và so với 12.000 đ. Kết quả này nói gì về thứ pilot cần học được? 

**Xong khi:** bảng B1 đủ 9 dòng; có xếp hạng ba yếu tố; có câu trả lời cho B3 và B4, mỗi câu không quá ba dòng. 

## **Nhiệm vụ C · Bảng lỗi và cách khắc phục (30 phút)** 

Mục tiêu: gắn nhãn 20 ca lỗi theo năm loại, đạt đồng thuận từ 80%, rồi gán cách khắc phục cho từng loại. 

Năm loại lỗi, theo Google PAIR: 

|**Loại**|**Nghĩa là**|
|---|---|
|Do người dùng|Người dùng nhập sai hoặc chọn sai|
|Hệ thống|Hệ thống trả lời sai hoặc làm sai so với thiết kế và chính sách|
|Ngữ cảnh|Hệ thống làm đúng thiết kế nhưng người dùng thấy là sai, vì giả định của hệ thống không<br>khớp hoàn cảnh của họ|
|Giới hạn hệ thống|Hệ thống không thể trả lời, do thiếu dữ liệu, ngoài phạm vi, hoặc dạng đầu vào không xử lý<br>được|
|Ngầm|Có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra|



### **Các bước** 

1. 8 phút: hai người trong nhóm gắn nhãn độc lập cả 20 ca, không trao đổi. Hai người còn lại hoàn thiện nhiệm vụ B. 

2. 3 phút: so nhãn, đếm số ca trùng. Tỉ lệ đồng thuận = số ca trùng ÷ 20. 

3. 5 phút: với ca không trùng, cả nhóm thống nhất nhãn và ghi một câu quy tắc phân biệt. Dưới 80% thì viết lại định nghĩa trước khi đi tiếp. 

4. 14 phút: chọn 5 ca, mỗi loại một ca, điền bảng: phát hiện bằng gì, khắc phục thế nào, ai phụ trách. 

AI20K · Ngày 13 · Launch & Economics · Trang 4 

### **Hai mươi ca lỗi** 

|**Ca**<br>1|**Mô tả**<br>Khách nhập số tài khoản nhận hoàn tiền thiếu hai chữ số. Trợ lý tạo lệnh hoàn, ngân hàng trả về lỗi.|
|---|---|
|2|Kiện nội địa 28 kg. Trợ lý gọi tool tra bảng giá với tham số hàng thường thay vì hàng nặng, hoàn thiếu<br>45.000 đ. Khách mở lại sau 2 ngày.|
|3|Theo thiết kế, trợ lý hoàn tiền về ví LogiX trong 5 phút. Khách chờ tiền về tài khoản ngân hàng và báo<br>“chưa được hoàn”.|
|4|Khách yêu cầu hoàn phí cho chặng do hãng nước ngoài giao. LogiX không có dữ liệu chặng này. Trợ lý<br>nói không xác định được trạng thái và chuyển cho nhân viên.|
|5|Kiểm tra mẫu cuối tuần thấy 14 đơn có mã giảm giá bị hoàn theo giá trước giảm, thừa trung bình<br>12.000 đ mỗi đơn. Không khách nào báo, không cảnh báo nào kích.|
|6|Khách chọn mục “Hoàn phí giao trễ” nhưng nội dung mô tả hàng bị vỡ. Trợ lý xử lý theo luồng giao trễ<br>và từ chối vì đơn giao đúng hạn.|
|7|API sổ cái trả lỗi 503 ở bước ghi hoàn tiền. Trợ lý thử lại 3 lần rồi vẫn báo khách “đã hoàn tiền thành<br>công”.|
|8|Trợ lý dẫn “Điều 7.2 chính sách hoàn phí” làm căn cứ. Bản chính sách hiện hành không có điều 7.2. Số<br>tiền hoàn vẫn đúng.|
|9|Khách nhập mã đơn của sàn thương mại điện tử thay vì mã vận đơn. Trợ lý báo “mã không hợp lệ” rồi<br>dừng, không gợi ý gì.|
|10|Đơn giao trễ do bão. Trợ lý từ chối hoàn theo điều khoản bất khả kháng, đúng chính sách. Khách thấy<br>vô lý vì ứng dụng vẫn hiện “cam kết giao 24 giờ”.|
|11|Khách gửi tin nhắn thoại 40 giây. Trợ lý không xử lý được âm thanh, trả lời “vui lòng nhập bằng chữ”.|
|12|Tool tra đơn của depot D05 trả thiếu một trường. Trợ lý vẫn ra kết quả đúng sau nhiều lần gọi, nên tiền<br>token của D05 gấp 3 lần depot khác suốt 3 tuần mà không ai thấy.|
|13|Khách hỏi hoàn phí bảo hiểm hàng hoá, sản phẩm của công ty bảo hiểm đối tác, ngoài phạm vi trợ lý.<br>Trợ lý trả lời chung chung về phí vận chuyển, không nói rõ là mình không xử lý được.|
|14|Khách bấm nhầm “Xác nhận đã nhận tiền” khi chưa nhận. Yêu cầu bị đóng.|
|15|Đơn trễ 26 giờ. Chính sách: trễ 24–48 giờ hoàn 50%. Trợ lý tính hoàn 100%. Nhân viên xem lại bắt<br>được trước khi gửi.|
|16|Theo thiết kế “gửi ngay khi xong”, trợ lý gửi thông báo hoàn tiền qua Zalo lúc 2:14 sáng. Khách phản<br>ánh bị làm phiền.|
|17|Bảng giá đổi từ ngày 01/11 nhưng trợ lý vẫn dùng bản cũ trong bộ nhớ đệm cho đơn dưới 2 kg. Lệch<br>1.000–2.000 đ mỗi đơn, 212 đơn trong 9 ngày, không ai mở lại.|
|18|Trợ lý tính đúng: phí giao 30.000 đ, hoàn 50%. Tin nhắn chỉ ghi “Đã hoàn 15.000 đ”, không kèm cách<br>tính. Khách cho là hoàn thiếu và mở lại yêu cầu.|
|19|Khách yêu cầu hoàn phí cho đơn từ 14 tháng trước. Trợ lý chỉ truy cập được dữ liệu 12 tháng. Trợ lý<br>nói rõ không tra được và chuyển cho nhân viên kèm tóm tắt.|
|20|Khách gửi lại yêu cầu sau 10 phút vì chưa thấy phản hồi. Trợ lý hoàn hai lần cho cùng một đơn vì lệnh<br>thứ hai không có khoá chống trùng.|



### **Bảng cần điền cho 5 ca đã chọn** 

|**Ca**<br>**Loại lỗi**<br>**Phát hiện bằng gì**|**Khắc phục thế nào**<br>**Ai phụ trách**|
|---|---|



AI20K · Ngày 13 · Launch & Economics · Trang 5 

**Xong khi:** có hai bộ nhãn độc lập và tỉ lệ đồng thuận; tỉ lệ từ 80% trở lên, hoặc có định nghĩa đã sửa; bảng 5 ca đủ năm loại, mỗi dòng có cách phát hiện đo được và một người phụ trách có tên vai trò. 

## **Nhiệm vụ D · pilot_plan.yaml (25 phút)** 

Mục tiêu: một kế hoạch pilot tách được tác động của trợ lý và đủ cỡ mẫu, có điều kiện dừng viết trước. 

Số liệu cho sẵn: chỉ số chính hiện tại, khi chỉ có nhân viên, là 0,70. Giám đốc vận hành chỉ mở rộng nếu trợ lý nâng chỉ số này ít nhất 5 điểm. Dùng alpha 0,05, power 0,8, ICC 0,02. LogiX-VN có 40 nhân viên, 12 depot, 1.500 yêu cầu mỗi ngày. 

### **D1 · Cỡ mẫu theo ba cách chia (12 phút)** 

|**Câu**|**Việc cần tính**|
|---|---|
|a|Chia theo từng yêu cầu: cần bao nhiêu yêu cầu mỗi nhóm? Dùng statsmodels hoặc công thức so sánh<br>hai tỉ lệ.|
|b|Chia theo nhân viên, mỗi nhân viên 75 yêu cầu: hệ số thiết kế, cỡ mẫu mỗi nhóm, số nhân viên mỗi<br>nhóm. LogiX-VN có đủ người không?|
|c|Chia theo nhân viên, 20 người mỗi nhóm, mỗi người xử lý bao nhiêu yêu cầu cũng được: cỡ mẫu hiệu<br>dụng tối đa là bao nhiêu? Có đạt con số ở câu a không?|
|d|Chia theo depot, 6 depot mỗi nhóm: cỡ mẫu hiệu dụng tối đa là bao nhiêu?|
|e|Nếu chấp nhận chỉ thấy được mức chênh 6 điểm (cần 859 mỗi nhóm) và chia theo nhân viên 20 người<br>mỗi nhóm, mỗi nhân viên cần xử lý ít nhất bao nhiêu yêu cầu?|



hệ số thiết kế =1+( _m−_ 1) _⋅ I C C ,n_ hiệu dụng= _c ⋅ m_ 1+( _m−_ 1) _⋅ I C C_ 

Trong đó c là số cụm mỗi nhóm, m là số yêu cầu mỗi cụm. 

### **D2 · Năm câu kiểm tra “tách được tác động” (5 phút)** 

Chọn một cách chia rồi trả lời, mỗi câu một dòng: 

1. Nhóm đối chứng có chạy cùng thời gian với nhóm dùng trợ lý không? 

2. Việc chia nhóm là ngẫu nhiên hay do người chọn? 

3. Nhóm đối chứng có bị ảnh hưởng gián tiếp không, và nhóm làm gì để giảm? 

4. Chỉ số chính, ngưỡng và ngày quyết định đã viết trước khi chạy chưa? 

5. Nếu chia theo cụm, mỗi nhóm có ít nhất 20 cụm không? 

### **D3 · Viết file (8 phút)** 

Điền các chỗ có dấu hỏi. Phần stop_rules cần ít nhất ba luật: một về an toàn, một về chi phí, một về mức độ sử dụng. Mỗi luật viết theo mẫu NẾU [chỉ số vượt mức] – TRONG [bao lâu] – THÌ [việc cụ thể] – KHÔNG THÌ [việc bị cấm]. 

pilot **:** owner **:** "?" _# một người có tên vai trò, không ghi "cả đội"_ scope **:** "?" _# loại yêu cầu nào, depot nào; dựa vào kết quả A3_ assignment **:** unit **:** "?" _# request | staff | depot_ control_share **:** 0.5 randomized **:** true rollout **: [** 0.10 **,** 0.25 **,** 0.50 **]** _# mỗi bước một tuần_ primary_metric **:** name **:** dong_trong_24h_khong_mo_lai_7_ngay baseline **:** 0.70 mde **:** 0.05 alpha **:** 0.05 

AI20K · Ngày 13 · Launch & Economics · Trang 6 

power **:** 0.80 n_per_arm **:** "?" design_effect **:** "?" _# 1 nếu chia theo yêu cầu_ clusters_per_arm **:** "?" _# để trống nếu chia theo yêu cầu_ identifiability **:** concurrent_control **:** "?" spillover_risk **:** "?" predeclared **:** "?" stop_rules **: -** "NẾU ? TRONG ? THÌ ? KHÔNG THÌ ?" **-** "NẾU ? TRONG ? THÌ ? KHÔNG THÌ ?" **-** "NẾU ? TRONG ? THÌ ? KHÔNG THÌ ?" interim_looks **:** "chỉ kiểm tra chỉ số an toàn" rollback **:** "?" _# ai bấm, mất bao lâu, khách được phục vụ bằng gì_ decision_date **:** "?" simulated_inputs **: [** "?" **]** _# liệt kê mọi con số giả lập đã dùng_ 

Trước khi chốt luật an toàn, tính từ dữ liệu chạy thử: bao nhiêu phần trăm yêu cầu có mo_lai_trong_7_ngay bằng 1? Với ngưỡng nhóm định đặt, pilot có bị dừng ngay tuần đầu không? Nếu có, kế hoạch cần thêm kiểm soát gì? 

**Xong khi:** năm câu D1 có số; file không còn dấu hỏi; cách chia đã chọn đạt cả hai điều kiện tách được tác động và đủ cỡ mẫu, hoặc nhóm ghi rõ đánh đổi đã chấp nhận. 

## **Nhiệm vụ E · Chỉ số, rủi ro kinh tế, hồ sơ launch v0 (20 phút)** 

Mục tiêu: ghép bốn nhiệm vụ trước thành một trang để hội đồng ra quyết định. 

### **E1 · Đặc tả chỉ số (8 phút)** 

Chỉ số chính đã cho sẵn. Nhóm thêm ít nhất một chỉ số dùng và một chỉ số an toàn của riêng mình, rồi tính thử ba dòng đầu trên dữ liệu. 

|**Loại**|**Chỉ số**|**Công thức**|**Tính thử trên**<br>**1.200 yêu cầu**|
|---|---|---|---|
|Chính<br>(kết quả)|% yêu cầu đóng trong 24 giờ và không<br>mở lại trong 7 ngày|dong_trong_24hbằng 1 và<br>mo_lai_trong_7_ngaybằng 0, chia tổng số<br>yêu cầu||
|Dùng|Tỉ lệ bỏ qua gợi ý|quyet_dinh_xem_lailàsuahoặcbo, chia<br>số yêu cầu được xem lại||
|An toàn|Tỉ lệ lỗi lọt đến khách|mo_lai_trong_7_ngaybằng 1, chia tổng số<br>yêu cầu||
|Dùng|Nhóm tự đề xuất||Không cần tính|
|An toàn|Nhóm tự đề xuất||Không cần tính|



Sau đó liệt kê ít nhất sáu event cần ghi. Mỗi event có: tên, ai tạo, thuộc tính chính, thời điểm, và trace_id để nối với trace của agent. Kiểm tra chéo: chỉ số nào trong bảng không tính được từ danh sách event thì chưa đo được. 

### **E2 · Rủi ro kinh tế (4 phút)** 

Thêm ít nhất hai dòng vào risk register, số lấy từ bảng độ nhạy của nhóm. 

|**Rủi ro**<br>**Tác động đã tính**<br>**Dấu hiệu theo dõi**<br>**Hành động**<br>**Người phụ trách**|
|---|



AI20K · Ngày 13 · Launch & Economics · Trang 7 

### **E3 · Hồ sơ launch v0, một trang (8 phút)** 

|**Mục**|**Con số chính**|**Trạng thái**|**Người phụ trách**|
|---|---|---|---|
|1 · Chi phí mỗi việc thành công||||
|2 · Ba yếu tố nhạy nhất||||
|3 · So với nhân viên tự làm||||
|4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn||||
|5 · Bảng lỗi và cách khắc phục||||
|6 · Pilot plan||||
|7 · Rủi ro kinh tế||||



Cột trạng thái chỉ nhận một trong ba giá trị: Xong, có bằng chứng · Chưa · Giả lập. 

Dòng cuối của trang là đề xuất của nhóm: **Go** , **Go có điều kiện** (ghi từng điều kiện, người phụ trách, ngày kiểm tra) hoặc **No-go** (ghi việc phải làm để quay lại cổng). Không đề xuất nào được dùng từ “production”: Gate 2a chỉ duyệt kế hoạch pilot. 

## **Duyệt chéo Gate 2a (45 phút)** 

Mỗi nhóm vừa là đội trình hồ sơ, vừa là hội đồng của nhóm khác. Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. 

|**Giờ**<br>**Phú**|**t**<br>**Việc**|||
|---|---|---|---|
|17:00<br>10|Hoàn thiện trang hồ sơ l|aunch v0, gửi cho nhóm hội|đồng|
|17:10<br>15|Hội đồng đọc hồ sơ, chấ|m theo thang dưới đây, viế|t quyết định kèm lý do và một câu hỏi|
|17:25<br>15|Năm cặp nhóm trình bày<br>trả lời câu hỏi 1 phút|: đội trình hồ sơ nói 1 phút,|hội đồng công bố quyết định 1 phút, đội|
|17:40<br>5|Giảng viên chốt: quyết đị|nh nào khớp bằng chứng||
|**Thang chấm**<br>**Tiêu chí**|**của hội đồng (30 điểm)**<br>**0 điểm**|**5 điểm**|**10 điểm**|
|Đề xuất khớp<br>bằng chứng|Đề xuất mâu thuẫn với số của<br>chính nhóm|Khớp, nhưng bỏ qua<br>một con số bất lợi|Khớp, nêu cả con số bất lợi và cách xử<br>lý|
|Số giả lập và<br>phạm vi|Không ghi nhãn giả lập; phạm<br>vi là “mọi yêu cầu”|Có nhãn hoặc có thu<br>hẹp phạm vi|Có nhãn ở mọi con số giả lập; phạm vi<br>thu hẹp có lý do bằng số|
|Pilot ra được<br>quyết định|Không có đối chứng hoặc thiếu<br>cỡ mẫu|Đủ cỡ mẫu, luật dừng<br>còn chung chung|Tách được tác động, đủ cỡ mẫu, luật<br>dừng có ngưỡng, thời hạn, người có<br>quyền dừng|



### **Điểm đối chiếu đáp án (70 điểm)** 

|**Nhiệm vụ**|**Điểm**|**Điều kiện**|
|---|---|---|
|A|20|Ba phép thử đạt cả ba; số ở A2 và A3 lệch không quá 2%|
|B|15|Bảng B1 lệch không quá 2%; xếp hạng đúng; B3 và B4 có số|
|C|10|Đồng thuận trong nhóm từ 80%; khớp đáp án từ 16 trên 20 ca|
|D|15|Năm câu D1 đúng; file đủ trường; ít nhất ba luật dừng đúng mẫu|
|E|10|Ba chỉ số tính thử đúng; đủ sáu event có trace_id; đủ hai dòng rủi ro; trang hồ sơ đủ bảy<br>mục|



AI20K · Ngày 13 · Launch & Economics · Trang 8 

### **Làm thêm nếu xong sớm, không tính điểm** 

- Chạy lại nhiệm vụ A và B trên trace của chính agent nhóm bạn từ các ngày trước. So chi phí mỗi việc thành công của nhóm với mục tiêu trong acceptance profile. 

- Tính tỉ lệ thành công theo từng staff_id trong dữ liệu mẫu. Độ chênh giữa các nhân viên gợi ý gì về giả định ICC 0,02? 

- Làm ba bài trong tài liệu “Bài tập nâng cao — đề bài”: khoảng tin cậy bằng bootstrap, mô phỏng power và kiểm định tuần tự, định tuyến mô hình. Cần thêm hai file nang_cao_starter.py và logix_models.csv . 

Cách tổ chức nhóm, cấu trúc thư mục nộp và các lỗi hay gặp nằm trong tài liệu “Hướng dẫn học viên”. 

AI20K · Ngày 13 · Launch & Economics · Trang 9 

