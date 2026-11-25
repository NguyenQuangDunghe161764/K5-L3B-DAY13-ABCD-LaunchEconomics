# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | Đóng trong 24 giờ và không mở lại trong 7 ngày | Số yêu cầu có `dong_trong_24h = 1` và `mo_lai_trong_7_ngay = 0` chia tổng số yêu cầu | 994/1.200 = **82,83%** |
| Dùng | Tỉ lệ bỏ qua hoặc sửa gợi ý | Số yêu cầu đã xem lại với `quyet_dinh_xem_lai` là `sua` hoặc `bo` chia số yêu cầu có `duoc_xem_lai = 1` | (41 + 7)/177 = **27,12%** |
| An toàn | Tỉ lệ mở lại trong 7 ngày | Số yêu cầu có `mo_lai_trong_7_ngay = 1` chia tổng số yêu cầu | 51/1.200 = **4,25%** |
| Dùng | Tỉ lệ yêu cầu được mở trợ lý | Số yêu cầu đủ điều kiện trong nhánh trợ lý có ít nhất một lần mở trợ lý chia tổng số yêu cầu đủ điều kiện được gán vào nhánh này | Không cần tính |
| An toàn | Tỉ lệ yêu cầu hoàn sai tiền qua kiểm tra mẫu | Số yêu cầu được kiểm tra có tổng tiền hoàn thực tế khác số đúng chia tổng số yêu cầu đã kiểm tra trong tuần | Không cần tính |

Ba kết quả trên là số liệu mô tả đợt chạy thử giả lập, tính bằng cách đếm trực tiếp các dòng trong `src/logix_requests.csv`. Đợt chạy thử thiếu đối chứng đồng thời.

## Danh sách event

Hệ thống ticket tạo `trace_id` khi nhận yêu cầu và truyền sang các dịch vụ liên quan, kể cả nhánh đối chứng. Đếm theo `request_id` để một yêu cầu chạy lại nhiều lần vẫn chỉ được tính một lần.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Hệ thống ticket | `request_id`, `trace_id`, `created_at`, `staff_id`, `depot`, `loai`, `arm`, `eligible`, `rollout_step` | Khi tiếp nhận và phân tuyến |
| `assistant_opened` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `opened_at` | Khi nhân viên mở trợ lý cho yêu cầu |
| `agent_run_completed` | Trợ lý | `request_id`, `trace_id`, `attempt`, `status`, `tokens_in`, `tokens_out`, `tool_calls` | Sau mỗi lần chạy, kể cả lỗi |
| `staff_review_decision` | Giao diện CSKH | `request_id`, `trace_id`, `staff_id`, `decision` (giu/sua/bo), `review_minutes`, `decided_at` | Khi nhân viên chốt xử lý gợi ý |
| `staff_rework_completed` | Giao diện CSKH | `request_id`, `trace_id`, `rework_minutes`, `reason`, `completed_at` | Khi nhân viên hoàn tất làm lại |
| `refund_ledger_write` | Dịch vụ sổ cái | `request_id`, `trace_id`, `idempotency_key`, `amount_vnd`, `status`, `recorded_at` | Khi ghi nhận kết quả lệnh hoàn |
| `ticket_closed` | Hệ thống ticket | `request_id`, `trace_id`, `closed_at` | Khi đóng yêu cầu |
| `ticket_reopened` | Hệ thống ticket | `request_id`, `trace_id`, `reopened_at`, `reason` | Khi yêu cầu được mở lại |
| `refund_audit_completed` | Kế toán | `request_id`, `trace_id`, `actual_total_vnd`, `expected_total_vnd`, `audited_at` | Sau khi đối soát từng yêu cầu trong mẫu tuần |

**Event dùng để tính từng chỉ số**

- **Chính.** Nối `refund_request_created`, `ticket_closed` và `ticket_reopened`. Lấy lần đóng đầu tiên, so với thời điểm nhận yêu cầu và kiểm tra mở lại trong 7 ngày kể từ lần đóng. Phân tích theo nhánh đã gán và chờ đủ thời gian quan sát.
- **Bỏ qua hoặc sửa.** Dùng `staff_review_decision`, lấy quyết định cuối của từng yêu cầu đã xem lại trong cửa sổ báo cáo. Dùng cùng mẫu số cho luật dừng sử dụng của CP4.
- **Mở lại.** Nối `refund_request_created`, `ticket_closed` và `ticket_reopened`; đếm yêu cầu có lần mở lại trong 7 ngày kể từ lần đóng đầu tiên. Chỉ so sánh các kỳ đã đủ thời gian theo dõi.
- **Mở trợ lý.** Nối `assistant_opened` với `refund_request_created`, lọc yêu cầu đủ điều kiện theo nhánh đã gán.
- **Hoàn sai tiền.** Dùng `refund_audit_completed`, so sánh hai số tiền trên từng yêu cầu trong mẫu kiểm tra tuần.

## E2 · Rủi ro kinh tế

Tác động dưới đây lấy từ [bảng độ nhạy](bang_chi_phi.md). Các ngưỡng theo dõi là ngưỡng đề xuất cho pilot.

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | B1: **+51,8%**, lên **6.787 đ/việc thành công** (simulated) | Tỉ lệ yêu cầu có làm lại vượt 7% trong tuần | Rà trace và thời gian làm lại theo loại yêu cầu. Áp dụng quy tắc thu hẹp của CP4 nếu chi phí vượt 8.000 đ trong hai tuần liên tiếp | PM trợ lý hoàn phí |
| Phải xem lại mọi gợi ý | B4: **11.743 đ/việc** nếu làm lại 9 phút/ca và **12.415 đ/việc** nếu mất 15,3 phút/ca (simulated); mức thủ công **12.000 đ** | Tỉ lệ xem lại, phút xem lại và phút làm lại mỗi tuần. Ở kịch bản 15,3 phút, xem lại quá **4,80 phút/ca** vượt mức hòa vốn (simulated) | Đo thời gian thực từ tuần đầu. Chỉ giảm xem lại cho nhóm ca đủ điều kiện sau khi đối soát và xác nhận đạt ngưỡng an toàn | Trưởng nhóm CSKH |
