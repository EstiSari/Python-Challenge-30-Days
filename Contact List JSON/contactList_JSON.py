import json
contact = []

def tambah_kontak(nama, telp, alamat):
    kontak = {
        'nama' : nama,
        'telp' : telp,
        'alamat' : alamat
    }
    contact.append(kontak)

def simpan_json():
    with open('kontak.json', 'w') as file:
        json.dump(contact, file)


print('Masukan Data Kontak')
pertanyaan = True
while pertanyaan:
    
    nama = input("Masukan Nama :")
    telp = input("Masukan Telp :")
    alamat = input("Masukan Alamat : ")
    jawab = input("Tambah data lagi ? (Y/N)")
    
    tambah_kontak(nama, telp, alamat)
    
    
    if jawab == 'N' :
        pertanyaan = False
    
    
simpan_json()
print(contact)

