# Báo cáo cá nhân — TrieuTuanMinh-2A202604123

Copy file này và đổi tên theo quy tắc `MSSV_HoTen.md`. Giữ nguyên file mẫu.

Ví dụ: `20241234_NguyenVanAn.md`.

## 1. Thông tin thành viên

- Họ tên: Triệu Tuấn Minh
- MSSV: 2A202604123
- Email: trieutuanminh004@gmail.com
- Vai trong nhóm (người viết code, người kiểm số, người gắn nhãn 1, người gắn nhãn 2 kiêm giữ hồ sơ): Người gắn nhãn 2 kiêm giữ hồ sơ

## 2. Phần việc phụ trách

- Người gắn nhãn 2: đọc và gắn nhãn độc lập 20 ca lỗi ở CP3, không trao đổi trước khi đối chiếu.
- Kiêm giữ hồ sơ: điền và cập nhật `ho_so_launch_v0.md` xuyên suốt CP1–CP5; tổng hợp bằng chứng, số liệu và đề xuất pilot của nhóm.

## 3. Đóng góp cụ thể

- Hoàn thành bộ nhãn độc lập cho 20 ca; cùng Người gắn nhãn 1 đối chiếu kết quả, đạt 20/20 ca trùng (100%).
- Tham gia hoàn thiện bảng khắc phục cho năm loại lỗi, gồm cách phát hiện đo được và vai trò phụ trách.
- Cập nhật hồ sơ launch sau từng checkpoint: chi phí và độ nhạy CP1–CP2; kết quả gắn nhãn CP3; cỡ mẫu, rollout và luật dừng CP4; chỉ số, event, rủi ro và đề xuất có điều kiện CP5.
- Phân biệt số liệu chạy thử giả lập với kết quả có bằng chứng; nêu điều kiện xác nhận đủ nhân viên và lưu lượng yêu cầu trước khi chạy pilot.

## 4. Bằng chứng

- `report/team/bang_loi.md`: bộ nhãn Người gắn nhãn 2 và kết quả đồng thuận 20/20 (100%).
- `report/team/ho_so_launch_v0.md`: hồ sơ bảy mục, các số liệu CP1–CP5, điều kiện Go có điều kiện.
- `report/team/chi_so.md`: số liệu mô tả đợt chạy thử giả lập: chỉ số chính 82,83%, tỉ lệ sửa/bỏ gợi ý 27,12%, tỉ lệ mở lại 4,25%; danh sách event và hai rủi ro kinh tế.
- `report/team/pilot_plan.yaml`: phương án CP4, cỡ mẫu, rollout và luật dừng được ghi trong hồ sơ.

## 5. Công cụ AI đã dùng

- Dùng Copilot trong VS Code để hỗ trợ biên tập và tổng hợp hồ sơ CP1–CP5.
- Tự đối chiếu các con số và trạng thái với `bang_chi_phi.md`, `bang_loi.md`, `chi_so.md` và `pilot_plan.yaml`; giữ nhãn giả lập cho số liệu từ dữ liệu chạy thử.

## 6. Tự đánh giá

- Hoàn thành việc gắn nhãn độc lập và cập nhật hồ sơ theo tiến độ; hồ sơ nêu rõ cả lợi ích, rủi ro và điều kiện dừng thay vì coi kết quả mô phỏng là phê duyệt triển khai.
- Cần tiếp tục xác nhận khả năng tuyển đủ 40 nhân viên và 299 yêu cầu mỗi người trước khi đề xuất bắt đầu pilot.
