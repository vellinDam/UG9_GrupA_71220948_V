

panjang = int(input("Masukkan Panjang :"))
lebar = int(input("Masukkan Lebar : "))
jari = int(input("Masukkan jari :"))

set_lingkarangan =(3.14*jari*jari)*0.5
persegi_panjang = (panjang*lebar)
total = set_lingkarangan+persegi_panjang

cat = int((total/15)+1)

print("Area tersebut membutuhkan",cat  ,"Kaleng Cat")


