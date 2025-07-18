# -*- coding: utf-8 -*-
"""inventory.kopi

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/18DyHhW5EHvD7ibVp45u2EeIZz_lrkDCh
"""

import json # mengambil fungsi utk simpan dan baca data
import time # OPTIMASI: untuk mengukur waktu eksekusi fungsi

# d = data item (bahan atau menu minuman di coffee shop)

data_kopi = [] # list untuk menyimpan data inventori

# simpan data ke file
def save_data():
    with open("coffeeshop_data.json", "w") as f: # buka file dalam mode tulis
        json.dump(data_kopi, f) # simpan data dalam format JSON

# muat data dari file
def load_data():
    try:
        with open("coffeeshop_data.json", "r") as f: # buka file dalam mode baca
            return json.load(f) # ambil dan kembalikan data
    except:
        return [] # jika file belum ada atau rusak, mulai dari kosong

# cari item berdasarkan kode
def search_item(kode):
    for d in data_kopi: # periksa tiap item dalam list
        if d['kode'] == kode: # cocokkan kode
            return d
    return None # jika tidak ditemukan

# """" MENU UTAMA """"

def tambah_item(): # tambah bahan atau menu
    kode = input("Kode item: ") # input kode
    if search_item(kode): # cek apakah kode sudah ada
        print("Item dengan kode ini sudah terdaftar.")
        return
    nama = input("Nama item: ") # input nama item
    jenis = input("Jenis (bahan/menu): ").lower() # input jenis
    if jenis not in ['bahan', 'menu']: # validasi jenis
        print("Jenis hanya boleh 'bahan' atau 'menu'.")
        return
    try:
        stok = int(input("Jumlah stok: ")) # input stok
        if stok < 0:
            print("Stok tidak boleh negatif.")
            return
    except ValueError:
        print("Stok harus berupa angka.")
        return
    data_kopi.append({"kode": kode, "nama": nama, "jenis": jenis, "stok": stok}) # data ditambahkan
    print("Item berhasil ditambahkan.\n")

def lihat_all(): # tampilkan semua data
    if not data_kopi:
        print("Belum ada data.")
        return
    start = time.time()  # OPTIMASI: mulai hitung waktu
    for d in data_kopi: # tampilkan tiap item
        print(f"{d['kode']} - {d['nama']} ({d['jenis']}, Stok: {d['stok']})")
    end = time.time()
    print(f"Waktu tampilkan data: {end - start:.6f} detik\n") # tampilkan waktu eksekusi

def edit_stok(): # ubah stok item
    kode = input("Masukkan kode item yang ingin diedit: ")
    d = search_item(kode) # cari item
    if d:
        try:
            stok_baru = int(input("Stok baru: ")) # input stok baru
            if stok_baru < 0:
                print("Stok tidak boleh negatif.")
                return
            d['stok'] = stok_baru # update stok
            print("Stok berhasil diperbarui.\n")
        except ValueError:
            print("Input stok harus berupa angka.")
    else:
        print("Item tidak ditemukan.") # jika kode tidak cocok

def hapus_item(): # hapus item dari list
    kode = input("Masukkan kode item yang ingin dihapus: ")
    d = search_item(kode) # cari item
    if d:
        data_kopi.remove(d) # hapus data
        print("Item berhasil dihapus.\n")
    else:
        print("Item tidak ditemukan.") # kalau kode tidak ditemukan

def report_stok(): # tampilkan laporan stok
    if not data_kopi:
        print("Belum ada data.")
        return
    print("Laporan stok (diurutkan dari terbanyak):")
    start = time.time()  # OPTIMASI: mulai hitung waktu
    urut = sorted(data_kopi, key=lambda x: x['stok'], reverse=True) # urutkan dari stok tertinggi
    for d in urut:
        print(f"{d['nama']} ({d['jenis']}) - Stok: {d['stok']}")
    end = time.time()
    print(f"Waktu proses laporan: {end - start:.6f} detik\n") # tampilkan waktu eksekusi

# """" PROGRAM UTAMA DAN ALUR KERJANYA """"
data_kopi = load_data() # muat data saat program dimulai

while True:
    print("=== Menu Inventori Coffee Shop ===")
    print("1. Tambah Bahan/Menu")
    print("2. Lihat Semua Data")
    print("3. Edit Stok")
    print("4. Hapus Data")
    print("5. Laporan Stok")
    print("6. Simpan & Keluar")

    pilihan = input("Pilih menu (1-6): ")
    print()
    # percabangan sesuai input
    if pilihan == '1': tambah_item()
    elif pilihan == '2': lihat_all()
    elif pilihan == '3': edit_stok()
    elif pilihan == '4': hapus_item()
    elif pilihan == '5': report_stok()
    elif pilihan == '6':
        save_data() # simpan data sebelum keluar
        print("Data disimpan. Keluar.")
        break
    else:
        print("Pilihan tidak valid.\n")