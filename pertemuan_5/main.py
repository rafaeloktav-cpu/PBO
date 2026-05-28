class SmartLock:
    
    __pemilik = ''
    __id_pintu = 0
    __pin_akses = ''
    __status_kunci = ''

    def __init__(self, pemilik, id_pintu, pin_akses):
        self.__pemilik = pemilik
        self.__id_pintu = id_pintu
        self.__pin_akses = pin_akses
        self.__status_kunci = "Terkunci" 

    
    def get_pemilik(self):
        return self.__pemilik

    def get_id_pintu(self):
        return self.__id_pintu

    def get_status_kunci(self):
        return self.__status_kunci

    
    def buka_pintu(self, pin_input):
        if pin_input != self.__pin_akses:
            print("PIN salah! Akses masuk ditolak.")
            return
        self.__status_kunci = "Terbuka"
        print(f"PIN benar. Selamat datang kembali, {self.__pemilik}!")
    
    
    def kunci_darurat(self, pin_input):
        if pin_input != self.__pin_akses:
            print("PIN salah! Gagal mengaktifkan kunci darurat.")
            return
        self.__status_kunci = "Terkunci (Mode Darurat)"
        print(f"Pintu {self.__id_pintu} milik {self.__pemilik} berhasil dikunci dalam mode darurat!")





pintu1 = SmartLock("Ahmad Fauzi", 101, "987654")



pintu1.buka_pintu("000000")       # Contoh jika PIN salah
pintu1.buka_pintu("987654")       # Contoh jika PIN benar

print(f"Pemilik     : {pintu1.get_pemilik()}")
print(f"Nomor Pintu : {pintu1.get_id_pintu()}")
print(f"Status Pintu: {pintu1.get_status_kunci()}")

print("-" * 40)


pintu2 = SmartLock("Zaki", 102, "112233")

pintu2.kunci_darurat("123456")    # Nyoba pakai PIN asal (salah)
print(f"Status Pintu: {pintu2.get_status_kunci()}")

pintu2.kunci_darurat("112233")    # Pakai PIN yang benar
print(f"Status Pintu: {pintu2.get_status_kunci()}")