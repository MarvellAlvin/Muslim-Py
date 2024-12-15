import requests
import datetime

# Fungsi untuk mendapatkan daftar kode kota
def get_kode_kota(nama_kota):
    url = f"https://api.myquran.com/v2/sholat/kota/cari/{nama_kota}"
    try:
        response = requests.get(url)
        response.raise_for_status()

        # Parse data sebagai JSON
        data = response.json()

        # Pastikan data valid dan sesuai format
        if data.get("status") and "data" in data:
            hasil = data["data"]
            if len(hasil) == 1:
                return hasil[0]["id"], hasil[0]["lokasi"]
            elif len(hasil) > 1:
                print(f"Ditemukan beberapa hasil untuk '{nama_kota}':")
                for i, kota in enumerate(hasil):
                    print(f"{i+1}. {kota['lokasi']} (Kode: {kota['id']})")
                pilihan = int(input("Pilih nomor kota yang sesuai: ")) - 1
                if 0 <= pilihan < len(hasil):
                    return hasil[pilihan]["id"], hasil[pilihan]["lokasi"]
                else:
                    print("Pilihan tidak valid.")
            else:
                print(f"Tidak ditemukan hasil untuk '{nama_kota}'.")
        else:
            print("Data dari API tidak sesuai format yang diharapkan.")
    except requests.exceptions.RequestException as e:
        print("Gagal mendapatkan daftar kota:", e)
    return None, None

# Fungsi untuk mendapatkan jadwal sholat
def get_jadwal_sholat(kode_kota, tanggal):
    url = f"https://api.myquran.com/v2/sholat/jadwal/{kode_kota}/{tanggal}"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        
        if data["status"]:
            jadwal = data["data"]["jadwal"]
            print(f"\nJadwal Sholat di {data['data']['lokasi']} ({data['data']['daerah']}) pada {jadwal['tanggal']}:")
            print(f"Imsak: {jadwal['imsak']}")
            print(f"Subuh: {jadwal['subuh']}")
            print(f"Terbit: {jadwal['terbit']}")
            print(f"Dhuha: {jadwal['dhuha']}")
            print(f"Dzuhur: {jadwal['dzuhur']}")
            print(f"Ashar: {jadwal['ashar']}")
            print(f"Maghrib: {jadwal['maghrib']}")
            print(f"Isya: {jadwal['isya']}")
        else:
            print("Data tidak ditemukan.")
    except requests.exceptions.RequestException as e:
        print("Gagal mengambil data jadwal sholat:", e)

# Program Utama
def main():
    print("===== Jadwal Sholat Harian =====")
    nama_kota = input("Masukkan nama kota: ")

    # Menanyakan apakah pengguna ingin menggunakan tanggal hari ini
    pilih_tanggal = input("Gunakan tanggal hari ini? (y/n): ").lower()
    
    if pilih_tanggal == 'y':
        tanggal = datetime.datetime.today().strftime('%Y-%m-%d')  # Mendapatkan tanggal hari ini
    else:
        tanggal = input("Masukkan tanggal (format yyyy-mm-dd): ")

    # Validasi format tanggal
    try:
        datetime.datetime.strptime(tanggal, "%Y-%m-%d")
    except ValueError:
        print("Format tanggal tidak valid. Gunakan format yyyy-mm-dd.")
        return

    # Cari kode kota berdasarkan nama kota
    kode_kota, lokasi = get_kode_kota(nama_kota)
    if kode_kota:
        print(f"Mengambil jadwal sholat untuk {lokasi} pada {tanggal}...")
        get_jadwal_sholat(kode_kota, tanggal)
    else:
        print("Gagal menemukan kode kota.")

if __name__ == "__main__":
    main()
