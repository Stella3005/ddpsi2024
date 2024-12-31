import streamlit as st

class Film:
    def __init__(self, nama, harga, jam_tayang, jumlah_kursi):
        self.nama = nama
        self.harga = harga
        self.jam_tayang = jam_tayang
        self.jumlah_kursi = jumlah_kursi
        self.kursi_terjual = 0
        self.kursi_tersedia = [f"Kursi {i+1}" for i in range(jumlah_kursi)]  # Daftar kursi

    def tampilkan_info(self):
        st.write(f"Nama Film: {self.nama}")
        st.write(f"Harga: Rp {self.harga:,}")
        st.write(f"Jam Tayang: {self.jam_tayang}")
        st.write(f"Jumlah Kursi: {self.jumlah_kursi}")
        st.write(f"Kursi Terjual: {self.kursi_terjual}")

    def beli_tiket(self, jumlah, kursi_pilihan):
        if jumlah <= self.jumlah_kursi - self.kursi_terjual:
            self.kursi_terjual += jumlah
            for kursi in kursi_pilihan:
                self.kursi_tersedia.remove(kursi)  # Hapus kursi dari daftar tersedia
            total_harga = self.harga * jumlah
            st.success(f"Tiket berhasil dibeli untuk {', '.join(kursi_pilihan)}. Total harga: Rp {total_harga:,}")
            return True  # Mengembalikan True jika pembelian berhasil
        else:
            st.error("Kursi tidak cukup.")
            return False  # Mengembalikan False jika tidak cukup kursi

class Bioskop:
    def __init__(self):
        self.daftar_film = []

    def tambah_film(self, film):
        self.daftar_film.append(film)

    def tampilkan_daftar_film(self):
        for i, film in enumerate(self.daftar_film, start=1):
            st.write(f"{i}. {film.nama}")

def main():
    bioskop = Bioskop()

    film1 = Film("Wicked", 50000, "13:30", 50)
    film2 = Film("Moana", 50000, "14:25", 50)
    film3 = Film("Avengers End Game", 50000, "14:00", 50)
    film4 = Film("Pengabdi Setan", 50000, "15:10", 50)
    film5 = Film("Miracle in Cell No.7", 50000, "16:20", 50)

    bioskop.tambah_film(film1)
    bioskop.tambah_film(film2)
    bioskop.tambah_film(film3)
    bioskop.tambah_film(film4)
    bioskop.tambah_film(film5)

    st.title("Daftar Tiket Premium")

    # Menampilkan gambar film secara horizontal
    cols = st.columns(len(bioskop.daftar_film))
    
    images = ["wicked.jpg", "moan.jpg", "ini avng.jpeg", "panggonan.jpeg", "miracle.jpeg"]
    
    for col, film, image in zip(cols, bioskop.daftar_film, images):
        with col:
            st.image(image, width=100)
            st.write(film.nama)

    pilihan_film = st.selectbox("Pilih Film", [film.nama for film in bioskop.daftar_film])

    for film in bioskop.daftar_film:
        if film.nama == pilihan_film:
            film.tampilkan_info()

            jumlah_tiket = st.number_input("Jumlah Tiket", min_value=1)

            # Menampilkan pilihan kursi dengan tampilan kotak-kotak
            if jumlah_tiket > 0:
                st.write("Pilih Kursi:")
                selected_kursi = []
                cols_kursi = st.columns(5)  # Misalnya kita ingin menampilkan hingga 10 kolom untuk kursi

                for i in range(film.jumlah_kursi):
                    with cols_kursi[i % 5]:  # Menggunakan modulus untuk mengatur kolom
                        if film.kursi_tersedia:
                            is_checked = st.checkbox(f"{film.kursi_tersedia[i]}", key=f"kursi_{film.kursi_tersedia[i]}")
                            if is_checked:
                                selected_kursi.append(film.kursi_tersedia[i])

                if st.button("Beli Tiket"):
                    if len(selected_kursi) == jumlah_tiket:
                        if film.beli_tiket(jumlah_tiket, selected_kursi):
                            # Jika pembelian berhasil, tampilkan informasi terbaru
                            film.tampilkan_info()  # Tampilkan info terbaru termasuk kursi terjual
                    else:
                        st.error("Silakan pilih jumlah kursi yang sesuai dengan tiket yang dibeli.")

if __name__ == "__main__":
    main()
