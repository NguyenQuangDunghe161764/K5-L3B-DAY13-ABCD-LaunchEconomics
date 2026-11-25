# Hồ sơ launch v0 · Trợ lý hoàn phí LogiX-VN · Gate 2a

Nhóm ABCD · Lớp L3B · Gate 2a xét kế hoạch pilot.

| Mục | Con số chính | Trạng thái | Người phụ trách |
| --- | --- | --- | --- |
| 1 · Chi phí mỗi việc thành công | 4.472 đ/việc thành công; gấp 16,28× hoá đơn token + tool mỗi yêu cầu | Giả lập | Người kiểm số |
| 2 · Ba yếu tố nhạy nhất | Làm lại ×2: +51,8%; xem lại ×2: +40,7%; lương nhân viên +25%: +23,1% | Giả lập | Người viết code |
| 3 · So với nhân viên tự làm | `noi_dia` 2.696 đ (0,22×); `hang_nang` 8.221 đ (0,69×); `quoc_te` 22.515 đ (1,88×), loại khỏi pilot. Phạm vi `noi_dia` + `hang_nang` gồm chi phí cố định: 4.599–5.784 đ (0,38–0,48×) | Giả lập | Người kiểm số |
| 4 · Chỉ số chính, chỉ số dùng, chỉ số an toàn | Đợt chạy thử: đóng trong 24 giờ và không mở lại trong 7 ngày **82,83%**; sửa hoặc bỏ gợi ý **27,12%** trong số ca đã xem lại; mở lại **4,25%**. [Đặc tả và event](chi_so.md) | Giả lập | Người giữ hồ sơ |
| 5 · Bảng lỗi và cách khắc phục | 20/20 nhãn trùng (100%); đủ 5 loại lỗi và biện pháp khắc phục có ngưỡng theo dõi | Xong, có bằng chứng | Người gắn nhãn 1 |
| 6 · Pilot plan | [Kế hoạch CP4](pilot_plan.yaml) chia ngẫu nhiên 20 nhân viên mỗi nhóm. Cần 299 yêu cầu đủ điều kiện mỗi người, tương đương 859 mẫu hiệu dụng mỗi nhóm, để phát hiện chênh lệch 6 điểm phần trăm với power 80%. Với chênh lệch 5 điểm, power khoảng 64%. | Giả lập | Người giữ hồ sơ |
| 7 · Rủi ro kinh tế | Làm lại ×2 làm chi phí tăng **51,8%**. Xem lại 100% với 15,3 phút làm lại/ca đẩy chi phí lên **12.415 đ/việc**, vượt mức thủ công 12.000 đ. [Ngưỡng theo dõi và ứng phó](chi_so.md#e2--rủi-ro-kinh-tế) | Giả lập | Người giữ hồ sơ |

| Điều kiện | Người phụ trách | Ngày kiểm tra dự kiến |
| --- | --- | --- |
| Xác nhận 40 nhân viên, phân tuyến đủ 299 yêu cầu mỗi người và chấp nhận power khoảng 64% nếu tác động thực là 5 điểm | Giám đốc vận hành | 29/11/2026 |
| Kiểm tra khóa chống hoàn trùng, đối soát sổ cái và sự kiện có `trace_id` ở cả hai nhánh | Người viết code | 29/11/2026 |
| Rà phút xem lại và làm lại đo được trong tuần đầu. Chỉ tăng bước khi đủ dữ liệu theo dõi và đạt các ngưỡng CP4 | Trưởng nhóm CSKH | 07/12/2026 |

**Đề xuất — Go có điều kiện** cho pilot `noi_dia` và `hang_nang` theo các mốc kiểm tra trên.
