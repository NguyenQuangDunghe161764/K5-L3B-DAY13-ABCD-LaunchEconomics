# Team

## Thông tin nhóm

- Tên nhóm: ABCD
- Lớp: L3B
- Repo nhóm: `K5-L3B-DAY13-ABCD-LaunchEconomics` (xem [SUBMISSION.md](SUBMISSION.md))
- URL repo: [K5-L3B-DAY13-ABCD-LaunchEconomics](https://github.com/NguyenQuangDunghe161764/K5-L3B-DAY13-ABCD-LaunchEconomics)
- Nhánh nộp: `main`
- Commit chốt bản nộp: [`9ba9d08`](https://github.com/NguyenQuangDunghe161764/K5-L3B-DAY13-ABCD-LaunchEconomics/commit/9ba9d084a93ea18dc90960c774857ace000bf5ef).

## Thành viên

| STT | Họ tên | MSSV | Email | GitHub | Vai trò |
| --: | ------ | ---- | ----- | ------ | ------- |
|   1 | Nguyen Quang Dung | 2A202604031 | dunghamhaha@gmail.com | NguyenQuangDunghe161764 | Người viết code |
|   2 | Nguyễn Văn Lên | 2A202604007 | nguyenvanlen24122004@gmail.com | len2412 | Người gắn nhãn 1 |
|   3 | Đặng Nguyễn Nhật Minh | 2A202604118 | 26ai.minhdnn@vinuni.edu.vn | MN-HD | Người kiểm số |
|   4 | Triệu Tuấn Minh | 2A202604123 | trieutuanminh004@gmail.com | ttm4623 | Người gắn nhãn 2, kiêm giữ hồ sơ |

Bốn vai của lab:

- **Người viết code:** viết và chạy `src/lab13.py`.
- **Người kiểm số:** tính tay một con số để đối chiếu, điền bảng.
- **Người gắn nhãn 1:** đọc đề, theo dõi điều kiện "Xong khi"; gắn nhãn 20 ca độc lập ở CP3.
- **Người gắn nhãn 2, kiêm giữ hồ sơ:** điền `report/team/ho_so_launch_v0.md` từ đầu buổi; gắn nhãn 20 ca độc lập ở CP3.

Đổi người viết code sau giờ giải lao, để ít nhất hai người trong nhóm tự tay tính được chi phí.

## Cá nhân

- [Nguyen Quang Dung](report/team/2A202604031_NguyenQuangDung.md)
- [Nguyễn Văn Lên](report/team/2A202604007_NguyenVanLen.md)
- [Đặng Nguyễn Nhật Minh](report/team/2A202604118_DangNguyenNhatMinh.md)
- [Triệu Tuấn Minh](report/team/2A202604123_TrieuTuanMinh.md)

## Nguyen Quang Dung — 2A202604031

### Phần việc phụ trách

- Người viết code cho nhiệm vụ A, B và D1 trong `src/lab13.py`.

### Đóng góp cụ thể

- Triển khai mô hình chi phí, bảng độ nhạy và phép tính cỡ mẫu pilot với sự hỗ trợ của Codex.
- Hoàn thiện kế hoạch pilot và tính tỷ lệ mở lại theo phạm vi ở CP4. Tổng hợp đặc tả chỉ số và báo cáo nhóm ở CP5.

### Bằng chứng

- Commit `823fafb` cho code phân tích, `6dbcd65` cho CP4 và `2c3495d` cho CP5. `python lab13.py` chạy hết và cả ba phép thử A1 đều đạt.

## Nguyễn Văn Lên — 2A202604007

### Phần việc phụ trách

- Được phân công người gắn nhãn 1 cho nhiệm vụ C: đọc đề, theo dõi điều kiện hoàn thành và tham gia phân loại 20 ca lỗi.

### Đóng góp cụ thể

- Ghi bộ nhãn người 1 và kết quả so sánh được báo cáo là 20/20 ca trùng trong `report/team/bang_loi.md`.
- Các nhãn ban đầu và đề xuất khắc phục đã được soạn với hỗ trợ định nghĩa và giải thích của Copilot

### Bằng chứng

- `report/team/bang_loi.md` (bộ nhãn người 1, kết quả đồng thuận và bảng khắc phục).

## Đặng Nguyễn Nhật Minh — 2A202604118

### Phần việc phụ trách

- Người kiểm số cho nhiệm vụ A và B.

### Đóng góp cụ thể

- Chạy ba phép thử A1 và đối chiếu các kết quả 1,20 · 1,25 · 1,25.
- Kiểm tra độc lập chi phí gọi tool từ CSV: 5.600 lượt × 15 đ/lượt = 84.000 đ, khớp với kết quả của `lab13.py`.
- Điền bảng chi phí A1–A4 và phân tích độ nhạy B1–B4 từ kết quả chạy của nhóm.

### Bằng chứng

- `report/team/bang_chi_phi.md`, commit `042f972`.

## Triệu Tuấn Minh — 2A202604123

### Phần việc phụ trách

- Người gắn nhãn 2 ở CP3, kiêm giữ hồ sơ launch từ CP1 đến CP5.

### Đóng góp cụ thể

- Gắn nhãn độc lập 20 ca lỗi. Khi đối chiếu với người gắn nhãn 1, hai bộ nhãn trùng 20/20 ca. Tham gia hoàn thiện bảng khắc phục cho năm loại lỗi.
- Tổng hợp bằng chứng và cập nhật hồ sơ launch về cỡ mẫu, rollout, luật dừng, chỉ số và các điều kiện trước pilot.

### Bằng chứng

- [Bảng lỗi CP3](report/team/bang_loi.md) · [Hồ sơ launch v0](report/team/ho_so_launch_v0.md) · [Báo cáo cá nhân](report/team/2A202604123_TrieuTuanMinh.md)
- Commit `7fd4ab5` và `7b9577d` cho CP4, `4a834cd` cho CP5.
