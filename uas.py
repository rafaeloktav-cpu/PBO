class Dosen:
    def __init__(self, nama, nip, jabatan):
        self.nama, self.nip, self.jabatan = nama, nip, jabatan
    def info(self):
        return f"Dosen: {self.nama}"

class Matkul:
    def __init__(self, kode, nama, sks):
        self.kode, self.nama, self.sks = kode, nama, sks
    def info(self):
        return f"{self.nama} ({self.sks} SKS)"

class Jadwal:
    def __init__(self, hari, jam, mk, dosen, ruang):
        self.hari, self.jam = hari, jam
        self.mkuliah, self.dosen = mk, dosen
        self.ruang, self.status = ruang, "berjalan"
    def ubah_status(self, s): self.status = s
    def ubah_ruang(self, r): self.ruang = r
    def tampil(self, no=None):
        print("-"*55)
        if no: print(f"[{no}] ", end="")
        print(f"Hari/Jam   : {self.hari}, {self.jam}")
        print(f"Mata Kuliah: {self.mkuliah.info()}")
        print(f"Dosen      : {self.dosen.info()}")
        print(f"Ruangan    : {self.ruang}")
        print(f"Status      : {self.status.upper()}")
        print("-"*55)

# === PILIHAN DATA ===
daftar_mk_pilihan = [
    Matkul("MK01", "Mantiq (Logika Islam)", "2"),
    Matkul("MK02", "Filsafat Islam", "3"),
    Matkul("MK03", "Islamisasi Sains dan Teknologi", "3"),
    Matkul("MK04", "Islamisasi Pengetahuan Kontemporer", "2"),
    Matkul("MK05", "Metodologi Studi Islam", "3"),
]
daftar_dosen_pilihan = [
    Dosen("Dr. Harun Al Rasyid, M.Ag.", "-", "-"),
    Dosen("Prof. Dr. Iskandar Zulkarnain, M.A.", "-", "-"),
    Dosen("Dr. Taufik Hidayat, M.T.", "-", "-"),
    Dosen("Prof. Dr. Lukman Hakim, M.Phil", "-", "-"),
    Dosen("Dr. Farhan Al-Ghifari, M.Ag", "-", "-"),
]
pilihan_hari = ["Senin", "Selasa", "Rabu", "Kamis", "Jumat", "Sabtu", "Minggu"]
pilihan_jam = ["08.00 - 09.30", "10.00 - 11.30", "13.00 - 14.30"]

daftar_jadwal = []
PASS_ADMIN = "12345"

# === Bantuan ===
def pilih_jadwal(pesan):
    if not daftar_jadwal:
        print("Belum ada jadwal!")
        return None
    for i, j in enumerate(daftar_jadwal, 1):
        j.tampil(i)
    pilih = input(pesan)
    if pilih.isdigit() and 1<=int(pilih)<=len(daftar_jadwal):
        return int(pilih)-1
    print("Pilihan salah!")

def pilih_hari():
    print("\n--- Pilih Hari ---")
    for i, h in enumerate(pilihan_hari, 1):
        print(f" {i}. {h}")
    pilih = input("Nomor hari: ")
    if pilih.isdigit() and 1<=int(pilih)<=7:
        return pilihan_hari[int(pilih)-1]
    print("Pilihan hari salah!")
    return None

# === Menu Admin ===
def menu_admin():
    print("\n" + "="*40)
    print("          MENU ADMIN")
    print("="*40)
    print("1. Input Jadwal")
    print("2. Ubah Status Jadwal")
    print("3. Ubah Ruangan")
    print("4. Lihat Semua Jadwal")
    print("5. Log Out")
    return input("Pilih menu: ")

def input_jadwal():
    print("\n--- Pilih Mata Kuliah ---")
    for i, mk in enumerate(daftar_mk_pilihan, 1):
        print(f" {i}. {mk.info()} — {daftar_dosen_pilihan[i-1].nama}")
    pilih_mk = input("Nomor mata kuliah (1-5): ")
    if not pilih_mk.isdigit() or not (1<=int(pilih_mk)<=5):
        return print("Pilihan tidak valid!")
    mk = daftar_mk_pilihan[int(pilih_mk)-1]
    dosen = daftar_dosen_pilihan[int(pilih_mk)-1]

    hari = pilih_hari()
    if not hari: return

    print("\n--- Pilih Jam ---")
    for i, jm in enumerate(pilihan_jam, 1):
        print(f" {i}. {jm}")
    pilih_jm = input("Nomor jam: ")
    if not pilih_jm.isdigit() or not (1<=int(pilih_jm)<=3):
        return print("Pilihan jam salah!")
    jam = pilihan_jam[int(pilih_jm)-1]

    ruang = input("Ruangan: ")
    daftar_jadwal.append(Jadwal(hari, jam, mk, dosen, ruang))
    print("Jadwal berhasil ditambahkan!")

def ubah_status():
    idx = pilih_jadwal("Ubah nomor: ")
    if idx!=None:
        s = input("Status [berjalan/diliburkan]: ").lower()
        daftar_jadwal[idx].ubah_status(s)
        print(f"Diubah jadi: {s.upper()}")

def ubah_ruangan():
    idx = pilih_jadwal("Ubah ruang nomor: ")
    if idx!=None:
        r = input("Ruangan baru: ")
        daftar_jadwal[idx].ubah_ruang(r)
        print(f"Ruangan jadi: {r}")

def lihat_semua():
    if not daftar_jadwal: print("Belum ada jadwal")
    else:
        for i,j in enumerate(daftar_jadwal,1): j.tampil(i)

# === Pengguna ===
def lihat_jadwal_pengguna(nama):
    print(f"\nSelamat datang, {nama}!")
    print("--- Jadwal Perkuliahan ---")
    ada = False
    for j in daftar_jadwal:
        if j.status=="berjalan":
            j.tampil()
            ada=True
    if not ada:
        print("\nTidak ada Perkuliahan Hari Ini")

# === Program Utama ===
if __name__=="__main__":
    while True:
        print("\n" + "="*50)
        print("===== SISTEM JADWAL PERKULIAHAN =====")
        print("="*50)
        nama = input("Masukkan Nama: ").strip()

        if nama.lower()=="admin":
            sandi = input("Kata Sandi: ")
            if sandi==PASS_ADMIN:
                print("Login Admin Berhasil!")
                while True:
                    pilih = menu_admin()
                    if pilih=="1": input_jadwal()
                    elif pilih=="2": ubah_status()
                    elif pilih=="3": ubah_ruangan()
                    elif pilih=="4": lihat_semua()
                    elif pilih=="5":
                        print("Log Out berhasil! Kembali ke menu awal")
                        break
                    else: print("Pilihan salah!")
            else: print("Sandi salah!")
        else:
            lihat_jadwal_pengguna(nama)
            print("\nTerima kasih!")
            input("Tekan Enter untuk kembali ke menu awal")