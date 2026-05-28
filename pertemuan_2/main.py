class Laptop:
    
    def __init__(self, merek, harga, spek):
        self.merek = merek
        self.harga = harga
        self.spek = spek

laptopUdin = Laptop("thinkpad", "3.000.000", "i3 windows 9")
laptopAidan = Laptop("Hp", "15.000.000", "i9 windows 11")
laptopSupri = Laptop("Dell", "2.000.000", "intel celeron windows 7")

print(f"Laptop Udin: Merk {laptopUdin.merek}, Harga {laptopUdin.harga}, Spek {laptopUdin.spek}")
print(f"Laptop Aidan: Merk {laptopAidan.merek}, Harga {laptopAidan.harga}, Spek {laptopAidan.spek}")
print(f"Laptop Supri: Merk {laptopSupri.merek}, Harga {laptopSupri.harga}, Spek {laptopSupri.spek}")