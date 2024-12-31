import streamlit as st
from reguler import main as reguler_main  
from premium import main as premium_main  
from minuman import main as minuman_main
from makanan import main as makanan_main

# Judul Aplikasi
st.title("Selamat Datang di XXI NF ACADEMI")

# Menambahkan Gambar
st.image("Cinema_XXI.svg.png")

# Deskripsi Singkat
st.write("Silakan masukkan nama pengguna atau email Anda.")

# Formulir Masuk
with st.form("form_masuk"):
    nama_pengguna = st.text_input("Nama Pengguna atau Email")
    tombol_submit = st.form_submit_button("Masuk")

# Logika Setelah Submit
if tombol_submit:
    if nama_pengguna.strip():
        st.session_state.logged_in = True  # Set logged_in state to True
        st.session_state.username = nama_pengguna  # Store username
        st.success(f"Selamat datang, {nama_pengguna}!")
    else:
        st.error("Nama pengguna atau email tidak boleh kosong.")

# Cek apakah pengguna sudah login
if "logged_in" in st.session_state and st.session_state.logged_in:
    # Fungsi untuk menampilkan halaman sesuai dengan pilihan
    def show_page(page):
        if page == "Tiket Reguler":
            reguler_main()  
        elif page == "Tiket Premium":
            premium_main()
        elif page == "Menu Minuman":
            minuman_main()
        elif page == "Menu Makanan":
            makanan_main()
        else:
            st.write("Halaman belum tersedia.")

    # Sidebar untuk navigasi
    st.sidebar.title("MENU")
    page = st.sidebar.radio("Pilih Tiket", 
                             ("Tiket Reguler", "Tiket Premium", "Menu Minuman", "Menu Makanan"))

    # Menampilkan halaman berdasarkan pilihan
    show_page(page)
else:
    st.write("Silakan login untuk mengakses menu.")
