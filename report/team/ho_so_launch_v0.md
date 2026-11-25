# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Một trang. Cột trạng thái chỉ nhận: **Xong, có bằng chứng · Chưa · Giả lập**. Mục nào dựa trên cột `_simulated` ghi Giả lập. Người phụ trách là một vai trò, không ghi "cả đội". Gate 2a chỉ duyệt kế hoạch pilot: không viết như thể trợ lý đã được duyệt chạy chính thức (xem quy tắc 5 trong `README.md`).

Nhóm: ... · Lớp: ...

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công; gấp 16,28× hoá đơn token + tool mỗi yêu cầu | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương nhân viên +25%: +23,1% | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | `noi_dia` 2.696 đ (0,22×); `hang_nang` 8.221 đ (0,69×); `quoc_te` 22.515 đ (1,88×), loại khỏi pilot. Phạm vi `noi_dia` + `hang_nang` gồm chi phí cố định: 4.599–5.784 đ (0,38–0,48×) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Chờ CP5 | Chưa | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20/20 nhãn trùng (100%); đủ 5 loại lỗi và biện pháp khắc phục có ngưỡng theo dõi | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | Đã điền kế hoạch: ngẫu nhiên theo nhân viên, 20/nhánh; MDE 6 điểm, 859 yêu cầu hiệu dụng (5.980 thô)/nhánh; ba luật dừng, rollback 30 phút. Cần xác nhận đủ 11.960 yêu cầu tổng (xấp xỉ 10× 1.200 yêu cầu lịch sử); power khoảng 0,64 nếu tác động thật là 5 điểm | Giả lập | Người giữ hồ sơ |
| 7 · Rủi ro kinh tế | Làm lại ×2: chi phí +51,8%; xem lại ×2: +40,7%. Mở lại nền 4,25%; dừng nếu chênh với đối chứng ≥2 điểm hoặc vượt 6% trong 3 lần kiểm tra liên tiếp sau đủ 7 ngày theo dõi, hoặc có ca hoàn trùng trong cửa sổ 3 ngày | Giả lập | Người giữ hồ sơ |

**Đề xuất:** Go có điều kiện — chỉ xem xét pilot `noi_dia` + `hang_nang`, loại `quoc_te`; theo dõi ca làm lại, tỉ lệ xem lại và mở lại. Trước khi chạy, xác nhận khả năng đạt cỡ mẫu CP4 và hoàn tất CP5; kế hoạch mô phỏng này chưa phải phê duyệt chạy chính thức.
