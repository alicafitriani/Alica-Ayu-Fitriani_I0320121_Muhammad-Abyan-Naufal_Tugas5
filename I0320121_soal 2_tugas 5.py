# Input nama dan nilai
nama = input("Masukkan Nama Anda : ")
nilai = float(input("Masukkan Nilai Anda : "))
nama_konversi = 'Halo, '+ nama + '!'
nilai_konversi = 'Nilai anda setelah dikonversi adalah'

# Konversi nilai
if nilai >= 0 and nilai <= 100:
    if nilai >= 85:
        print(nama_konversi,nilai_konversi,"A")
    elif nilai >= 80:
        print(nama_konversi,nilai_konversi,"A-")
    elif nilai >= 75:
        print(nama_konversi,nilai_konversi,"B+")
    elif nilai >= 70:
        print(nama_konversi,nilai_konversi,"B")
    elif nilai >= 65:
        print(nama_konversi,nilai_konversi,"C+")
    elif nilai >= 60:
        print(nama_konversi,nilai_konversi,"C")
    else:
        print(nama_konversi,nilai_konversi,"E")
else:
    print(nama_konversi,"Nilai yang anda masukkan tidak valid untuk dikonversi.")
print()