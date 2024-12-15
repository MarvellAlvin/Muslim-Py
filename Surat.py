import requests

# Fungsi untuk mendapatkan daftar semua surat
def get_all_surahs():
    url = "https://api.myquran.com/v2/quran/surat/semua"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            return data["data"]
        else:
            print("Data surat tidak ditemukan.")
            return None
    else:
        print("Terjadi kesalahan saat mengambil data surat.")
        return None

# Fungsi untuk mendapatkan informasi surat berdasarkan nomor
def get_surat_by_number(number):
    url = f"https://api.myquran.com/v2/quran/surat/{number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            return data["data"]
        else:
            print("Data surat tidak ditemukan.")
            return None
    else:
        print("Terjadi kesalahan saat mengambil data surat.")
        return None

# Fungsi untuk mendapatkan ayat berdasarkan nomor surat dan nomor ayat
def get_ayat_by_number(surat_number, ayat_number):
    url = f"https://api.myquran.com/v2/quran/ayat/{surat_number}/{ayat_number}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        if "data" in data:
            ayat_data = data["data"][0]
            return ayat_data
        else:
            print("Data ayat tidak ditemukan.")
            return None
    else:
        print("Terjadi kesalahan saat mengambil data ayat.")
        return None

def main():
    print("===== Daftar Semua Surat Al-Quran =====")
    
    # Mendapatkan daftar semua surat
    surahs = get_all_surahs()
    
    if surahs:
        # Menampilkan daftar surat
        print("Daftar Surat Al-Quran (Nomor 1-114):")
        for i, surat in enumerate(surahs):
            print(f"{i+1}. {surat['name_id']}")

        # Meminta input nomor surat dari pengguna
        try:
            surat_choice = int(input("Silahkan pilih nomor surat yang ingin ditampilkan lebih detail: "))
            if 1 <= surat_choice <= 114:
                # Menampilkan detail surat berdasarkan pilihan nomor
                surat_data = get_surat_by_number(surat_choice)
                
                if surat_data:
                    print(f"\nInformasi Surat Al-Quran Nomor {surat_choice}:")
                    print(f"Nama Surat: {surat_data['name_id']} ({surat_data['name_short']})")
                    print(f"Nama Panjang: {surat_data['name_long']}")
                    print(f"Arti: {surat_data['translation_id']}")
                    print(f"Jumlah Ayat: {surat_data['number_of_verses']}")
                    print(f"Surat ini adalah surat {surat_data['revelation_id']}")
                    print(f"Tafsir: {surat_data['tafsir']}")
                    print(f"Audio URL: {surat_data['audio_url']}")
                    
                    # Meminta input nomor ayat dari pengguna
                    try:
                        ayat_choice = int(input(f"Masukkan nomor ayat yang ingin ditampilkan (1-{surat_data['number_of_verses']}): "))
                        if 1 <= ayat_choice <= int(surat_data['number_of_verses']):
                            while True:
                                # Menampilkan ayat berdasarkan nomor surat dan nomor ayat
                                ayat_data = get_ayat_by_number(surat_choice, ayat_choice)
                                
                                if ayat_data:
                                    # Menampilkan informasi ayat
                                    print(f"\nAyat {ayat_choice} dari Surat {surat_data['name_id']}:")
                                    print(f"Ayat (Arab): {ayat_data['arab']}")
                                    print(f"Ayat (Latin): {ayat_data['latin']}")
                                    print(f"Terjemahan: {ayat_data['text']}")
                                    print(f"Audio URL: {ayat_data['audio']}")
                                    
                                    # Menanyakan apakah ingin melanjutkan ke ayat selanjutnya
                                    lanjut = input(f"Apakah Anda ingin melanjutkan ke Ayat {ayat_choice + 1}? (y/n): ").lower()
                                    if lanjut == "y":
                                        if ayat_choice < int(surat_data['number_of_verses']):
                                            ayat_choice += 1
                                        else:
                                            print("Tidak ada ayat selanjutnya. Program selesai.")
                                            break
                                    else:
                                        print("Terima kasih, program selesai.")
                                        break
                        else:
                            print(f"Nomor ayat harus antara 1 dan {surat_data['number_of_verses']}.")
                    except ValueError:
                        print("Masukkan nomor ayat yang valid.")
            else:
                print("Nomor surat tidak valid. Pilih nomor antara 1 dan 114.")
        except ValueError:
            print("Masukkan nomor yang valid.")
    else:
        print("Gagal mendapatkan daftar surat.")

if __name__ == "__main__":
    main()
