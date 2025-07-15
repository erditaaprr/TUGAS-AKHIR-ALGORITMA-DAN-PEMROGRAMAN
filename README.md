DESKRIPSI PROGRAM
Aplikasi ini adalah program Python berbasis teks untuk mengelola inventori di sebuah Coffee Shop. Program memungkinkan pengguna untuk menambahkan, melihat, mengedit, menghapus, dan melaporkan stok bahan baku maupun menu minuman.

Dapat dijalankan melalui:
Terminal / Command Prompt
Visual Studio Code
Google Colab

Panduan Menu Program
Saat program dijalankan, kamu akan melihat tampilan menu:
markdown
Copy
Edit

=== Menu Inventori Coffee Shop ===
1. Tambah Bahan/Menu
2. Lihat Semua Data
3. Edit Stok
4. Hapus Data
5. Laporan Stok
6. Simpan & Keluar
No	Menu	Fungsi
1	Tambah Bahan/Menu	Menambahkan item baru (kode, nama, jenis, stok). Kode harus unik.
2	Lihat Semua Data	Menampilkan semua data bahan dan menu yang tersimpan.
3	Edit Stok	Mengubah stok dari item berdasarkan kode.
4	Hapus Data	Menghapus item dari daftar inventori berdasarkan kode.
5	Laporan Stok	Menampilkan daftar item berdasarkan stok terbanyak ke terkecil.
6	Simpan & Keluar	Menyimpan data ke file JSON dan mengakhiri program.

PENJELASAN SETIAP CODE
1. Impor Perpustakaan
import json #mengambil fungsi utk menyimpan dan membaca data
import time # OPTIMASI: untuk mengukur waktu fungsi eksekusi
json : Digunakan untuk menyimpan dan membaca data dalam format JSON.
time : Digunakan untuk mengukur waktu eksekusi fungsi, membantu dalam optimasi.

INSTALASI DATA
data_kopi = [] # list untuk menyimpan data inventori
data_kopi : Daftar kosong yang akan menyimpan data item (bahan atau menu) di kedai kopi.

FUNGSI UNTUK MENYIMPAN DATA
save_data : Fungsi ini menyimpan data inventaris ke dalam file JSON. Jika file tidak ada, akan dibuat baru.

FUNGSI UNTUK MEMUAT DATA
load_data : Fungsi ini memuat data dari file JSON. Jika file tidak ada atau rusak, akan mengembalikan daftar kosong.

FUNGSI UNTUK MENCARI ITEM
search_item : Fungsi ini mencari item berdasarkan kode. Jika ditemukan, barang tersebut akan dikembalikan; jika tidak, akan mengembalikan None.

FUNGSI UNTUK MENAMBAH ITEM
tambah_item : Fungsi ini menambahkan item baru ke dalam inventaris. Memeriksa apakah kode sudah ada, dan melakukan validasi untuk jenis dan stoK

FUNGSI UNTUK MELIHAT SEMUA DATA
ihat_all : Fungsi ini menampilkan semua item dalam inventaris. Menghitung waktu yang dibutuhkan untuk menampilkan data.

FUNGSI UNTUK MENGEDIT STOK
edit_stok : Fungsi ini mengubah jumlah stok item yang ada. Memeriksa apakah barang ditemukan dan melakukan validasi pada input stok baru.

FUNGSI UNTUK MENGAHPUS ITEM
hapus_item : Fungsi ini menghapus item dari inventaris berdasarkan kode. Jika item tidak ditemukan, akan memberikan pesan yang sesuai.

FUNGSI UNTUK MELAPORKAN STOK
report_stok : Fungsi ini menampilkan laporan stok yang diurutkan dari yang terbanyak. Menghitung waktu yang dibutuhkan untuk memproses laporan.

Kesimpulan

Program ini memberikan antarmuka yang sederhana untuk mengelola inventaris di kedai kopi, memungkinkan pengguna untuk menambah, melihat, mengedit, menghapus, dan melaporkan stok item. Dengan menggunakan JSON untuk penyimpanan data, program ini juga memastikan bahwa data dapat dipertahankan antara sesi.






        
