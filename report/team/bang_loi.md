# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: Nguyễn Văn Lên · Người gắn nhãn 2: Triệu Tuấn Minh (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Do người dùng | Có | Do người dùng |
| 2 | Hệ thống | Hệ thống | Có | Hệ thống |
| 3 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 4 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 5 | Ngầm | Ngầm | Có | Ngầm |
| 6 | Do người dùng | Do người dùng | Có | Do người dùng |
| 7 | Hệ thống | Hệ thống | Có | Hệ thống |
| 8 | Hệ thống | Hệ thống | Có | Hệ thống |
| 9 | Do người dùng | Do người dùng | Có | Do người dùng |
| 10 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 11 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 12 | Ngầm | Ngầm | Có | Ngầm |
| 13 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 14 | Do người dùng | Do người dùng | Có | Do người dùng |
| 15 | Hệ thống | Hệ thống | Có | Hệ thống |
| 16 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 17 | Ngầm | Ngầm | Có | Ngầm |
| 18 | Ngữ cảnh | Ngữ cảnh | Có | Ngữ cảnh |
| 19 | Giới hạn hệ thống | Giới hạn hệ thống | Có | Giới hạn hệ thống |
| 20 | Hệ thống | Hệ thống | Có | Hệ thống |

**Tỉ lệ đồng thuận:** 20 / 20 = 100%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- Không có ca không trùng; hai người thống nhất cả 20/20 nhãn (100%), nên không cần bổ sung quy tắc phân biệt hay viết lại định nghĩa.

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Theo dõi event `refund_request_submitted` có `account_validation_failed`; cảnh báo nếu có từ 5 lần nhập sai trong một ngày. | Kiểm tra định dạng và độ dài tài khoản trước khi tạo lệnh; hướng dẫn khách sửa hoặc chuyển nhân viên, không gửi lệnh khi dữ liệu không hợp lệ. | Người viết code |
| 7 | Hệ thống | Đối chiếu event `refund_status_sent` với kết quả ghi sổ cái; cảnh báo ngay khi có thông báo thành công nhưng ghi sổ thất bại (ngưỡng: lớn hơn 0). | Chỉ báo thành công sau khi sổ cái xác nhận; nếu thất bại thì báo đang xử lý/chuyển nhân viên và không tự xác nhận hoàn tất. | Người viết code |
| 3 | Ngữ cảnh | Theo dõi event `refund_reopened` gắn với phương thức hoàn tiền; rà soát hàng tuần nếu từ 5% yêu cầu hoàn về ví bị mở lại vì khách chờ tiền vào ngân hàng. | Nêu rõ tiền được hoàn về ví và thời gian dự kiến ngay trước khi khách xác nhận; cung cấp hướng dẫn nếu khách cần hoàn về ngân hàng. | Người gắn nhãn 2, kiêm giữ hồ sơ |
| 4 | Giới hạn hệ thống | Theo dõi event `unsupported_route_handoff`; kiểm tra hàng tuần để bảo đảm 100% ca thiếu dữ liệu được thông báo giới hạn và chuyển nhân viên. | Không suy đoán trạng thái; thông báo thiếu dữ liệu và chuyển nhân viên kèm thông tin đã tra cứu. | Người viết code |
| 5 | Ngầm | Hàng tuần lấy mẫu các đơn có mã giảm giá, đối chiếu tiền hoàn với giá sau giảm; cảnh báo nếu phát hiện từ 1 đơn sai. | Sửa quy tắc tính tiền theo giá thực trả; kiểm tra lại các đơn liên quan và ghi nhận/chủ động xử lý khoản hoàn thừa. | Người kiểm số |
