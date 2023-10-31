from os import system
def judul ():
    system('cls')
    print('====================================')
    print('|      SELAMAT DATANG DI WARVO     |')
    print('|           WARUNG VOKASI          |')
    print('====================================')
    (input('Silahkann Tekan Enter: '))
    system('cls')
    total()


def menu_minuman():
    system('cls')
    print("========================================")
    print("|            DAFTAR MINUMAN            |")
    print("========================================")

    daftar_minuman = {
        1: "Teh Panas/Es      = Rp. 3.000",
        2: "Jeruk Panas/Es    = Rp. 3.000",
        3: "Kopi Susu         = Rp. 4.000",
        4: "Kopi Hitam        = Rp. 4.000",
        5: "Jahe Panas        = Rp. 4.000",
        6: "Wedang Secang     = Rp. 5.000",
    }

    for kode, minuman in daftar_minuman.items():
        print(f"[{kode}]: {minuman}")

    print("========================================")
    try:
        minum = {
            1:3000,
            2:3000,
            3:4000,
            4:4000,
            5:4000,
            6:5000,
        }
        kode_minum = int(input('Ketikkan kode minuman: '))
        if kode_minum in minum:
            jumlah_minum = int(input("Berapa jumlah pesanan anda?: "))
            total_minum = minum[kode_minum] * jumlah_minum
            return total_minum
        else:
            print("Pilih kode minuman yang tersedia.")
            system('cls')
            menu_minuman()
    except ValueError:
            print("Masukkan Anda tidak valid")
            menu_minuman()


def menu_makanan():
    system('cls')
    print("========================================")
    print("|            DAFTAR MAKANAN            |")
    print("========================================")
    daftar_makanan = {
        1:"Nasi Goreng         = Rp. 11.000",
        2:"Nasi Ayam Geprek    = Rp. 13.000",
        3:"Nasi Pecel Lele     = Rp. 10.000",
        4:"Nasi Ayam Kentucky  = Rp. 10.000",
        5:"Mie Ayam            = Rp. 7.000",
        6:"Bakso               = Rp. 7.000",
    }

    for kode,makan in daftar_makanan.items():
        print(f"[{kode}]: {makan}")

    print("========================================")

    try:
        makan = {
            1:11000,
            2:13000,
            3:10000,
        }
        kode_makan = int(input('Ketikkan Kode Makanan: '))
        if kode_makan in makan:
            jumlah_makan = int(input('Berapa jumlah pesanannya?: '))
            total_makan = makan[kode_makan] * jumlah_makan
            return total_makan
        else:
            print("Pilih sesuai yang ada didaftar")
            system('cls')
            menu_makanan()
    except ValueError:
        print("Masukkan anda tidak valid")
        menu_makanan()

def total():
    total_makanan = menu_makanan()
    total_minuman = menu_minuman()
    total_harga = total_makanan + total_minuman
    system('cls')
    print('======================================')
    print('              TOTAL HARGA             ')    
    print(f"Total harga adalah: Rp. {total_harga}")
    print('======================================')

judul()