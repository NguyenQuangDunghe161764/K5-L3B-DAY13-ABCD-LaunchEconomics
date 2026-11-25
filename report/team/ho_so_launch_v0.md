# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm ABCD · Lớp L3B · Gate 2a xét kế hoạch pilot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công; gấp 16,28× hoá đơn token + tool mỗi yêu cầu | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương nhân viên +25%: +23,1% | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | `noi_dia` 2.696 đ (0,22×); `hang_nang` 8.221 đ (0,69×); `doi_tac` 10.215 đ (0,85×); `quoc_te` 22.515 đ (1,88×). Pilot chọn `noi_dia` + `hang_nang`; loại `quoc_te` vì vượt mức thủ công. Có chi phí cố định: 4.599–5.784 đ/việc (0,38–0,48×) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: đóng trong 24 giờ và không mở lại trong 7 ngày **82,83%**; sửa hoặc bỏ gợi ý **27,12%** trong số ca đã xem lại; mở lại **4,25%**. [Đặc tả và event](chi_so.md) | Giả lập | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20/20 nhãn trùng (100%); đủ 5 loại lỗi và biện pháp khắc phục có ngưỡng theo dõi | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | [Kế hoạch CP4](pilot_plan.yaml): ngẫu nhiên theo nhân viên, 20/nhóm; cần 299 yêu cầu/người, tương đương 5.980 yêu cầu thô (859 hiệu dụng)/nhóm, để phát hiện chênh 6 điểm với power 80%. Với tác động thật 5 điểm, power khoảng 64%; xác nhận đủ 11.960 yêu cầu tổng (xấp xỉ 10× dữ liệu lịch sử) trước khi chạy | Giả lập | Người giữ hồ sơ |
| 7 · Rủi ro kinh tế | Làm lại ×2: +51,8% (6.787 đ/việc). Xem lại 100%: 12.415 đ/việc nếu làm lại mất 15,3 phút, vượt mức thủ công 12.000 đ; hoà vốn ở 4,80 phút xem lại/ca. Mở lại nền 4,25%; luật dừng an toàn: chênh ≥2 điểm hoặc >6%, hay có ca hoàn trùng. [Theo dõi và ứng phó](chi_so.md#e2--rủi-ro-kinh-tế) | Giả lập | Người giữ hồ sơ |

| Điều kiện | Người phụ trách | Ngày kiểm tra dự kiến |
| --- | --- | --- |
| Xác nhận 40 nhân viên, phân tuyến đủ 299 yêu cầu mỗi người và chấp nhận power khoảng 64% nếu tác động thực là 5 điểm | Giám đốc vận hành | 29/11/2026 |
| Kiểm tra khóa chống hoàn trùng, đối soát sổ cái và sự kiện có `trace_id` ở cả hai nhánh | Người viết code | 29/11/2026 |
| Rà phút xem lại và làm lại đo được trong tuần đầu; chỉ tăng bước khi đủ dữ liệu theo dõi và đạt ngưỡng CP4 | Trưởng nhóm CSKH | 07/12/2026 |

**Đề xuất — Go có điều kiện** cho pilot `noi_dia` và `hang_nang`: xác nhận 40 nhân viên và khả năng đạt 299 yêu cầu/người; kiểm tra chống hoàn trùng, sổ cái và event hai nhánh; đo phút xem lại/làm lại và chỉ tăng rollout khi đủ mẫu, đủ 7 ngày theo dõi, đạt ngưỡng CP4. Đây là đề xuất cho Gate 2a, chưa phải phê duyệt triển khai chính thức.
