import pandas as pd

contact = []

def tambah_kontak(nama, telp, alamat):
    kontak = {
        'nama' : nama,
        'telp' : telp,
        'alamat' : alamat
    }
    
    contact.append(kontak)

pertanyaan = True
while pertanyaan :
    nama = input("Masukan Nama :")
    telp = input("Masukan Telp :")
    alamat = input("Masukan Alamat : ")
    jawab = input("Tambah data lagi ? (Y/N)")

    tambah_kontak(nama,telp,alamat)
    
    if jawab == 'N':
        pertanyaan = False
    
df = pd.DataFrame(contact)

if df.empty:
  print("DataFrame Kosong")
else:
  print("DataFrame tidak kosong")
  
nama_file = 'List_Kontak.xlsx'
df.to_excel(nama_file, index = False)

print("Data telah disimpan pada file :", nama_file)