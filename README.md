# Quotes Scraper & Data Analysis

Proyek ini adalah eksperimen *web scraping end-to-end* dan *Exploratory Data Analysis* (EDA) dasar menggunakan Python. Proyek ini mendemonstrasikan proses pengambilan data mentah dari internet hingga menjadi wawasan visual.

Tujuan Proyek
Mengumpulkan data kutipan tokoh terkenal secara otomatis, menangani data yang kosong, dan mencari tahu tokoh mana yang kutipannya paling sering muncul.

Teknologi yang Digunakan
* Web Scraping: `requests`, `beautifulsoup4`
* Data Preprocessing: `pandas`
* Data Visualization: `matplotlib`, `seaborn`

Alur Kerja
1. Ekstraksi: Menarik 100 baris data kutipan secara otomatis dari halaman 1-10 di *quotes.toscrape.com*.
2. Penyimpanan: Menyimpan hasil ekstraksi ke dalam format tabular `quotes_dataset.csv`.
3. Pembersihan: Menangani *missing values* (nilai kosong) pada kolom *tags* agar siap dianalisis.
4. Visualisasi: Menghasilkan *bar chart* untuk melihat peringkat penulis dengan kutipan terbanyak.