<img width="578" height="418" alt="Screenshot 2026-02-05 091239" src="https://github.com/user-attachments/assets/c4908a0e-773c-4eed-98c8-148d79b0e2b5" />


Analisis Proyek
1. Keamanan Data (Encapsulation) Atribut __stok dan __harga dibuat private agar tidak bisa diubah sembarangan tanpa melewati fungsi set_stok. Hal ini mencegah data stok menjadi negatif yang akan merusak logika bisnis.

2. Struktur Program (Abstraction) Menggunakan from abc import ABC, abstractmethod. Class Produk bertindak sebagai kontrak murni. Jika ada produk baru (misal: Tablet), ia wajib memiliki fungsi hitung_pajak dan tampilkan_info, jika tidak program akan error.

3. Pewarisan (Inheritance) Laptop dan Smartphone mewarisi fungsi dasar dari ProdukElektronik. Ini membuat kode lebih rapi karena kita tidak perlu menulis ulang logika stok dan harga di setiap jenis barang.

4. Perbedaan Perilaku (Polymorphism) Meskipun keduanya memanggil hitung_pajak(), hasilnya berbeda: Laptop dikenakan 10% sedangkan Smartphone 5%. Ini memungkinkan sistem kasir menghitung total secara otomatis tanpa perlu banyak perintah if-else.
