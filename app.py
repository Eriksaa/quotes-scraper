import streamlit as st
import pandas as pd

st.title("Dashboard Kutipan Tokoh")
st.write("Eksplorasi dataset hasil web scraping secara interaktif")

# Membaca dataset dari project sebelumnya
df = pd.read_csv('quotes_dataset.csv')

# Membuat menu filter di sidebar
st.sidebar.header("Menu Pencarian")
daftar_penulis = df['author'].unique()
pilihan_penulis = st.sidebar.selectbox("Pilih Penulis:", ["Semua"] + list(daftar_penulis))

# Logika penyaringan data
if pilihan_penulis == "Semua":
    df_tampil = df
else:
    df_tampil = df[df['author'] == pilihan_penulis]

# Menampilkan hasil filter
st.subheader(f"Menampilkan Kutipan: {pilihan_penulis}")
st.dataframe(df_tampil)