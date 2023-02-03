import streamlit as st
import pandas as pd
import time
import hydralit_components as hc
from streamlit_option_menu import option_menu
from side import Tampil, sidebar, about, info1, info2, info3, detailpref, style,footer


# KONFIRGURASI PAGE #HARUS DI AWAL
st.set_page_config(page_title='TUGAS KELOMPOK',
                   page_icon=':hotel:',
                   layout='wide',
                   initial_sidebar_state="collapsed"
                   )
st.markdown("""
<style>div[data-testid="stToolbar"] { display: none;}</style>
""", unsafe_allow_html=True)

# CREATE DATAFRAME
def ambil_data():
    df = pd.read_excel(
        io='hotel_jawabarat_tiket_fix.xlsx',
        engine='openpyxl',
    )
    return df


# ADD DATA FRAME
df = ambil_data()
#BACKGORUND
latar = """
<style>
[data-testid="stAppViewContainer"]{
background-image: url("https://cdn.discordapp.com/attachments/1038017092806512712/1070778864890028112/white_wallpaper_5_4k_hd_white-1920x1080.jpg");
background-size: 100%;
background-position: top left;
background-repeat: no-repeat;
background-attachment: local;
}

[data-testid="stHeader"] {
background: rgba(0,0,0,0);
}

.card {
background-color: rgba(0,0,0,0);
}
</style>
"""
st.markdown(latar, unsafe_allow_html=True)
# add_bg_from_local('white.jpg')
style()

with st.sidebar:
    selected = option_menu("Pytorch", ["Dashboard", "Detail Hotel",  "About"], menu_icon="cast",
                           icons=['house', 'search', "person"], default_index=0, orientation="vertical",
                           )


if selected == "Dashboard":
    
    with hc.HyLoader('Memuat Data', hc.Loaders.pacman, height=200):
        time.sleep(2)
        info1(df)
        info2(df)
        info3(df)

    with st.container():
        st.markdown("""
        <center><h1>Peta Data Hotel Jawa Barat</h1><h5>Berdasarkan Kabupaten dan Kota</h5></center>
        """, unsafe_allow_html=True)
        kolom1,kolom2,kolom3 = st.columns((1,12,1))
        with kolom2 :
            Tampil(df, "city")


elif selected == "Detail Hotel":
    with hc.HyLoader('Memuat Data', hc.Loaders.standard_loaders, height=200):
        time.sleep(2)
    detail, tipe = sidebar(df)
    st.markdown("""
            <center><h1>Detail Posisi Hotel Jawa Barat</h1></center>
            <center><h4>Sesuai koordinat Hotel</h4></center>
            """, unsafe_allow_html=True)
    col1, col2, col3 = st.columns((1,12,2), gap='large')
    with col2:
        Tampil(detail, "all")
    detailpref(detail, tipe)

elif selected == "About":
    with hc.HyLoader('Memuat Data', hc.Loaders.pacman, height=150):
        time.sleep(1)
    about()

footer()
