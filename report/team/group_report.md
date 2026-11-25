# Báo cáo nhóm · Lab 13

## 1. Thông tin nhóm

Nhóm ABCD, lớp L3B. Thành viên và phần việc đã ghi nhận trong [TEAM.md](../../TEAM.md).

## 2. Mục tiêu và cách tiếp cận

Đánh giá chi phí và rủi ro của trợ lý hoàn phí LogiX-VN bằng 1.200 yêu cầu giả lập. Dùng kết quả để chọn phạm vi pilot, cách chia nhóm, chỉ số và luật dừng.

## 3. Giải pháp

- **A.** Cộng chi phí mọi lượt chạy, xem lại và làm lại, rồi chia cho số yêu cầu thành công. So theo loại yêu cầu và tính thêm chi phí cố định. [Bảng chi phí](bang_chi_phi.md)
- **B.** Đổi từng yếu tố chi phí, so giới hạn chạy lại và kiểm tra kịch bản xem lại 100%. [Bảng độ nhạy](bang_chi_phi.md#b1--đổi-từng-yếu-tố)
- **C.** Đối chiếu hai bộ nhãn độc lập và ghi cách phát hiện, xử lý cho năm loại lỗi. [Bảng lỗi](bang_loi.md)
- **D.** Tính cỡ mẫu theo yêu cầu, nhân viên và depot. Chọn chia ngẫu nhiên theo nhân viên, có đối chứng đồng thời và luật dừng. [Kế hoạch pilot](pilot_plan.yaml)
- **E.** Tính ba chỉ số chạy thử, đặc tả sự kiện và cách theo dõi rủi ro kinh tế. [Chỉ số](chi_so.md) · [Hồ sơ launch v0](ho_so_launch_v0.md)

## 4. Kết quả

Chi phí toàn mẫu là **4.472 đ/việc thành công** (simulated). Kịch bản xem lại 100% với 15,3 phút làm lại mỗi ca đạt **12.415 đ/việc** (simulated), vượt mức thủ công **12.000 đ**. Hai người gắn nhãn đồng thuận **20/20 ca**. Trong đợt chạy thử giả lập, **82,83%** yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày, **27,12%** ca được xem lại có quyết định sửa hoặc bỏ gợi ý, và **4,25%** yêu cầu mở lại trong 7 ngày.

Đề xuất **Go có điều kiện** cho pilot `noi_dia` và `hang_nang`. Kết quả duyệt chéo đang chờ hội đồng.

## 5. Khó khăn và cách xử lý

Với 20 nhân viên mỗi nhóm, cỡ mẫu hiệu dụng bị giới hạn dưới 1.000 mỗi nhóm. Pilot đặt mục tiêu phát hiện chênh lệch 6 điểm với ít nhất 299 yêu cầu đủ điều kiện mỗi người. Chỉ kết luận hiệu quả khi đủ mẫu và đủ thời gian theo dõi.

## 6. Tổng hợp đóng góp

Xem phần đóng góp và bằng chứng trong [TEAM.md](../../TEAM.md) và các báo cáo cá nhân.

## 7. Hạn chế và hướng cải thiện

Trace chạy thử là dữ liệu giả lập và thiếu nhóm đối chứng đồng thời. Pilot sẽ ghi thời gian xem lại, thời gian làm lại và các sự kiện ở cả hai nhánh. Nếu tác động thực là 5 điểm, lực thống kê dự kiến chỉ khoảng 64%.

## 8. Tài liệu tham khảo

[Đề bài Lab 13](../../docs/Ngay13_Lab13_De_bai_hoc_vien.md) · [Dữ liệu và công thức](../../docs/du_lieu_va_cong_thuc.md) · [Mã phân tích](../../src/lab13.py)
