import streamlit as st

class MakananBioskop:
    def __init__(self, nama_makanan, harga):
        self.nama_makanan = nama_makanan
        self.harga = harga
        self.jumlah_terjual = 0

    def jual_makanan(self, jumlah):
        if jumlah <= 0:
            st.error("Jumlah makanan harus lebih dari 0.")
            return
        self.jumlah_terjual += jumlah
        total_harga = self.harga * jumlah
        st.success(f"{jumlah} {self.nama_makanan} berhasil dijual.")
        st.write(f"Total harga: Rp {total_harga:,}")

    def tampilkan_info(self):
        # Menggunakan markdown untuk format yang lebih baik
        st.markdown(f"### {self.nama_makanan}")
        st.write(f"- **Harga:** Rp {self.harga:,}")
        st.write(f"- **Jumlah Terjual:** {self.jumlah_terjual}\n")

def menu():
    st.title("Daftar Makanan Bioskop")
    


def main():
    # Inisialisasi daftar makanan
    makanan_list = [
        MakananBioskop("Popcorn", 25000),
        MakananBioskop("Popmie", 15000),
        MakananBioskop("Nachos", 45000),
        MakananBioskop("Burger", 50000),
        MakananBioskop("Waffle", 20000)
    ]

    # Menyimpan daftar makanan di session state
    if 'makanan_list' not in st.session_state:
        st.session_state.makanan_list = makanan_list

    # Menampilkan menu
    menu()

    # Pilihan pengguna untuk menu
    pilihan = st.selectbox("Pilih menu (1-2)", ["1", "2"])

    if pilihan == '1':
        # Menampilkan daftar makanan dengan format yang lebih rapi
        for makanan in st.session_state.makanan_list:
            makanan.tampilkan_info()
    
    elif pilihan == '2':
        nama_makanan = st.selectbox("Masukkan nama makanan", [makanan.nama_makanan for makanan in st.session_state.makanan_list]).strip()
        jumlah = st.number_input("Masukkan jumlah yang ingin dibeli", min_value=1) 

        if st.button("Pesan"):
            found = False
            for makanan in st.session_state.makanan_list:
                if makanan.nama_makanan == nama_makanan:
                    makanan.jual_makanan(jumlah)
                    found = True
                    break
            
            if not found:
                st.error("Makanan tidak ditemukan. Silakan coba lagi.")

if __name__ == "__main__":
    main()
