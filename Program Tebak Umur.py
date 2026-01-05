import datetime, os, time

def tebakumur():
    while True:
        try:
            print("==========================================")
            print("=========== PROGRAM TEBAK UMUR ===========")
            print("==========================================")
            tanggal = int(input("Masukkan Tanggal : "))
            bulan = int(input("Masukkan Bulan : "))
            tahun = int(input("Masukkan Tahun : "))
        except ValueError:
            print("Masukkan angka!")
            continue

        if bulan < 1 or bulan > 12:
            print("Bulan harus antara 1 sampai 12!")
            continue

        try:
            tanggallahir = datetime.date(tahun, bulan, tanggal)
        except ValueError:
            print("Tanggal tidak valid untuk bulan dan tahun tersebut!")
            continue

        tanggalsekarang = datetime.date.today()
        kurangi = tanggalsekarang - tanggallahir
        umur = kurangi.days // 365

        if umur < 0:
            print("Anda belum lahir!")
            continue
        else:
            print("================ Loading =================")
            time.sleep(3)
            print(f"Umur anda sekarang adalah {umur} tahun")
            break
    while True:
        lanjut = input("Apakah anda ingin mencoba lagi (Y/N) : ")
        if lanjut == 'y' or lanjut == "Y":
            os.system("cls")
            tebakumur()
        elif lanjut == 'n' or lanjut == "N":
            print("Terima kasih telah mencoba!")
            break
        else:
            print("Input tidak valid. Silakan masukkan Y atau N")

if __name__ == "__main__":
    os.system("cls")
    tebakumur()