import requests

# Fungsi untuk menampilkan Asmaul Husna berdasarkan nomor
def get_husna_by_number(nomor):
    url = f"https://api.myquran.com/v2/husna/{nomor}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                husna = data["data"]
                print(f"Nomor: {husna['id']}")
                print(f"Nama: {husna['indo']} ({husna['arab']})")
                print(f"Latin: {husna['latin']}")
                print("\n")
            else:
                print("Data Asmaul Husna tidak ditemukan.")
        else:
            print(f"Error {response.status_code}: Gagal mendapatkan data.")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan semua Asmaul Husna
def get_all_husna():
    url = "https://api.myquran.com/v2/husna/semua"
    try:
        response = requests.get(url)
        response.raise_for_status()
        
        if response.status_code == 200:
            data = response.json()
            if "data" in data:
                husna_list = data["data"]
                for husna in husna_list:
                    print(f"Nomor: {husna['id']}")
                    print(f"Nama: {husna['indo']} ({husna['arab']})")
                    print(f"Latin: {husna['latin']}")
                    print("\n")
            else:
                print("Data Asmaul Husna tidak ditemukan.")
        else:
            print(f"Error {response.status_code}: Gagal mendapatkan data.")
    except requests.exceptions.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

# Fungsi untuk menampilkan Asmaul Husna dengan melanjutkan ke nomor urut berikutnya
def get_husna_with_continue(start_nomor):
    nomor = start_nomor
    while True:
        get_husna_by_number(nomor)
        
        # Menanyakan apakah ingin melanjutkan ke nomor urut berikutnya
        lanjut = input(f"Apakah Anda ingin melanjutkan ke Asmaul Husna nomor {nomor + 1}? (y/n atau tekan enter untuk lanjut): ").lower()
        
        if lanjut == "y" or lanjut == "":
            if nomor < 99:
                nomor += 1
            else:
                print("Ini adalah Asmaul Husna terakhir. Program selesai.")
                break
        elif lanjut == "n":
            print("Terima kasih, program selesai.")
            break
        else:
            print("Masukkan pilihan yang valid.")

def main():
    print("===== Menu Asmaul Husna =====")
    print("1. Menampilkan Asmaul Husna Berdasarkan Nomor")
    print("2. Menampilkan Semua Asmaul Husna")
    
    try:
        pilihan = int(input("Pilih menu (1 atau 2): "))
        
        if pilihan == 1:
            nomor = int(input("Masukkan nomor Asmaul Husna (1-99): "))
            if 1 <= nomor <= 99:
                get_husna_with_continue(nomor)
            else:
                print("Nomor tidak valid. Masukkan angka antara 1 hingga 99.")
        elif pilihan == 2:
            get_all_husna()
        else:
            print("Pilihan tidak valid. Masukkan 1 atau 2.")
    except ValueError:
        print("Masukkan pilihan yang valid.")

if __name__ == "__main__":
    main()
