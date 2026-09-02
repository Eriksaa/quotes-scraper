import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Dashboard Kutipan Tokoh")
st.write("Eksplorasi dataset hasil web scraping secara interaktif")

# Membaca dataset dari project sebelumnya
df = pd.read_csv('quotes_dataset.csv')

# Filter sidebar
st.sidebar.header("Menu Pencarian")
pilihan_penulis = st.sidebar.selectbox("Pilih Penulis:", ["Semua"] + list(df['author'].unique()))

if pilihan_penulis == "Semua":
    df_tampil = df
else:
    df_tampil = df[df['author'] == pilihan_penulis]

st.subheader(f"Kutipan: {pilihan_penulis}")
st.dataframe(df_tampil)

# Memasukkan visualisasi grafik Top 5 Penulis
if pilihan_penulis == "Semua":
    st.subheader("Top 5 Penulis Terpopuler")
    top_authors = df['author'].value_counts().head(5)
    
    fig, ax = plt.subplots(figsize=(8, 4))
    sns.barplot(x=top_authors.values, y=top_authors.index, palette='viridis', ax=ax)
    ax.set_xlabel('Jumlah Kutipan')
    ax.set_ylabel('Nama Penulis')
    
    # Render grafik di Streamlit
    st.pyplot(fig)