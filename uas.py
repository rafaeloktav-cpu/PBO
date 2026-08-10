class Orang:
    def __init__(self, nama, nomor_id):
        self._nama = nama
        self._nomor_id = nomor_id

    def tampilan_info(self):
        pass 

class Dosen(Orang):
    def __init__(self, nama, nomor_id, jabatan):
        super().__init__(nama, nomor_id)
        self._jabatan = jabatan

    def tampilan_info(self):
        return f"Dosen : {self._nama} | NIP: {self._nomor_id} | Jabatan: {self._jabatan}"

class MahasiswaS2(Orang):
    def __init__(self, nama, nomor_id, prodi):
        super().__init__(nama, nomor_id)
        self._prodi = prodi 

    def tampilan_info(self):
        return f"Mahasiswa : {self._nama} | NIM: {self._nomor_id} | prodi: {self._prodi}"


class Matakuliah:
    def __init__(self, kode_mk, nama_mk, sks):
        self._kode = kode_mk
        self._nama = nama_mk
        self._sks = sks

    def info_mata_kuliah(self):  
        return f"{self._kode} - {self._nama} ({self._sks} SKS)"


class Jadwal:
    def __init__(self, hari, jam, mata_kuliah, dosen, ruangan):
        self._hari = hari
        self._jam = jam
        self._mata_kuliah = mata_kuliah
        self._dosen = dosen
        self._ruangan = ruangan

    def tampilkan_jadwal(self):  
        print("-" * 60)
        print(f" Hari/Jam   : {self._hari}, {self._jam}")  
        print(f" Mata Kuliah: {self._mata_kuliah.info_mata_kuliah()}") 
        print(f" Dosen     : {self._dosen.tampilan_info()}")  
        print(f" Ruangan    : {self._ruangan}")  
        print("-" * 60)


if __name__ == "__main__":
    
    dosen1 = Dosen("Dr. Muhammad Ahmad", "123456789", "Lektor Kepala")
    mk1 = Matakuliah("TI-8201", "Metodologi Penelitian Ilmu Komputer", "3")
    mk2 = Matakuliah("TI-8202", "Arsitektur Sistem Terdistribusi", "3")
    
    daftar_jadwal = [
        Jadwal("Senin", "08.00 - 10.30", mk1, dosen1, "Ruang Pascasarjana A"),
        Jadwal("Rabu", "13.00 - 15.30", mk2, dosen1, "Ruang Pascasarjana B")
    ]

   
    print("=" * 60)
    print("===== SISTEM INFORMASI JADWAL PASCASARJANA =====")
    nama_pengguna = input("\nSilakan Masukkan Nama Anda: ").strip()

    print(f"\n Selamat Datang, {nama_pengguna}!")
    print(" Berikut Jadwal Perkuliahan Anda:\n")
    
    for jadwal in daftar_jadwal:
        jadwal.tampilkan_jadwal()
