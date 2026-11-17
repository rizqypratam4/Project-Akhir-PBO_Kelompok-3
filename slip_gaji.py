TARIF_BPJS_PERSEN = 3

NAMA_BULAN = ["Januari", "Februari", "Maret", "April", "Mei", "Juni",
              "Juli", "Agustus", "September", "Oktober", "November", "Desember"]


def format_rupiah(nilai):
    return "Rp" + f"{nilai:,}".replace(",", ".")


class SlipGaji:
    def __init__(self, kode, karyawan, presensi, bulan, tahun):
        self._kode = kode
        self._karyawan = karyawan
        self._presensi = presensi
        self._bulan = bulan
        self._tahun = tahun

        self._gaji_kotor = karyawan.hitung_gaji_kotor(presensi)
        # pembulatan setengah ke atas, dihitung dengan bilangan bulat
        self._potongan_bpjs = (self._gaji_kotor * TARIF_BPJS_PERSEN + 50) // 100
        self._gaji_bersih = self._gaji_kotor - self._potongan_bpjs

    @property
    def kode(self):
        return self._kode

    @property
    def karyawan(self):
        return self._karyawan

    @property
    def gaji_kotor(self):
        return self._gaji_kotor

    @property
    def potongan_bpjs(self):
        return self._potongan_bpjs

    @property
    def gaji_bersih(self):
        return self._gaji_bersih

    def cetak_slip(self):
        k, p = self._karyawan, self._presensi
        garis = "=" * 45
        print(garis)
        print("SLIP GAJI KARYAWAN".center(45))
        print(garis)
        print(f"Kode Slip   : {self._kode}")
        print(f"Periode     : {NAMA_BULAN[self._bulan - 1]} {self._tahun}")
        print(f"ID Karyawan : {k.id_karyawan}")
        print(f"Nama        : {k.nama}")
        print(f"Jabatan     : {k.jabatan}")
        print(f"Jenis       : {k.get_jenis()}")
        print("-" * 45)
        print(f"Hari Hadir  : {p.hari_hadir} hari")
        print(f"Hari Izin   : {p.hari_izin} hari")
        print(f"Hari Alpha  : {p.hari_alpha} hari")
        print(f"Jam Lembur  : {p.jam_lembur} jam")
        print("-" * 45)
        print(f"Gaji Kotor  : {format_rupiah(self._gaji_kotor)}")
        print(f"Pot. BPJS   : {format_rupiah(self._potongan_bpjs)}")
        print("-" * 45)
        print(f"Gaji Bersih : {format_rupiah(self._gaji_bersih)}")
        print(garis)