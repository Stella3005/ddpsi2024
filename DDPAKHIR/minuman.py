import streamlit as st

class Minuman:
    def __init__(self, nama, harga):
        self.nama = nama
        self.harga = harga

class Bioskop:
    def __init__(self):
        self.minuman = []

    def tambah_minuman(self, nama, harga):
        self.minuman.append(Minuman(nama, harga))

    def tampilkan_minuman(self):
        for i, minuman in enumerate(self.minuman, start=1):
            st.write(f"{i}. {minuman.nama} - Rp {minuman.harga:,}")

    def pesan_minuman(self):
        pesanan = st.selectbox("Pilih Minuman", [minuman.nama for minuman in self.minuman])
        
        # Input jumlah minuman yang ingin dipesan
        jumlah = st.number_input("Jumlah", min_value=1, value=1)

        if st.button("Pesan"):
            if pesanan:
                # Mencari harga minuman berdasarkan nama
                harga_minuman = next(minuman.harga for minuman in self.minuman if minuman.nama == pesanan)
                total_harga = harga_minuman * jumlah
                st.success(f"Anda memesan {jumlah} {pesanan}. Total harga: Rp {total_harga:,}")
            else:
                st.error("Silakan pilih minuman")

def main():
    bioskop = Bioskop()

    # Menambahkan minuman awal
    bioskop.tambah_minuman("Milo Dinosaurus", 45000)
    bioskop.tambah_minuman("Brown Sugar Milk", 35000)
    bioskop.tambah_minuman("Hot Tea", 28000)
    bioskop.tambah_minuman("Java Tea", 25000)
    bioskop.tambah_minuman("Lemon Tea", 22000)

    st.title("Daftar Minuman Bioskop")
    bioskop.tampilkan_minuman()

    st.title("Pesan Minuman")
    bioskop.pesan_minuman()

if __name__ == "__main__":
    main()
