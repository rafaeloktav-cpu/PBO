# 1. Definisikan Custom Exception
class OverweightBaggageError(Exception):
    pass

class MaxItemExceededError(Exception):
    pass

# 2. Definisikan Kelas Sistem Utama
class BaggageCheckSystem:
    def __init__(self, flight_number, max_weight_per_item, max_items):
        self.flight_number = flight_number
        self.max_weight_per_item = max_weight_per_item  # Batas berat per koper (kg)
        self.max_items = max_items                      # Batas maksimal jumlah koper

    def check_in_baggage(self, passenger_name, item_count, total_weight):
        # 1. Validasi jumlah koper
        if item_count > self.max_items:
            raise MaxItemExceededError(f"Ditolak: {passenger_name} membawa {item_count} koper. Maksimal hanya boleh {self.max_items} koper.")
        
        # 2. Validasi rata-rata berat per koper
        avg_weight = total_weight / item_count if item_count > 0 else 0
        if avg_weight > self.max_weight_per_item:
            raise OverweightBaggageError(f"Ditolak: Rata-rata berat koper ({avg_weight:.1f} kg) melebihi batas {self.max_weight_per_item} kg.")
        
        print(f"Sukses: Bagasi {passenger_name} ({item_count} koper, Total {total_weight} kg) lolos pengecekan untuk penerbangan {self.flight_number}.")

# --- Pengujian Sistem ---

# Inisialisasi: Penerbangan GA-123, Batas Berat 20 kg/koper, Maksimal 2 koper
airport_scale = BaggageCheckSystem("GA-123", max_weight_per_item=20, max_items=2)

print("--- Penumpang 1 ---")
try:
    airport_scale.check_in_baggage("Budi", item_count=2, total_weight=30)  # Rata-rata 15kg/koper (Aman)
except (MaxItemExceededError, OverweightBaggageError) as e:
    print(e)

print("\n--- Penumpang 2 ---")
try:
    airport_scale.check_in_baggage("Siti", item_count=3, total_weight=40)  # Jumlah koper terlalu banyak
except (MaxItemExceededError, OverweightBaggageError) as e:
    print(e)

print("\n--- Penumpang 3 ---")
try:
    airport_scale.check_in_baggage("Dewi", item_count=1, total_weight=25)  # Berat per koper melebihi 20kg
except (MaxItemExceededError, OverweightBaggageError) as e:
    print(e)