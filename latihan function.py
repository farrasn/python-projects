# function

def tambah(*angka): # function dengan parameter tidak terbatas
    hasil = 0
    for a in angka:
        hasil += a
    return hasil

def kurang(*angka): # function dengan parameter tidak terbatas
    hasil = angka[0]
    for a in angka[1:]:
        hasil -= a
    return hasil

def kali(*angka): # function dengan parameter tidak terbatas
    hasil = 1
    for a in angka:
        hasil *= a
    return hasil

def bagi(*angka): # function denga parameter tidak terbatas
    hasil = angka[0]
    for a in angka[1:]:
        hasil /= a
    return hasil

# program

print("==================")
print("pilih operasi : ")
print("1. tambah\n2. kurang\n3. kali\n4. bagi")

pilihan = input("masukkan pilihan 1 - 4 : ")

angka_1 = float(input("masukkan angka ke 1 : ")) # float saat pembagian nilainya bisa pakai desimal
angka_2 = float(input("masukkan angka ke 2 : ")) # float saat pembagian nilainya bisa pakai desimal

if pilihan == "1":
    print(f"hasil: {tambah(angka_1, angka_2)}")

elif pilihan == "2":
    print(f"hasil: {kurang(angka_1, angka_2)}")

elif pilihan == "3":
    print(f"hasil: {kali(angka_1, angka_2)}")

elif pilihan == "4":
    print(f"hasil: {bagi(angka_1, angka_2)}")
