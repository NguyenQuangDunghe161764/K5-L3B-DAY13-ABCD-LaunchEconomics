"""Lab 13 · Chạy python lab13.py để in kết quả A, B và D1."""
import csv
import math
import sys
from pathlib import Path
from statistics import NormalDist, mean

GIA_VAO = 26
GIA_RA = 130
GIA_TOOL = 15
LUONG_PHUT = 2000
BASELINE = 12000
PHAM_VI_PILOT = {"noi_dia", "hang_nang"}
THU_MUC = Path(__file__).resolve().parent


def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình với xác suất thành công p mỗi lần."""
    if p == 0:
        return math.inf if k is None else k
    return ti_le_thanh_cong(p, k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất thành công trong tối đa k lần, hoặc sau khi chạy đến khi đúng."""
    return float(p > 0) if k is None else 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công theo bội số giá một lần chạy."""
    thanh_cong = ti_le_thanh_cong(p, k)
    return so_lan_chay_ky_vong(p, k) / thanh_cong if thanh_cong else math.inf


def kiem_tra_dap_an_biet_truoc():
    assert math.isclose(so_lan_chay_ky_vong(0.8, 2), 1.20)
    assert math.isclose(so_lan_chay_ky_vong(0.8), 1.25)
    assert math.isclose(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3), 1.25)
    print("Ba phép thử đáp án biết trước: ĐẠT")


def doc_csv(ten):
    with (THU_MUC / ten).open(encoding="utf-8-sig", newline="") as tep:
        return list(csv.DictReader(tep))


def mo_hinh(runs, reqs, gia_vao=GIA_VAO, gia_ra=GIA_RA, gia_tool=GIA_TOOL,
            luong_phut=LUONG_PHUT, he_so_xem_lai=1.0, he_so_lam_lai=1.0,
            max_lan_chay=None):
    """Tính chi phí từ trace và phút giả lập cho phạm vi yêu cầu đã chọn."""
    ma_yeu_cau = {yc["request_id"] for yc in reqs}
    token = tool = chay_lai = 0
    for run in runs:
        lan = int(run["attempt"])
        if run["request_id"] not in ma_yeu_cau:
            continue
        if max_lan_chay is not None and lan > max_lan_chay:
            continue
        tien_token = (int(run["tokens_in"]) * gia_vao + int(run["tokens_out"]) * gia_ra) / 1000
        tien_tool = int(run["tool_calls"]) * gia_tool
        token += tien_token
        tool += tien_tool
        if lan > 1:
            chay_lai += tien_token + tien_tool

    # Ca vượt giới hạn được chuyển cho nhân viên. B3 cộng chi phí xử lý các ca này.
    da_xu_ly = [
        yc for yc in reqs
        if max_lan_chay is None or int(yc["so_lan_chay"]) <= max_lan_chay
    ]
    xem_lai = sum(float(yc["phut_xem_lai_simulated"]) for yc in da_xu_ly) * luong_phut * he_so_xem_lai
    lam_lai = sum(float(yc["phut_lam_lai_simulated"]) for yc in da_xu_ly) * luong_phut * he_so_lam_lai
    thanh_cong = sum(yc["ket_qua"] == "thanh_cong" for yc in da_xu_ly)
    tong = token + tool + xem_lai + lam_lai
    return dict(
        token=token, tool=tool, chay_lai=chay_lai, xem_lai=xem_lai,
        lam_lai=lam_lai, tong=tong, thanh_cong=thanh_cong,
        cps=tong / thanh_cong if thanh_cong else math.inf,
        hoa_don_moi_yc=(token + tool) / len(reqs) if reqs else math.nan,
    )


def in_chi_phi(runs, reqs, goc, pilot):
    print("\nA2 · Chi phí (đồng)")
    don_vi = {"thanh_cong": "yêu cầu", "hoa_don_moi_yc": "đ/yêu cầu", "cps": "đ/việc thành công"}
    for ten, gia_tri in goc.items():
        nhan = " [simulated]" if ten in {"xem_lai", "lam_lai", "tong", "cps"} else ""
        print(f"{ten:18s} {gia_tri:>14,.1f} {don_vi.get(ten, 'đ')}{nhan}")
    print(f"CPS / hóa đơn mỗi yêu cầu: {goc['cps'] / goc['hoa_don_moi_yc']:.2f}× [simulated]")
    print(f"Làm lại chiếm {goc['lam_lai'] / goc['tong']:.1%} tổng chi phí [simulated]")
    he_thong = goc["tong"] + (len(reqs) - goc["thanh_cong"]) * BASELINE
    print(f"Chi phí cả hệ thống: {he_thong / len(reqs):,.0f} đ/yêu cầu [simulated]")

    print("\nA3 · Loại | Yêu cầu | Thành công | Lần/yêu cầu | CPS [simulated] | CPS/12.000")
    for loai in sorted({yc["loai"] for yc in reqs}):
        nhom = [yc for yc in reqs if yc["loai"] == loai]
        kq = mo_hinh(runs, nhom)
        so_lan = mean(int(yc["so_lan_chay"]) for yc in nhom)
        print(f"{loai:9s} {len(nhom):4d} {kq['thanh_cong'] / len(nhom):8.1%} "
              f"{so_lan:6.2f} {kq['cps']:10,.0f} {kq['cps'] / BASELINE:6.2f}×")
        ma_nhom = {yc["request_id"] for yc in nhom}
        for lan in range(1, 4):
            cac_lan = [r for r in runs if r["request_id"] in ma_nhom and int(r["attempt"]) == lan]
            if cac_lan:
                ti_le_ok = mean(r["status"] == "ok" for r in cac_lan)
                print(f"  Lần {lan}: {ti_le_ok:.1%} ok (n={len(cac_lan)})")

    kq = mo_hinh(runs, pilot)
    print("\nA4 · Chi phí cố định 40 triệu đ/tháng")
    for luong_thang in (45000, 22500):
        thanh_cong = luong_thang * kq["thanh_cong"] / len(reqs)
        co_dinh = 40000000 / thanh_cong
        cps = kq["cps"] + co_dinh
        print(f"{luong_thang:,} yêu cầu/tháng → {thanh_cong:,.0f} việc thành công trong phạm vi, "
              f"cố định {co_dinh:,.0f} đ/việc, CPS {cps:,.0f} đ ({cps / BASELINE:.2f}×) [simulated]")


def in_do_nhay(runs, reqs, goc, pilot):
    kich_ban = {
        "Giá token gấp đôi": dict(gia_vao=2 * GIA_VAO, gia_ra=2 * GIA_RA),
        "Giá token giảm một nửa": dict(gia_vao=GIA_VAO / 2, gia_ra=GIA_RA / 2),
        "Xem lại gấp đôi": dict(he_so_xem_lai=2),
        "Xem lại giảm một nửa": dict(he_so_xem_lai=0.5),
        "Làm lại gấp đôi": dict(he_so_lam_lai=2),
        "Làm lại giảm một nửa": dict(he_so_lam_lai=0.5),
        "Lương tăng 25%": dict(luong_phut=1.25 * LUONG_PHUT),
        "Tối đa 2 lần chạy": dict(max_lan_chay=2),
        "Chỉ 1 lần chạy": dict(max_lan_chay=1),
    }
    print("\nB1 · Kịch bản | CPS [simulated] | Thay đổi so với gốc")
    chenh_lech = {}
    for ten, tham_so in kich_ban.items():
        cps = mo_hinh(runs, reqs, **tham_so)["cps"]
        chenh_lech[ten] = cps / goc["cps"] - 1
        print(f"{ten:25s} {cps:10,.0f} {chenh_lech[ten]:+8.1%}")

    doi_cap = mo_hinh(runs, reqs, **kich_ban["Giá token gấp đôi"], he_so_xem_lai=2)
    print(f"\nB2 · Giá token và xem lại gấp đôi: {doi_cap['cps']:,.0f} đ "
          f"({doi_cap['cps'] / goc['cps'] - 1:+.1%}) [simulated]")
    yeu_to = {ten: abs(chenh_lech[ten]) for ten in (
        "Giá token gấp đôi", "Xem lại gấp đôi", "Làm lại gấp đôi", "Lương tăng 25%",
    )}
    xep_hang = sorted(yeu_to, key=yeu_to.get, reverse=True)[:3]
    print("Ba yếu tố tác động nhiều nhất: " + " > ".join(xep_hang) + " [simulated]")

    print("\nB3 · Giới hạn | Tổng trợ lý | Số ca không thành công | Tổng hệ thống | CPS [simulated]")
    tong_he_thong = {}
    cps_moi_muc = {}
    for lan in range(1, 4):
        kq = mo_hinh(runs, reqs, max_lan_chay=lan)
        con_lai = len(reqs) - kq["thanh_cong"]
        tong_he_thong[lan] = kq["tong"] + con_lai * BASELINE
        cps_moi_muc[lan] = kq["cps"]
        print(f"{lan:2d} {kq['tong']:14,.0f} {con_lai:10d} {tong_he_thong[lan]:14,.0f} {kq['cps']:10,.0f}")
    print(f"Hệ thống rẻ nhất: {min(tong_he_thong, key=tong_he_thong.get)} lần. "
          f"CPS thấp nhất: {min(cps_moi_muc, key=cps_moi_muc.get)} lần [simulated].")

    kq = mo_hinh(runs, pilot)
    ma_pilot = {yc["request_id"] for yc in pilot}
    so_ca_xem = len({r["request_id"] for r in runs if r["request_id"] in ma_pilot and r["status"] == "ok"})
    so_ca_lam_lai = sum(yc["ket_qua"] == "lam_lai" for yc in pilot)
    # Kịch bản thay thế dùng phút trung bình của toàn bộ ca làm lại, làm tròn 1 chữ số.
    phut_quan_sat = round(mean(float(yc["phut_lam_lai_simulated"]) for yc in reqs
                              if yc["ket_qua"] == "lam_lai"), 1)
    hoa_don = kq["token"] + kq["tool"]
    print(f"\nB4 · Xem lại 100%: {so_ca_xem} ca × 5 phút, {so_ca_lam_lai} ca làm lại")
    for phut in (9, phut_quan_sat):
        chi_phi_khac = hoa_don + so_ca_lam_lai * phut * LUONG_PHUT
        cps = (chi_phi_khac + so_ca_xem * 5 * LUONG_PHUT) / kq["thanh_cong"]
        hoa_von = (kq["thanh_cong"] * BASELINE - chi_phi_khac) / (so_ca_xem * LUONG_PHUT)
        print(f"{phut:g} phút làm lại: CPS {cps:,.0f} đ ({cps / BASELINE:.2f}×), "
              f"hòa vốn ở {hoa_von:.2f} phút xem lại/ca [simulated]")


def co_mau(p1, p2, alpha=0.05, power=0.8):
    """Cỡ mẫu mỗi nhánh cho kiểm định hai phía so sánh hai tỷ lệ."""
    phan_phoi = NormalDist()
    z_alpha = phan_phoi.inv_cdf(1 - alpha / 2)
    z_power = phan_phoi.inv_cdf(power)
    p_gop = (p1 + p2) / 2
    sai_so_gop = math.sqrt(2 * p_gop * (1 - p_gop))
    sai_so_rieng = math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))
    return math.ceil(((z_alpha * sai_so_gop + z_power * sai_so_rieng) / (p2 - p1)) ** 2)


def in_co_mau():
    icc, nhan_vien, depot, m = 0.02, 20, 6, 75
    n_5 = co_mau(0.70, 0.75)
    n_6 = co_mau(0.70, 0.76)
    he_so = 1 + (m - 1) * icc
    n_cum = math.ceil(n_5 * he_so)
    m_toi_thieu = math.ceil(n_6 * (1 - icc) / (nhan_vien - n_6 * icc))

    print("\nD1 · Cỡ mẫu mỗi nhóm (alpha 0,05; power 0,8; ICC 0,02)")
    print(f"a. Chia theo yêu cầu (+5 điểm): {n_5:,} yêu cầu")
    print(f"b. Chia theo nhân viên ({m} yêu cầu/người): DE={he_so:.2f}, "
          f"{n_cum:,} yêu cầu, {math.ceil(n_cum / m)} người/nhóm")
    print(f"c. {nhan_vien} nhân viên/nhóm: cận trên {nhan_vien / icc:,.0f} yêu cầu hiệu dụng")
    print(f"d. {depot} depot/nhóm: cận trên {depot / icc:,.0f} yêu cầu hiệu dụng")
    print(f"e. +6 điểm: {n_6} yêu cầu hiệu dụng/nhóm, cần ít nhất {m_toi_thieu} yêu cầu/người "
          f"(DE={1 + (m_toi_thieu - 1) * icc:.2f})")


if __name__ == "__main__":
    # Gi? ti?ng Vi?t khi chuy?n ??u ra qua pipe ho?c ghi v?o file tr?n Windows.
    sys.stdout.reconfigure(encoding="utf-8")
    kiem_tra_dap_an_biet_truoc()
    runs = doc_csv("logix_runs.csv")
    reqs = doc_csv("logix_requests.csv")
    goc = mo_hinh(runs, reqs)
    pilot = [yc for yc in reqs if yc["loai"] in PHAM_VI_PILOT]
    in_chi_phi(runs, reqs, goc, pilot)
    in_do_nhay(runs, reqs, goc, pilot)
    in_co_mau()
