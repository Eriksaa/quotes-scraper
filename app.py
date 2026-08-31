import streamlit as st
import pandas as pd

st.title("Dashboard Kutipan Tokoh")
st.write("Menampilkan hasil web scraping dan analisis kutipan")

# Membaca dataset dari project sebelumnya
df = pd.read_csv('quotes_dataset.csv')

# Menampilkan data mentah di halaman web
st.subheader("Data Mentah")
st.dataframe(df)