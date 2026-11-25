# **Ngày 13 · Launch & Economics — Hướng dẫn học viên** 

L3A, L3B · Sáng 9:00–13:00, chiều 14:00–18:00 

## **Ngày hôm nay bạn sẽ làm được gì** 

Agent của nhóm bạn đã chạy được. Ngày 13 trả lời câu hỏi tiếp theo: có nên đưa nó ra cho người dùng thật không, và đưa ra thế nào để biết nó có hiệu quả. 

Cuối ngày, bạn làm được năm việc: 

1. Tính chi phí cho mỗi việc thành công từ trace, gồm cả tiền token, tool, lần chạy lại và giờ của nhân viên. 

2. Tìm yếu tố làm chi phí thay đổi nhiều nhất bằng bảng độ nhạy. 

3. Chọn một chỉ số chính, một chỉ số dùng, một chỉ số an toàn, và liệt kê event cần ghi để đo chúng. 

4. Phân loại lỗi theo năm loại và gán cách khắc phục có người phụ trách. 

5. Viết kế hoạch pilot có nhóm đối chứng, đủ cỡ mẫu, có luật dừng, rồi bảo vệ nó trước hội đồng Gate 2a. 

Sản phẩm nộp cuối ngày là bộ hồ sơ launch v0 cho trợ lý hoàn phí của công ty giả định LogiX-VN. 

## **Việc cần làm trước buổi học** 

### **Cài môi trường (10 phút)** 

Mỗi nhóm cần ít nhất hai máy chạy được Python 3.10 trở lên. 

pip install pandas numpy scipy statsmodels python3 -c "import pandas, numpy, scipy, statsmodels; print('san sang')" 

Dòng thứ hai phải in ra san sang . Lab không cần khoá API và không cần mạng trong lúc làm. 

### **Đọc trước (20 phút)** 

- Phần tóm tắt và phần giới thiệu của bài “Cost-of-Pass: An Economic Framework for Evaluating Language Models”, arxiv.org/abs/2504.13359. Chỉ cần nắm một ý: chi phí nên tính cho một lời giải đúng, không tính cho một lần gọi mô hình. 

### **Mang theo** 

- Con số baseline của nhóm từ Ngày 2: công việc hiện đang tốn bao nhiêu phút và bao nhiêu tiền khi con người tự làm. 

- Acceptance profile nhóm đã nộp ở Ngày 10. 

- Trace của agent nhóm bạn, nếu có. Dùng cho phần làm thêm. 

## **Lịch trong ngày** 

|**Giờ**|**Nội dung**|**Bạn làm gì**|
|---|---|---|
|9:00|Mở đầu|Đoán nhanh một con số|
|9:12|01 · Chi phí thật|Bài tập 1 theo cặp|
|10:05|02 · Tài chính căn bản, có đáng chạy không|Bốn câu tính nhẩm; tính mua hay tự làm|



AI20K · Ngày 13 · Launch & Economics · Trang 1 

|**Giờ**|**Nội dung**|**Bạn làm gì**|
|---|---|---|
|10:38|03 · Nhân viên có dùng không|Thảo luận một tín hiệu|
|11:00|Giải lao||
|11:15|04 · Khi hỏng thì sao|Bài tập 2 theo cặp|
|11:45|05 · Thiết kế pilot||
|12:20|06 · Duyệt launch, tổng kết||
|12:45|Exit ticket|Ba câu trắc nghiệm, làm một mình|
|13:00|Nghỉ trưa||
|14:00|Chia nhóm, mở file|Chạy thử file khởi đầu|
|14:10|Nhiệm vụ A · Mô hình chi phí|40 phút làm, 3 phút chữa|
|14:53|Nhiệm vụ B · Bảng độ nhạy|25 phút làm, 2 phút chữa|
|15:20|Giải lao||
|15:35|Nhiệm vụ C · Bảng lỗi và cách khắc phục|30 phút làm, 3 phút chữa|
|16:08|Nhiệm vụ D · pilot_plan.yaml|25 phút làm, 3 phút chữa|
|16:36|Nhiệm vụ E · Chỉ số, rủi ro, hồ sơ|20 phút làm, 4 phút chữa|
|17:00|Duyệt chéo Gate 2a|Trình hồ sơ và chấm nhóm khác|
|17:45|Đóng gói, nộp|Hạn nộp 18:00|



## **Cách học buổi sáng** 

Giảng viên nói từng lượt ngắn, sau mỗi lượt là một việc cho bạn làm. Sau mỗi câu hỏi trên slide là một slide đáp án kèm giải thích. 

- **Tự trả lời trước khi xem đáp án.** Viết con số của bạn ra giấy. Sai mà biết mình sai ở đâu có ích hơn đúng mà không biết vì sao. 

- **Bài tập theo cặp:** mỗi người tự tính trong nửa thời gian đầu, nửa sau so kết quả. 

- **Exit ticket** không tính điểm. Nó cho bạn biết phần nào cần đọc lại trước giờ lab. 

### **Sáu công thức của cả ngày** 

|**Tên**|**Công thức**|**Ghi nhớ**|
|---|---|---|
|Chi phí mỗi việc thành<br>công|(token + tool + xem lại + làm lại) ÷ số việc<br>thành công|Tử số tính mọi lần chạy, kể cả lần lỗi. Mẫu<br>số chỉ đếm việc thành công|
|Số lần chạy trung bình,<br>tối đa k lần|(1 − (1 − p)^k) ÷ p|Đúng khi các lần thử độc lập với nhau|
|Tỉ lệ thành công sau tối<br>đa k lần|1 − (1 − p)^k|Lỗi lặp lại ở cùng yêu cầu thì công thức này<br>quá lạc quan|
|Cỡ mẫu mỗi nhóm, so<br>hai tỉ lệ|(1,96 × √(2 ×  × (1 − )) + 0,84 × √(p (1 −<br>p̄�<br>p̄�<br>₁<br>p ) + p (1 − p )))² ÷ (p − p )², với  là trung<br>₁<br>₂<br>₂<br>₂<br>₁<br>p̄�<br>bình của p và p<br>₁<br>₂|Với alpha 0,05 và power 0,8. Từ 0,70 lên<br>0,75 cho 1.251|
|Hệ số thiết kế|1 + (m − 1) × ICC|m là số yêu cầu mỗi cụm|
|Cỡ mẫu hiệu dụng khi<br>chia theo cụm|c × m ÷ hệ số thiết kế, luôn nhỏ hơn c ÷<br>ICC|c là số cụm mỗi nhóm. Số cụm quyết định,<br>không phải tổng số yêu cầu|



## **Cách làm Lab 13** 

Đề bài đầy đủ nằm trong tài liệu “Lab 13 — đề bài học viên”. Phần này nói cách tổ chức để làm kịp giờ. 

AI20K · Ngày 13 · Launch & Economics · Trang 2 

### **Phân vai trong nhóm 4 người** 

|**Vai**|**Việc chính**|**Trong nhiệm vụ C**|
|---|---|---|
|Người viết code|Viết và chạylab13_starter.py|Hoàn thiện nhiệm vụ B|
|Người kiểm số|Tính tay một con số để đối chiếu, điền bảng|Hoàn thiện nhiệm vụ B|
|Người gắn nhãn 1|Đọc đề, theo dõi điều kiện “Xong khi”|Gắn nhãn 20 ca, độc<br>lập|
|Người gắn nhãn 2, kiêm giữ hồ<br>sơ|Ghép kết quả vào trang hồ sơ launch v0 từ đầu buổi|Gắn nhãn 20 ca, độc<br>lập|



Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí. 

### **Năm quy tắc của lab** 

1. **Qua ba phép thử rồi mới làm tiếp.** Ba phép thử đáp án biết trước ở A1 phải ra 1,20 · 1,25 · 1,25. Chưa đạt thì mọi con số phía sau sai theo. 

2. **Ghi nhãn simulated .** Mọi con số tính từ hai cột có đuôi _simulated phải có nhãn này trong hồ sơ. Thiếu nhãn bị trừ điểm. 

3. **Đối chiếu ngay khi slide chữa hiện lên.** Số của nhóm lệch quá 2% thì tìm chỗ sai trong lúc chữa; nhiệm vụ sau dùng lại số của nhiệm vụ trước. 

4. **Mỗi câu trả lời không quá ba dòng** , có ít nhất một con số. 

5. **Không dùng từ “production”.** Gate 2a chỉ duyệt kế hoạch pilot. 

### **Đọc dữ liệu cho đúng** 

**import** pandas **as** pd runs = pd.read_csv('logix_runs.csv') reqs = pd.read_csv('logix_requests.csv', keep_default_na=False) 

Phải có keep_default_na=False . Thiếu nó, ô trống trong cột quyet_dinh_xem_lai bị đọc thành NaN và phép so sánh phía sau cho kết quả sai. 

### **Gợi ý cho từng nhiệm vụ** 

|**Nhiệ**<br>**m**<br>**vụ**|**Bắt đầu từ đâu**|**Tự kiểm tra**|
|---|---|---|
|A|Viết ba hàm của A1 trước. Sau đó viết một hàm<br>mo_hinh(runs, reqs)trả về từng khoản, để nhiệm vụ<br>B gọi lại|Chi phí mỗi việc thành công phải lớn hơn nhiều lần so<br>với hoá đơn chia số yêu cầu. Nếu chỉ gấp 1–2 lần,<br>bạn đã quên giờ của nhân viên|
|B|Cho hàmmo_hinhnhận tham số giá và hệ số. Mỗi<br>kịch bản là một lần gọi hàm|Kịch bản “giảm một nửa” phải làm chi phí giảm bằng<br>nửa mức tăng của kịch bản “gấp đôi”|
|C|Hai người gắn nhãn ngồi tách nhau, không trao đổi<br>trong 8 phút|Trùng dưới 16 trên 20 ca thì viết lại định nghĩa trước<br>khi đi tiếp|
|D|Tính năm câu D1 trước rồi mới chọn cách chia nhóm|Cách chia đã chọn phải đạt cả hai điều kiện: tách<br>được tác động và đủ cỡ mẫu. Không đạt thì ghi rõ<br>đánh đổi|
|E|Điền trang hồ sơ từ đầu buổi, không đợi đến 16:36|Chỉ số nào không tính được từ danh sách event thì<br>chưa đo được|



### **Viết luật dừng** 

Mỗi luật dừng có đủ bốn vế: 

NẾU [chỉ số vượt mức] – TRONG [bao lâu] – THÌ [việc cụ thể, ai làm] – KHÔNG THÌ [việc bị cấm] 

AI20K · Ngày 13 · Launch & Economics · Trang 3 

Ví dụ cho một sản phẩm khác, không phải đáp án của lab: “NẾU tỉ lệ đơn giao nhầm địa chỉ vượt 0,5% TRONG 2 ngày liên tiếp THÌ trưởng ca tắt tính năng gợi ý địa chỉ trong 30 phút KHÔNG THÌ không được mở thêm kho nào.” 

## **Nộp bài** 

Nộp một thư mục trước 18:00, đặt tên lop_nhom (ví dụ L3A_nhom04 ). 

|**File**|**Nội dung**|**Nhiệm vụ**|
|---|---|---|
|lab13.py|Code chạy được từ đầu đến cuối, in ra các bảng|A, B, D1|
|bang_chi_phi.md|Bảng A2, A3, bảng độ nhạy, câu trả lời B3 và B4|A, B|
|bang_loi.md|Hai bộ nhãn, tỉ lệ đồng thuận, bảng khắc phục 5 ca|C|
|pilot_plan.yaml|Kế hoạch pilot, không còn dấu hỏi|D|
|chi_so.md|Đặc tả chỉ số, danh sách event, các dòng rủi ro kinh tế|E|
|ho_so_launch_v0.md|Một trang, bảy mục, dòng cuối là đề xuất của nhóm|E|
|phieu_cham.md|Phiếu nhóm bạn chấm nhóm khác khi làm hội đồng|Duyệt chéo|



Kiểm tra trước khi nộp: 

- python3 lab13.py chạy hết trên một máy khác trong nhóm. 

- Mọi con số giả lập có nhãn simulated . 

- Trang hồ sơ có cột trạng thái điền đủ, mỗi mục có người phụ trách là một vai trò, không ghi “cả đội”. 

- Đề xuất là một trong ba: Go, Go có điều kiện, No-go. 

## **Cách chấm** 

|**Phần**|**Điểm**|**Ai**<br>**chấm**|**Dựa vào**|
|---|---|---|---|
|Đối chiếu đáp án|70|Trợ<br>giảng|A 20 · B 15 · C 10 · D 15 · E 10. Số được nhận nếu lệch không quá 2%|
|Đánh giá của hội đồng|30|Nhóm<br>khác|Đề xuất khớp bằng chứng · số giả lập và phạm vi · pilot ra được quyết<br>định. Mỗi tiêu chí 0, 5 hoặc 10 điểm|



Khi làm hội đồng, bạn chấm theo bằng chứng trong hồ sơ, không theo cách trình bày. Một đề xuất “Nogo” có lý do bằng số được điểm cao hơn một đề xuất “Go” bỏ qua con số bất lợi. 

## **Mười lỗi hay gặp** 

|**Lỗi**|**Cách tránh**|
|---|---|
|Lấy hoá đơn token chia số yêu cầu làm chi phí|Cộng thêm tiền xem lại và làm lại, chia cho số việc thành<br>công|
|Chỉ cộng token của lần chạy thành công|Lần chạy lỗi vẫn tốn tiền|
|Quên giá tính cho 1.000 token|Chia 1.000 trước khi nhân giá|
|Tin rằng chạy lại luôn giúp|Xem tỉ lệ thành công theo loại yêu cầu; lỗi lặp lại thì chạy<br>lại chỉ tốn thêm|
|Tối ưu chi phí mỗi việc thành công mà quên phần việc để<br>lại cho nhân viên|Tính thêm chi phí cả hệ thống|
|Gắn nhãn lỗi sau khi đã bàn với nhau|Gắn độc lập trước, so sau|
|Ghi người phụ trách là “cả đội”|Ghi một vai trò có quyền quyết định|



AI20K · Ngày 13 · Launch & Economics · Trang 4 

|**Lỗi**|**Cách tránh**|
|---|---|
|Chia pilot theo depot vì dễ triển khai|Tính cỡ mẫu hiệu dụng tối đa trước khi chọn|
|Đặt ngưỡng dừng mà không nhìn dữ liệu chạy thử|Tính tỉ lệ hiện tại của chỉ số an toàn trước|
|Viết trợ lý “đã nâng” chỉ số khi chưa có nhóm đối chứng|Chỉ nói “chỉ số trong đợt chạy thử là…”, để pilot trả lời<br>phần còn lại|



## **Thuật ngữ** 

|**Thuật ngữ**|**Nghĩa trong ngày hôm nay**|
|---|---|
|Việc thành công|Yêu cầu đã đóng, không mở lại trong 7 ngày, không sai tiền|
|Xem lại|Nhân viên đọc câu trả lời của trợ lý trước khi gửi cho khách|
|Làm lại|Nhân viên phải tự xử lý lại vì trợ lý trả lời sai|
|Trace|Bản ghi từng bước của một lần agent chạy|
|Event|Một sự kiện được ghi lại trong sản phẩm, có tên, thời điểm, thuộc tính và<br>trace_id|
|Chỉ số chính|Một chỉ số duy nhất quyết định pilot thành hay bại, viết ra trước khi chạy|
|Chỉ số an toàn|Chỉ số không được xấu đi; vượt ngưỡng thì dừng|
|Pilot|Đợt chạy có giới hạn, có nhóm đối chứng, để ra một quyết định|
|Nhóm đối chứng|Nhóm không dùng trợ lý, chạy cùng thời gian, để so sánh|
|Cụm|Đơn vị được chia nhóm, ví dụ một nhân viên hoặc một depot|
|ICC|Mức giống nhau giữa các yêu cầu trong cùng một cụm, từ 0 đến 1|
|Mức chênh nhỏ nhất phát hiện được|Mức cải thiện nhỏ nhất mà pilot đủ mẫu để thấy; trong file viết làmde|
|Gate 2a|Cổng duyệt kế hoạch pilot của chương trình|
|Go, Go có điều kiện, No-go|Ba quyết định của hội đồng: cho chạy, cho chạy kèm điều kiện, chưa cho<br>chạy|



## **Sau buổi học** 

|**Việc**|**Khi nào**|**Để làm gì**|
|---|---|---|
|Chạy lại nhiệm vụ A và B trên trace của agent<br>nhóm bạn|Trước<br>Ngày 14|Có chi phí mỗi việc thành công thật của nhóm, so<br>với acceptance profile|
|Viết danh sách event cho agent của nhóm|Trước<br>Ngày 14|Ngày 14 dùng chính danh sách này để dựng bảng<br>theo dõi và cảnh báo|
|Hoàn thiện hồ sơ launch của nhóm theo nhận xét<br>của hội đồng|Trước<br>Ngày 15|Mang vào buổi bảo vệ|
|Làm ba bài nâng cao|Tự chọn|Đi sâu về khoảng tin cậy, mô phỏng pilot và định<br>tuyến mô hình|



Ba bài nâng cao nằm trong tài liệu “Bài tập nâng cao — đề bài”. Lời giải Lab 13 được phát sau khi có điểm. 

## **Tài liệu tham khảo** 

- Erol và cộng sự, “Cost-of-Pass: An Economic Framework for Evaluating Language Models”, arxiv.org/abs/2504.13359. 

- Anthropic, “Demystifying evals for AI agents”, 2026. 

- Google PAIR, People + AI Guidebook, chương “Errors + Graceful Failure”, pair.withgoogle.com. 

- Tài liệu statsmodels, lớp NormalIndPower , mục stats.power . 

AI20K · Ngày 13 · Launch & Economics · Trang 5 

## **Video xem thêm theo từng phần** 

Sáu video tiếng Anh, mỗi phần một video, xem sau buổi học. 

|**Phần**|**Video**|**Kênh**|**Thời lượng**|**Đường dẫn**|
|---|---|---|---|---|
|01 · Chi phí thật|LLM Cost Optimization: Token<br>Economics for Agentic FinOps|KryptoMindz<br>Technologies|Khoảng 12–15 phút<br>theo mô tả của kênh|youtube.com/<br>watch?<br>v=pZNtpZnj4E0|
|02 · Có đáng<br>chạy không|Outcome-Based Pricing Explained:<br>Paying for the Result|FourWeekMBA|Chưa kiểm chứng|youtube.com/<br>watch?<br>v=_z_XTjk6miQ|
|03 · Nhân viên<br>có dùng không|5 Feature Adoption Metrics That<br>Every PM Should Track|Userpilot|Khoảng 3 phút|youtube.com/<br>watch?<br>v=uVcUKQwgCU<br>4|
|04 · Khi hỏng<br>thì sao|Human in the Loop Is Not a<br>Governance Strategy for Agentic AI|IBM|Chưa kiểm chứng|youtube.com/<br>watch?<br>v=zRMAvMSSSII|
|05 · Thiết kế<br>pilot|Statistical Power, Clearly<br>Explained!!!|StatQuest with<br>Josh Starmer|Khoảng 8 phút|youtube.com/<br>watch?<br>v=Rsc5znwR5FA|
|06 · Duyệt<br>launch|Reducing Your Risk with Canary<br>Deployments|CA<br>Technologies|4:59|youtube.com/<br>watch?<br>v=c4xcn4sYIOE|



AI20K · Ngày 13 · Launch & Economics · Trang 6 

