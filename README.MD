
# Bike Sharing Analysis Dashboard

## Deskripsi
Proyek analisis data penyewaan sepeda berdasarkan jam, jenis hari, dan kondisi cuaca menggunakan dataset Bike Sharing.

## Pertanyaan Bisnis
1. Bagaimana pola rata-rata jumlah penyewaan sepeda per jam pada hari kerja dibandingkan hari nonkerja selama periode 2011–2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan berdasarkan kondisi cuaca selama periode 2011–2012?

## Dataset
Dataset yang digunakan adalah `hour.csv`, yang berisi catatan penyewaan sepeda per jam selama tahun 2011–2012.

## Proses Analisis
- Data wrangling dan pemeriksaan kualitas data.
- Exploratory Data Analysis (EDA).
- Analisis lanjutan menggunakan binning periode hari.
- Visualisasi interaktif menggunakan Streamlit.

## Cara Menjalankan
1. Install Python.
2. Install library dengan `python -m pip install -r requirements.txt`.
3. Jalankan dashboard dengan `python -m streamlit run app.py`.

## Temuan Utama
- Pola penyewaan berbeda berdasarkan jam dan jenis hari.
- Rata-rata penyewaan cenderung lebih tinggi pada cuaca yang lebih baik.
- Beberapa tanggal memiliki catatan kurang dari 24 jam, sehingga kelengkapan data perlu dipertimbangkan.

## Rekomendasi
- Optimalkan distribusi sepeda berdasarkan jam dengan permintaan tinggi.
- Pertimbangkan kondisi cuaca saat merencanakan operasional.
- Pantau kelengkapan data untuk mendukung keputusan yang lebih akurat.