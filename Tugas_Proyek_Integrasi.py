from abc import ABC, abstractmethod

# 1. ABSTRACTION: Kontrak Dasar Produk
class Produk(ABC):
    @abstractmethod
    def hitung_pajak(self):
        pass

    @abstractmethod
    def tampilkan_info(self):
        pass

# 2. INHERITANCE: Class Induk ProdukElektronik
class ProdukElektronik(Produk):
    def __init__(self, nama, harga, stok):
        self.nama = nama
        # 3. ENCAPSULATION: Atribut Private __stok
        self.__harga = harga
        self.__stok = stok

    # Getter & Setter untuk Encapsulation
    def get_stok(self):
        return self.__stok

    def set_stok(self, jumlah):
        if jumlah >= 0:
            self.__stok = jumlah
            return True
        else:
            print(f"Gagal update stok {self.nama}! Stok tidak boleh negatif ({jumlah}).")
            return False

    def get_harga(self):
        return self.__harga

# 4. POLYMORPHISM: Implementasi berbeda pada Laptop & Smartphone
class Laptop(ProdukElektronik):
    def __init__(self, nama, harga, stok, prosesor):
        super().__init__(nama, harga, stok)
        self.prosesor = prosesor

    def hitung_pajak(self):
        return self.get_harga() * 0.10  # Pajak Laptop 10%

    def tampilkan_info(self):
        return f"[LAPTOP] {self.nama} | Proc: {self.prosesor}"

class Smartphone(ProdukElektronik):
    def __init__(self, nama, harga, stok, kamera):
        super().__init__(nama, harga, stok)
        self.kamera = kamera

    def hitung_pajak(self):
        return self.get_harga() * 0.05  # Pajak Smartphone 5%

    def tampilkan_info(self):
        return f"[SMARTPHONE] {self.nama} | Cam: {self.kamera}"

# --- EKSEKUSI SESUAI TARGET OUTPUT MODUL ---

print("--- SETUP DATA ---")
# Membuat objek
produk1 = Laptop("ROG Zephyrus", 20000000, 0, "Ryzen 9")
produk2 = Smartphone("iPhone 13", 15000000, 0, "12MP")

# Uji Encapsulation & Validasi
if produk1.set_stok(10):
    print(f"Berhasil menambahkan stok {produk1.nama}: 10 unit.")

if not produk2.set_stok(-5): # Akan gagal
    pass 

if produk2.set_stok(20):
    print(f"Berhasil menambahkan stok {produk2.nama}: 20 unit.")

print("\n--- STRUK TRANSAKSI ---")
keranjang = [
    {"item": produk1, "beli": 2},
    {"item": produk2, "beli": 1}
]

total_tagihan = 0
for i, pesanan in enumerate(keranjang, 1):
    obj = pesanan["item"]
    qty = pesanan["beli"]
    
    pajak = obj.hitung_pajak()
    subtotal = (obj.get_harga() + pajak) * qty
    total_tagihan += subtotal

    print(f"{i}. ")
    print(f" {obj.tampilkan_info()}")
    print(f"  Harga Dasar: Rp {obj.get_harga():,.0f} | Pajak: Rp {pajak:,.0f}")
    print(f"  Beli: {qty} unit | Subtotal: Rp {subtotal:,.0f}\n")

print("-" * 40)
print(f" TOTAL TAGIHAN: Rp {total_tagihan:,.0f}")
print("-" * 40)