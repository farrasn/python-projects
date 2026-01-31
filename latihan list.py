barang_list = []

while True:
    print("\n=== MENU ===")
    print("1. tambah barang")
    print("2. edit barang")
    print("3. hapus barang")
    print("4. cetak barang")
    print("5. keluar")
    pilihan = input("masukkan pilihan 1 - 2 - 3 - 4 - 5 : ")

    if pilihan == "1":
        print("\n--- TAMBAH BARANG ---")
        kode = int(input("masukkan kode barang : "))
        nama = input("masukkan nama barang : ")
        harga = float(input("masukkan harga barang : "))
        stock = int(input("masukkan stock barang : "))
        barang_list.append([kode, nama, harga, stock])
        print("barang berhasil ditambahkan")

    elif pilihan == "2":
        print("\n--- EDIT BARANG ---")
        edit_kode = int(input("masukkan kode barang yang akan di edit : "))
        for barang in barang_list:
            if barang [0] == edit_kode:
                print("data barang ditemukan")
                nama = input("masukkan nama barang baru : ")
                harga = float(input("masukkan harga barang baru : ")) 
                stock = int(input("masukkan stock barang baru : ")) 
                barang[0] = nama
                barang[1] = harga
                barang[2] = stock
                print("data barang berhasil diubah")
                break

    elif pilihan == "3":
        print("\n--- HAPUS BARANG ---")
        hapus = int(input("masukkan kode barang yang akan di hapus : "))
        for barang in barang_list:
            if barang [0] == hapus:
                barang_list.remove(barang)
                print("barang berhasil dihapus")
                break

    elif pilihan == "4":
        print("\n--- CETAK BARANG ---")
        print("kode\tnama\tharga\tstock")
        for barang in barang_list:
            print(f"{barang[0]}\t{barang[1]}\t{barang[2]}\t{barang[3]}")

    elif pilihan == "5":
        print("keluar")
        break

