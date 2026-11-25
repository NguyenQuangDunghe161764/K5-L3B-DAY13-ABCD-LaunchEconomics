# Phiếu chấm hội đồng Gate 2a

Nhóm số n chấm nhóm số n + 1; nhóm cuối chấm nhóm 1. Chấm theo bằng chứng trong hồ sơ, không theo cách trình bày: một đề xuất No-go có lý do bằng số được điểm cao hơn một đề xuất Go bỏ qua con số bất lợi.

- Nhóm chấm (hội đồng): Coffee
- Nhóm được chấm: ABCD · L3B

Trạng thái: Đã ghi nhận điểm và phản hồi duyệt chéo của Coffee. Quyết định của hội đồng chờ xác nhận.

| Tiêu chí | 0 điểm | 5 điểm | 10 điểm | Điểm | Lý do (có số) |
| --- | --- | --- | --- | ---: | --- |
| Đề xuất khớp bằng chứng | Mâu thuẫn với số của chính nhóm | Khớp nhưng bỏ qua một con số bất lợi | Khớp, nêu cả con số bất lợi và cách xử lý | **10** | Đề xuất Go có điều kiện phù hợp với chi phí giả lập trong phạm vi pilot: 2.696 đ/việc thành công cho nội địa và 8.221 đ cho hàng nặng, đều dưới mức tham chiếu thủ công 12.000 đ. Nhóm nêu hai bất lợi: lực thống kê khoảng 64% ở mức chênh 5 điểm phần trăm và chi phí lên 12.415 đ/việc thành công khi xem lại 100%. Kế hoạch ghi trước luật dừng khi chi phí biến đổi vượt 8.000 đ/việc thành công trong hai tuần liên tiếp và giữ nguyên mức rollout nếu tuần đầu đã vượt. |
| Số giả lập và phạm vi | Không nhãn; phạm vi "mọi yêu cầu" | Có nhãn hoặc có thu hẹp phạm vi | Nhãn ở mọi số giả lập; phạm vi thu hẹp có lý do bằng số | **10** | Phạm vi thu hẹp về nội địa và hàng nặng dựa trên chi phí 2.696 đ và 8.221 đ mỗi việc thành công, đều dưới mức tham chiếu 12.000 đ. Nhóm ghi rõ dữ liệu là giả lập và giải thích 2.696 đ là chi phí của toàn bộ 824 yêu cầu nội địa, kể cả lượt chạy lỗi, chia cho 783 việc thành công. |
| Pilot ra được quyết định | Không đối chứng hoặc thiếu cỡ mẫu | Đủ cỡ mẫu, luật dừng chung chung | Tách được tác động, đủ mẫu, luật dừng có ngưỡng, thời hạn, người có quyền dừng | **10** | Chia ngẫu nhiên theo nhân viên với 20 người mỗi nhánh, phân tầng theo depot và đối chứng cùng kỳ. Với 299 yêu cầu đủ điều kiện mỗi người, mỗi nhánh có khoảng 859 mẫu hiệu dụng, đạt lực thống kê 80% ở mức chênh 6 điểm phần trăm. Luật chi phí đã viết trước, có ngưỡng 8.000 đ/việc thành công, thời hạn hai tuần liên tiếp và người hành động là quản lý sản phẩm trợ lý. |
| **Tổng** | | | | **30 / 30** | |

**Quyết định của hội đồng:** Chờ Coffee xác nhận.

## Hỏi đáp và nhận xét của Coffee

### 1. Chi phí nội địa 2.696 đ chia cho số nào?

**ABCD trả lời.** Chi phí 2.696 đ được tính bằng chi phí token, công cụ, xem lại và làm lại của toàn bộ 824 yêu cầu nội địa, kể cả lượt chạy lỗi, chia cho 783 yêu cầu thành công.

**Coffee nhận xét.** Mẫu số và cách tính đã rõ. Để so cùng đơn vị với mức thủ công 12.000 đ/yêu cầu, cộng chi phí xử lý thay cho 41 ca chưa thành công rồi chia cho toàn bộ 824 yêu cầu nội địa.

### 2. Vì sao chia theo nhân viên?

**ABCD trả lời.** Bốc thăm từng yêu cầu có thể khiến cùng một nhân viên mang cách làm từ ca dùng trợ lý sang ca đối chứng. Nhóm bốc thăm theo nhân viên, phân tầng theo depot. Với 20 người mỗi nhánh và 299 yêu cầu đủ điều kiện mỗi người, lực thống kê là 80% ở mức chênh 6 điểm phần trăm và khoảng 64% ở mức 5 điểm.

**Coffee nhận xét.** Lý do và đánh đổi cỡ mẫu đã rõ. Khi trình bày, nên nêu cụ thể cách hạn chế dùng chéo trong cùng depot bằng việc khóa quyền theo tài khoản và ghi log lượt mở trợ lý theo nhân viên.

### 3. Nếu phải xem lại 100%, khi nào dừng?

**ABCD trả lời.** Kịch bản giả lập xem lại 100% và làm lại 15,3 phút/ca cho chi phí 12.415 đ/việc thành công. Kế hoạch đã ghi trước rằng nếu chi phí biến đổi vượt 8.000 đ/việc thành công trong hai tuần liên tiếp, quản lý sản phẩm sẽ dừng thu mẫu chính, giới hạn phạm vi về nội địa và cho chạy tối đa hai lượt.

**Coffee nhận xét.** Luật đã có ngưỡng, thời hạn và người chịu trách nhiệm. Coffee đề nghị cân nhắc thêm điều kiện tăng rollout dựa trên số phút xem lại đo được, chẳng hạn dưới khoảng 5 phút mỗi lượt xem lại. Mốc này đang ở dạng đề xuất. Ngưỡng vận hành đã chốt nằm trong [kế hoạch pilot](pilot_plan.yaml).
