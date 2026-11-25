# Bảng chi phí · Nhiệm vụ A và B

Số liệu được tính bằng `src/lab13.py`. Các kết quả sử dụng dữ liệu từ cột `_simulated` được ghi nhãn `simulated`.

## A1 · Ba phép thử đáp án biết trước

| Phép thử (p = 0,8) | Kết quả của nhóm |
| --- | ---: |
| Số lần chạy trung bình, tối đa 2 lần | 1,20 |
| Số lần chạy trung bình, chạy đến khi đúng | 1,25 |
| Hệ số chi phí mỗi việc thành công, tối đa 3 lần | 1,25 |

## A2 · Mô hình chi phí từ trace

| Khoản | Giá trị | Nguồn | Nhãn |
| --- | ---: | --- | --- |
| Token | 245.585,1 đ | `logix_runs.csv` | đo từ trace |
| Tool | 84.000 đ | `logix_runs.csv` | đo từ trace |
| Trong đó, phần của lần chạy thứ 2 và 3 | 93.804,5 đ | Chi phí token và tool của các lượt có `attempt > 1` | đo từ trace |
| Xem lại | 1.780.000 đ | `phut_xem_lai_simulated` | simulated |
| Làm lại | 2.264.000 đ | `phut_lam_lai_simulated` | simulated |
| Tổng chi phí | 4.373.585,1 đ | Token + tool + xem lại + làm lại | simulated |
| Số việc thành công | 978 yêu cầu | `ket_qua == 'thanh_cong'` | |
| Chi phí mỗi việc thành công | 4.472,0 đ/việc thành công | Tổng chi phí ÷ 978 | simulated |
| Hoá đơn token và tool chia cho số yêu cầu | 274,7 đ/yêu cầu | (Token + tool) ÷ 1.200 | đo từ trace |

- Chi phí mỗi việc thành công gấp **16,28 lần** hoá đơn token và tool trên mỗi yêu cầu (`simulated`).
- Chi phí làm lại chiếm tỉ trọng lớn nhất, **51,8%** tổng chi phí (`simulated`).
- Đối chiếu độc lập: cộng cột `tool_calls` trên toàn bộ lượt chạy trong CSV được **5.600 lượt gọi tool**. Nhân với 15 đ/lượt được **84.000 đ**, khớp với kết quả của `lab13.py`.

## A3 · Tách theo loại yêu cầu

| Loại | Số yêu cầu | Tỉ lệ thành công | Số lần chạy mỗi yêu cầu | Chi phí mỗi việc thành công (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: | ---: |
| `noi_dia` | 824 | 95,0% | 1,11 | 2.696 đ | 0,22× |
| `hang_nang` | 158 | 74,1% | 1,47 | 8.221 đ | 0,69× |
| `quoc_te` | 150 | 27,3% | 2,32 | 22.515 đ | 1,88× |
| `doi_tac` | 68 | 54,4% | 1,88 | 10.215 đ | 0,85× |

- Nên loại `quoc_te` khỏi phạm vi pilot vì chi phí là **22.515 đ/việc thành công**, gấp **1,88 lần** xử lý thủ công (`simulated`). Ở lần chạy thứ ba, chỉ **2,2%** trong 93 lượt trả về `ok`, nên lợi ích của lần thử thêm rất hạn chế.

## A4 · Chi phí cố định (phạm vi `noi_dia` + `hang_nang`)

| Khối lượng | Việc thành công mỗi tháng | Chi phí cố định mỗi việc | Chi phí mỗi việc thành công + cố định (simulated) | So với 12.000 đ (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 45.000 yêu cầu/tháng | 33.750 | 1.185 đ | 4.599 đ | 0,38× |
| 22.500 yêu cầu/tháng | 16.875 | 2.370 đ | 5.784 đ | 0,48× |

- Kết luận giữ nguyên ở cả hai mức khối lượng. Khi giảm từ **45.000** xuống **22.500 yêu cầu/tháng**, chi phí mỗi việc thành công tăng từ **4.599 đ** lên **5.784 đ** (`simulated`), vẫn dưới mức **12.000 đ** khi nhân viên tự xử lý.

## B1 · Đổi từng yếu tố

| Kịch bản | Cách tính | Chi phí mỗi việc thành công (simulated) | Thay đổi so với mức gốc (simulated) |
| --- | --- | ---: | ---: |
| Giá token gấp đôi | 52 đ/1.000 token đầu vào và 260 đ/1.000 token đầu ra; giữ nguyên giá tool | 4.723 đ | +5,6% |
| Giá token giảm một nửa | 13 đ/1.000 token đầu vào và 65 đ/1.000 token đầu ra; giữ nguyên giá tool | 4.346 đ | −2,8% |
| Tỉ lệ xem lại gấp đôi | Tiền xem lại × 2 | 6.292 đ | +40,7% |
| Tỉ lệ xem lại giảm một nửa | Tiền xem lại ÷ 2 | 3.562 đ | −20,3% |
| Số ca làm lại gấp đôi | Tiền làm lại × 2 | 6.787 đ | +51,8% |
| Số ca làm lại giảm một nửa | Tiền làm lại ÷ 2 | 3.315 đ | −25,9% |
| Lương nhân viên tăng 25% | 2.500 đ/phút | 5.506 đ | +23,1% |
| Chỉ cho chạy tối đa 2 lần | Bỏ lượt có `attempt > 2`; chuyển yêu cầu có `so_lan_chay > 2` cho nhân viên | 4.237 đ | −5,2% |
| Chỉ cho chạy 1 lần | Bỏ lượt có `attempt > 1`; chuyển yêu cầu có `so_lan_chay > 1` cho nhân viên | 4.111 đ | −8,1% |

## B2 · Đổi một cặp và xếp hạng

- Khi giá token và tỉ lệ xem lại cùng gấp đôi, chi phí đạt **6.543 đ/việc thành công**, tăng **46,3%** so với mức gốc (`simulated`). Hai khoản chi phí thay đổi độc lập nên mức tăng cộng lại: **5,6% + 40,7% = 46,3%** theo số đã làm tròn.
- Ba kịch bản có tác động lớn nhất: **(1)** số ca làm lại gấp đôi (**+51,8%**), **(2)** tỉ lệ xem lại gấp đôi (**+40,7%**), **(3)** lương nhân viên tăng 25% (**+23,1%**) (`simulated`).

## B3 · Giới hạn chạy lại có thật sự rẻ hơn

| Giới hạn | Tổng chi phí trợ lý (simulated) | Số yêu cầu không thành công | Chi phí cả hệ thống (simulated) | Chi phí mỗi việc thành công (simulated) |
| --- | ---: | ---: | ---: | ---: |
| 1 lần | 3.621.781 đ | 319 | 7.449.781 đ | 4.111 đ |
| 2 lần | 4.093.220 đ | 234 | 6.901.220 đ | 4.237 đ |
| 3 lần | 4.373.585 đ | 222 | 7.037.585 đ | 4.472 đ |

- Giới hạn **2 lần** cho tổng chi phí hệ thống thấp nhất (**6.901.220 đ**), còn giới hạn **1 lần** cho chi phí trợ lý mỗi việc thành công thấp nhất (**4.111 đ**) (`simulated`). Chi phí hệ thống tính thêm **12.000 đ** xử lý thủ công cho mỗi yêu cầu trợ lý chưa giải quyết thành công.

## B4 · Nếu phải xem lại tất cả

- Với `noi_dia` + `hang_nang`, kịch bản xem lại 100% tính **948 ca × 5 phút**, trong đó có **48 ca làm lại**. Nếu mỗi ca làm lại mất **9 phút**, chi phí là **11.743 đ/việc thành công** (**0,98×** mức thủ công). Nếu mất **15,3 phút**, chi phí tăng lên **12.415 đ** (**1,03×**) (`simulated`).
- Pilot cần đo thời gian xem lại, tỉ lệ ca phải làm lại và thời gian làm lại thực tế. Thời gian xem lại hoà vốn giảm từ **5,12** xuống **4,80 phút/ca** khi thời gian làm lại tăng từ **9** lên **15,3 phút/ca** (`simulated`).