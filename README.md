# 📚 Sistem Manajemen Perpustakaan dengan Python

**Aplikasi sederhana untuk mengelola katalog dan peminjaman buku menggunakan bahasa pemrograman Python.**

## 👨‍💻 Identitas Pengembang

- **Nama:** Irga Mochamad Rafly
- **NPM:** 267006111160
- **Kelas:** B
- **Program Studi:** Informatika
- **Universitas:** Universitas Siliwangi
- **Bahasa Pemrograman:** Python

---

## 📖 Deskripsi Proyek

**Sistem Manajemen Perpustakaan** merupakan program sederhana berbasis Python yang dirancang untuk menyimulasikan aktivitas pengelolaan buku dalam sebuah perpustakaan.

Program ini menyediakan sistem menu interaktif yang memungkinkan pengguna untuk melihat katalog buku, mencari buku berdasarkan kode, serta melakukan proses peminjaman dengan memeriksa status ketersediaan buku terlebih dahulu.

Setiap buku disimpan menggunakan struktur data Dictionary yang kemudian dikumpulkan dalam sebuah List. Dengan pendekatan ini, informasi buku seperti kode, judul, dan status peminjaman dapat dikelola secara lebih terstruktur.

Proyek ini dibuat sebagai implementasi pembelajaran dasar pemrograman Python, khususnya penggunaan struktur data, fungsi, perulangan, dan percabangan.

## 🎯 Tujuan Program

- Memahami penggunaan List dan Dictionary untuk mengelola data.
- Mempelajari pembuatan dan pemanggilan Function.
- Menerapkan While Loop untuk menjalankan menu secara berulang.
- Menggunakan Conditional Statement untuk menentukan alur program.
- Memahami proses pencarian data berdasarkan kode buku.
- Menerapkan validasi status buku sebelum proses peminjaman dilakukan.

## ⚙️ Fitur Utama

### 1. 📖 Menampilkan Katalog Buku
Menampilkan seluruh daftar buku yang tersedia dalam sistem, termasuk kode buku, judul, dan status peminjaman.

### 2. 🔎 Pencarian Buku Berdasarkan Kode
Program menyediakan fungsi pencarian untuk menemukan posisi buku berdasarkan kode yang dimasukkan pengguna.

### 3. 📕 Peminjaman Buku
Pengguna dapat meminjam buku dengan memasukkan kode buku yang ingin dipinjam.

### 4. ✅ Pemeriksaan Ketersediaan Buku
Sebelum peminjaman dilakukan, program memeriksa status buku. Jika buku sudah dipinjam, sistem akan menolak permintaan peminjaman.

### 5. 🔄 Menu Interaktif
Pengguna dapat memilih menu untuk menampilkan buku, melakukan peminjaman, atau keluar dari program.

### 6. ⚠️ Validasi Input
Program memberikan pesan apabila kode buku tidak ditemukan, buku sedang dipinjam, atau pilihan menu tidak valid.

## 🛠️ Konsep Python yang Digunakan

| Konsep | Fungsi |
|---|---|
| List | Menyimpan kumpulan data buku |
| Dictionary | Menyimpan informasi setiap buku |
| Function | Membagi program menjadi beberapa fungsi |
| Parameter | Mengirimkan kode buku ke fungsi |
| `while` | Melakukan perulangan pencarian dan menu |
| `if-elif-else` | Mengatur kondisi dan pilihan menu |
| `return` | Mengembalikan hasil pencarian |
| `break` | Menghentikan perulangan menu |
| `input()` | Menerima masukan pengguna |
| `len()` | Menghitung jumlah data buku |
| `f-string` | Menampilkan informasi buku secara dinamis |

## 🧩 Penjelasan Fungsi Program

Program memiliki tiga fungsi utama:

**1. Fungsi `tampilkan()`**

Digunakan untuk menampilkan seluruh katalog buku dengan melakukan perulangan terhadap data yang tersimpan dalam List `perpus`.

**2. Fungsi `cari(kode)`**

Digunakan untuk mencari buku berdasarkan kode. Jika ditemukan, fungsi mengembalikan indeks buku. Jika tidak ditemukan, fungsi mengembalikan nilai `"tidak ada"`.

**3. Fungsi `pinjam(kode)`**

Digunakan untuk memproses peminjaman buku. Fungsi ini memanggil `cari(kode)` terlebih dahulu, kemudian memeriksa apakah buku ditemukan dan apakah statusnya masih tersedia.

Jika seluruh kondisi terpenuhi, status buku akan diubah menjadi `"dipinjam"`.

## 🚀 Cara Menjalankan Program

1. Pastikan Python sudah terinstal pada perangkat.
2. Clone atau download repository ini.
3. Buka folder proyek menggunakan Visual Studio Code atau terminal.
4. Jalankan file Python menggunakan perintah:

```bash
python sistem_perpustakaan.py
```

5. Pilih menu sesuai kebutuhan yang ditampilkan pada terminal.

## 💻 Contoh Tampilan Program

```text
=== SISTEM PERPUSTAKAAN ===

[ Menu Utama ]
1. Tampilkan Buku
2. Pinjam Buku
3. Keluar

Pilih menu (1/2/3): 1

--- Katalog Buku ---
Kode: B01 | Judul: Python Dasar | Status: tersedia
Kode: B02 | Judul: Basis Data | Status: tersedia
Kode: B03 | Judul: Jaringan | Status: dipinjam

[ Menu Utama ]
1. Tampilkan Buku
2. Pinjam Buku
3. Keluar

Pilih menu (1/2/3): 2
Masukkan kode buku (contoh: B01): B01
Berhasil dipinjam.

[ Menu Utama ]
1. Tampilkan Buku
2. Pinjam Buku
3. Keluar

Pilih menu (1/2/3): 3
Sistem ditutup. Terima kasih!
```

*Catatan: Contoh di atas merupakan simulasi penggunaan program berdasarkan kode yang dibuat.*

## 📌 Batasan dan Pengembangan Program

Program ini masih menggunakan penyimpanan data sementara di dalam List. Artinya, perubahan status buku hanya berlaku selama program berjalan dan akan kembali ke data awal ketika program dijalankan ulang.

Beberapa pengembangan yang dapat dilakukan selanjutnya:

- Menambahkan fitur pengembalian buku.
- Menambahkan fitur pencarian berdasarkan judul.
- Menambahkan fitur registrasi anggota perpustakaan.
- Menambahkan riwayat transaksi peminjaman.
- Menggunakan file JSON atau database untuk menyimpan data secara permanen.
- Menambahkan sistem login untuk admin dan anggota.

## 📝 Penutup

Proyek ini merupakan salah satu bentuk penerapan dasar pemrograman Python dalam membangun sistem pengelolaan data sederhana.

Melalui proyek ini, diharapkan pemahaman mengenai penggunaan List, Dictionary, Function, perulangan, percabangan, dan proses pencarian data dapat semakin berkembang.

---

**Developed by Irga Mochamad Rafly**  
*Informatika – Universitas Siliwangi*

⭐ Jika proyek ini bermanfaat, jangan ragu untuk mengembangkan dan mempelajarinya lebih lanjut!
