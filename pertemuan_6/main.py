class AlatElektronik:
    def __init__(self, merk, lokasi):
        self.merk = merk
        self.lokasi = lokasi  

    def info(self):
        print(f"Alat merk {self.merk} ini diletakkan {self.lokasi}.")
        
    def fungsi_tombol_power(self):
        print("Sistem: Layar menyala dan baterai mulai terpakai.")

class JamWeker(AlatElektronik):
    def fungsi_tombol_power(self):
        print("Fungsi Jam: Menampilkan jam digital di pojok atas layar.")
        super().fungsi_tombol_power()

class PemutarMusik(AlatElektronik):
    def fungsi_tombol_power(self):
        print("Fungsi Musik: Menampilkan widget lagu yang terakhir diputar.")
        super().fungsi_tombol_power()


class Smartphone(JamWeker, PemutarMusik):
    def fungsi_tombol_power(self):
        print("Fungsi HP: Membuka kunci layar utama (Lock Screen).")
        super().fungsi_tombol_power()



hp_kita = Smartphone("Samsung", "di atas kasur")
hp_kita.info()

print("\nSaat kita menekan tombol power HP:")
hp_kita.fungsi_tombol_power()