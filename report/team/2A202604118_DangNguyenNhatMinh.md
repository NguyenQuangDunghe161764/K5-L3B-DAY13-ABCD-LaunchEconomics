# Báo cáo cá nhân — Đặng Nguyễn Nhật Minh (2A202604118)

## 1. Thông tin thành viên

- Họ tên: Đặng Nguyễn Nhật Minh
- MSSV: 2A202604118
- Email: 26ai.minhdnn@vinuni.edu.vn
- Vai trong nhóm: Người kiểm số

## 2. Phần việc phụ trách

Tôi phụ trách đối chiếu kết quả tính chi phí ở nhiệm vụ A và tổng hợp kết quả phân tích độ nhạy ở nhiệm vụ B vào bảng chi phí của nhóm.

## 3. Đóng góp cụ thể

- Chạy `src/lab13.py` trên máy cá nhân và xác nhận ba phép thử A1 đều báo `ĐẠT`, với các giá trị kỳ vọng 1,20 · 1,25 · 1,25.
- Kiểm tra độc lập chi phí gọi tool bằng cách cộng cột `tool_calls` trên toàn bộ lượt chạy trong `src/logix_runs.csv`. Kết quả là 5.600 lượt × 15 đ/lượt = 84.000 đ, khớp với bảng A2.
- Điền các bảng A1–A4 và B1–B4 từ kết quả chạy của nhóm, đồng thời ghi nhãn `simulated` cho các kết quả dùng dữ liệu thời gian xem lại hoặc làm lại giả lập.

## 4. Bằng chứng

- File đóng góp: [`bang_chi_phi.md`](bang_chi_phi.md).
- Commit trên nhánh `main`: [`042f972`](https://github.com/NguyenQuangDunghe161764/K5-L3B-DAY13-ABCD-LaunchEconomics/commit/042f972).
- Kết quả kiểm tra A2 trên máy cá nhân: `Tool calls: 5600` và `Tool cost (VND): 84000`.

## 5. Công cụ AI đã dùng

Tôi dùng ChatGPT để được hướng dẫn chạy bài, giải thích ba phép thử A1, gợi ý lệnh kiểm tra chi phí gọi tool và hỗ trợ soạn bảng chi phí cùng báo cáo cá nhân bằng tiếng Việt. Tôi chạy `lab13.py` trên máy cá nhân để lấy số liệu điền bảng, sau đó chạy một lệnh Python riêng đọc trực tiếp CSV để đối chiếu chi phí gọi tool. Hai cách đều cho kết quả 84.000 đ.

## 6. Tự đánh giá

Qua A2, tôi hiểu vì sao phải tính chi phí của cả lượt chạy thất bại: các lượt này vẫn tiêu tốn tài nguyên, trong khi mẫu số của chi phí mỗi việc thành công chỉ gồm 978 yêu cầu đã xử lý thành công.

Qua B3, tôi thấy lựa chọn số lần chạy phụ thuộc vào mục tiêu. Giới hạn 2 lần cho tổng chi phí hệ thống thấp nhất, 6.901.220 đ, còn giới hạn 1 lần cho chi phí trợ lý mỗi việc thành công thấp nhất, 4.111 đ (`simulated`). Tôi đối chiếu độc lập chi phí gọi tool ở A2 và kiểm tra trực tiếp ba chỉ số CP5 từ src/logix_requests.csv: đóng trong 24 giờ và không mở lại trong 7 ngày (82,83%), sửa hoặc bỏ gợi ý (27,12%) và mở lại trong 7 ngày (4,25%). Tôi đã gửi tỉ lệ mở lại cho nhóm để dùng làm mốc an toàn ở CP4 và gửi cả ba kết quả để điền CP5.
