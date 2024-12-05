# Inisialisasi list kosong untuk menyimpan data mahasiswa
mahasiswa = []

while True:
    # Mengumpulkan data mahasiswa
    print("Nama: ", end="")
    nama = input()
    print("NIM: ", end="")
    nim = input()
    print("Nilai Tugas: ", end="")
    tugas = int(input())
    print("Nilai UTS: ", end="")
    uts = int(input())
    print("Nilai UAS: ", end="")
    uas = int(input())
    
    # Menghitung nilai akhir
    akhir = (tugas * 0.3) + (uts * 0.35) + (uas * 0.35)
    
    # Menambahkan data mahasiswa ke dalam list
    mahasiswa.append({
        "Nama": nama,
        "NIM": nim,
        "Tugas": tugas,
        "UTS": uts,
        "UAS": uas,
        "Akhir": round(akhir, 2)
    })
    
    # Menanyakan apakah ingin menambahkan data lagi
    print("Tambah data(y/t)?", end="")
    tambah_data = input().strip().lower()
    if tambah_data != 'y':
        break

# Menampilkan header tabel
print("\n" + "="*60)
print("| No | Nama      | NIM   | Tugas | UTS  | UAS  | Akhir |")
print("="*60)

# Menampilkan data setiap mahasiswa dalam tabel
for i, mhs in enumerate(mahasiswa, start=1):
    print(f"| {i:<2} | {mhs['Nama']:<9} | {mhs['NIM']:<5} | {mhs['Tugas']:<5} | {mhs['UTS']:<4} | {mhs['UAS']:<4} | {mhs['Akhir']:<5} |")
    
print("="*60)
