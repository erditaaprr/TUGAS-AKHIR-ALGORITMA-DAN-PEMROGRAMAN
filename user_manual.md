User Manual – Aplikasi Inventori Coffee Shop
1. Deskripsi Program
Aplikasi ini adalah program Python berbasis teks untuk mengelola inventori di sebuah Coffee Shop. Program memungkinkan pengguna untuk menambahkan, melihat, mengedit, menghapus, dan melaporkan stok bahan baku maupun menu minuman.

Semua data disimpan dalam file coffeeshop_data.json agar dapat diakses kembali saat program dijalankan ulang.

2. Persyaratan Sistem
Python 3.6 atau lebih tinggi
Dapat dijalankan melalui:
•Terminal / Command Prompt
•Visual Studio Code
•Google Colab

3. Struktur File
Nama File	Keterangan
inventori_kopi.py	File utama berisi kode program
coffeeshop_data.json	File penyimpanan data bahan & menu
user_manual.md	File dokumentasi ini

4. Cara Menjalankan Program
Di Terminal / VS Code:
Pastikan Python sudah terpasang.

Buka folder tempat file inventori_kopi.py berada.

Jalankan perintah berikut:
•bash
•Copy
•Edit
python inventori_kopi.py
Di Google Colab:
Upload file inventori_kopi.py.

Jalankan sel dengan perintah berikut:
•python
•Copy
•Edit
!python inventori_kopi.py
File coffeeshop_data.json akan otomatis muncul di direktori Colab.

5. Panduan Menu Program
Saat program dijalankan, kamu akan melihat tampilan menu:
•markdown
•Copy
•Edit

=== Menu Inventori Coffee Shop ===
1. Tambah Bahan/Menu
2. Lihat Semua Data
3. Edit Stok
4. Hapus Data
5. Laporan Stok
6. Simpan & Keluar

No	Menu	Fungsi
1. Tambah Bahan/Menu	Menambahkan item baru (kode, nama, jenis, stok). Kode harus unik.
2. Lihat Semua Data	Menampilkan semua data bahan dan menu yang tersimpan.
3. Edit Stok	Mengubah stok dari item berdasarkan kode.
4. Hapus Data	Menghapus item dari daftar inventori berdasarkan kode.
5. Laporan Stok	Menampilkan daftar item berdasarkan stok terbanyak ke terkecil.
6. Simpan & Keluar	Menyimpan data ke file JSON dan mengakhiri program.

6. Format Input
Field	Format	Contoh
Kode	String unik	DRK001
Nama	Teks bebas	Matcha Latte
Jenis	'bahan' / 'menu'	menu
Stok	Angka bulat positif	25

7. Fitur Optimasi & Error Handling
 Validasi kode agar tidak duplikat
 Validasi input stok (harus berupa angka dan tidak negatif)
 Waktu eksekusi dicatat dengan time.time() (untuk tampil & laporan)
 Data aman tersimpan dalam file .json
 Penanganan error jika file tidak ditemukan (try-except)

8. Catatan Tambahan
File coffeeshop_data.json akan otomatis dibuat jika belum ada.

Jangan mengedit file JSON secara manual agar tidak merusak strukturnya.

Data hanya akan tersimpan saat memilih menu 6. Simpan & Keluar.

Gunakan jenis 'menu' untuk produk jadi (misal: Matcha Latte, Cappuccino ) dan 'bahan' untuk bahan baku (misal: Susu, Gula, Kopi Bubuk).

9. Saran Pengembangan
Fitur lanjutan yang bisa ditambahkan:

pencarian berdasarkan nama item

 Filter berdasarkan jenis (menu/bahan)

 Ekspor laporan stok ke file .csv atau .txt

Mengganti struktur list ke dictionary untuk pencarian lebih cepat (O(1))
