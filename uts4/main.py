import utils

while True:
    print("\n===== MENU BANGUN DATAR =====")
    print("1. Persegi")
    print("2. Persegi Panjang")
    print("3. Segitiga")
    print("4. Jajar Genjang")
    print("5. Layang-layang")
    print("6. Belah Ketupat")
    print("7. Trapesium")
    print("8. Lingkaran")
    print("9. Heksagon")
    print("10. Pentagon")
    print("11. Keluar")

    pilihan = input("Pilih bangun datar: ")

    if pilihan == "1":
        utils.persegi()
    elif pilihan == "2":
        utils.persegi_panjang()
    elif pilihan == "3":
        utils.segitiga()
    elif pilihan == "4":
        utils.jajar_genjang()
    elif pilihan == "5":
        utils.layang_layang()
    elif pilihan == "6":
        utils.belah_ketupat()
    elif pilihan == "7":
        utils.trapesium()
    elif pilihan == "8":
        utils.lingkaran()
    elif pilihan == "9":
        utils.heksagon()
    elif pilihan == "10":
        utils.pentagon()
    elif pilihan == "11":
        print("Terima kasih 🙏")
        break
    else:
        print("Pilihan tidak valid!")

    input("\nTekan ENTER untuk kembali ke menu...")