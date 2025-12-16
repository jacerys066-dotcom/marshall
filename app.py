import streamlit as st

# Set halaman lebih modern
st.set_page_config(
    page_title="Profil Marshall Ramdhani",
    layout="centered"
)

# Sidebar menu
menu = st.sidebar.selectbox("Menu", ["Home", "Profil", "About"])

# ===== Halaman Home =====
if menu == "Home":
    st.markdown("<h1 style='text-align: center; color: #4B0082;'>🌟 Selamat Datang di Aplikasi</h1>", unsafe_allow_html=True)
    st.write("Pilih menu **Profil** di sidebar untuk melihat profil **Marshall Ramdhani**.")
    st.image(
        "https://raw.githubusercontent.com/jacerys066-dotcom/marshall/fda35c750e15b5c3efb175dcad73aa74d68e938b/foto_profil.png",
        width=250
    )

# ===== Halaman Profil =====
elif menu == "Profil":
    st.markdown("<h1 style='text-align: center; color: #2E8B57;'>👤 Profil Marshall Ramdhani</h1>", unsafe_allow_html=True)
    
    # Layout 2 kolom
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.image(
            "https://raw.githubusercontent.com/jacerys066-dotcom/marshall/fda35c750e15b5c3efb175dcad73aa74d68e938b/foto_profil.png",
            width=180,
            caption="Marshall Ramdhani"
        )
    
    with col2:
        st.markdown("<h3 style='color: #4B0082;'>Nama</h3>", unsafe_allow_html=True)
        st.write("Marshall Ramdhani")
        
        st.markdown("<h3 style='color: #4B0082;'>Peran</h3>", unsafe_allow_html=True)
        st.write("Actuarial Science")

    st.markdown("---")

# ===== Halaman About =====
elif menu == "About":
    st.markdown("<h1 style='text-align: center; color: #FF4500;'>📖 Tentang Aplikasi</h1>", unsafe_allow_html=True)
    st.write("""
    Ini adalah aplikasi demo **multi-halaman Streamlit** yang menampilkan profil **Marshall Ramdhani**.
    Desain dibuat lebih unik dan modern dengan layout kolom dan foto bulat.
    """)
