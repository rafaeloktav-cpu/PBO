class Karakter:
    def __init__(self, nama: str):
        self.nama = nama

    def aksi_spesial(self):
        print(f"Karakter {self.nama} melakukan aksi dasar (berjalan/berlari).")

class Warrior(Karakter):
    def aksi_spesial(self):
        print(f"Warrior {self.nama} menggunakan 'Slash': Menebas musuh dengan damage tinggi!")

class Mage(Karakter):
    def aksi_spesial(self):
        print(f"Mage {self.nama} menggunakan 'Meteor': Memanggil hujan api area (AoE)!")


class PotionKesehatan:
    def aksi_spesial(self):
        print("Sistem Item: Mengembalikan 50 HP ke target yang mengaktifkannya.")


def picu_aksi(objek_game):
    objek_game.aksi_spesial()



hero_pemula = Karakter("Bambang")
knight = Warrior("Arthur")
wizard = Mage("Merlin")
item_darurat = PotionKesehatan()

print("--- AKSI KARAKTER DI ARENA ---")
picu_aksi(hero_pemula)   
picu_aksi(knight)       
picu_aksi(wizard)


print("\n--- MEKANIK SISTEM GAME ---") 
picu_aksi(item_darurat)