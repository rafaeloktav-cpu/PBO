class Karyawan:
    nama = ''
    kinerja_status = '' 

    @staticmethod
    def prestasi():
        print("Karyawan ini memiliki banyak prestasi")

    def kinerja(self): 
        print(f"Karyawan dengan Nama {self.nama}, bekerja dengan {self.kinerja_status}")


karyawan1 = Karyawan()
karyawan1.nama = 'Ahmad'
karyawan1.kinerja_status = 'rajin'

print(f"Nama: {karyawan1.nama}") 
karyawan1.kinerja() 

print("-" * 20)


karyawan2 = Karyawan()
karyawan2.nama = 'Ahmad2'
karyawan2.kinerja_status = 'malas'

print(f"Nama: {karyawan2.nama}")
karyawan2.kinerja()