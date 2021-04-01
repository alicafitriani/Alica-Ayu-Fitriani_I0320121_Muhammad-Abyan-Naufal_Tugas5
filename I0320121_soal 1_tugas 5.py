# Input nama dan jenis kelamin
nama = input("Masukkan Nama Anda : ")
jenis_kelamin = input("Jenis Kelamin Anda (P/L) : ")
L = "Tuan"
P = "Nyonya"

# Memeriksa hasil input jenis kelamin
if jenis_kelamin == "P" :
    print('\nSelamat datang,',P,nama + '!')
elif jenis_kelamin == "L":
    print('\nSelamat datang,',L,nama + '!')
else:
    pass