import random

print('Masukan batas angka untuk mendapatkan angka random. C/n (1-10)')
b_awal = int(input('Dari angka : '))
b_akhir = int(input('Sampai angka : '))

hasil = random.randint(b_awal, b_akhir)
print(hasil)







