perpus = [
    {"kode": "B01", "judul": "Python Dasar", "status": "tersedia"},
    {"kode": "B02", "judul": "Basis Data", "status": "tersedia"},
    {"kode": "B03", "judul": "Jaringan", "status": "dipinjam"}
]


def tampilkan():
    print("\n--- Katalog Buku ---")
    i = 0
    while i < len(perpus):
        buku = perpus[i]
        print(f"Kode: {buku['kode']} | Judul: {buku['judul']} | Status: {buku['status']}")
        i += 1


def cari(kode):
    i = 0
    while i < len(perpus):
        if perpus[i]["kode"] == kode:
            return i
        i += 1
    return "tidak ada"


def pinjam(kode):

    i = cari(kode)

    if i == "tidak ada":
        print("Kode tidak ada.")
        return

    if perpus[i]["status"] == "dipinjam":
        print("Buku sedang dipinjam.")
        return

    perpus[i]["status"] = "dipinjam"
    print("Berhasil dipinjam.")


print("=== SISTEM PERPUSTAKAAN ===")

while True:
    print("\n[ Menu Utama ]")
    print("1. Tampilkan Buku")
    print("2. Pinjam Buku")
    print("3. Keluar")

    pilihan = input("Pilih menu (1/2/3): ")

    if pilihan == "3":
        print("Sistem ditutup. Terima kasih!")
        break
    elif pilihan == "1":
        tampilkan()
    elif pilihan == "2":
        kode_input = input("Masukkan kode buku (contoh: B01): ")
        pinjam(kode_input)
    else:
        print("Pilihan tidak valid.")
