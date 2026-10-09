# Bike Sharing Analysis Dashboard

## Deskripsi

Proyek ini merupakan analisis data penyewaan sepeda menggunakan **Bike Sharing Dataset** dari UCI Machine Learning Repository. Analisis berfokus pada pola penyewaan sepeda berdasarkan jam, jenis hari, dan kondisi cuaca selama periode 2011–2012.

Hasil analisis disajikan melalui dashboard interaktif menggunakan Streamlit untuk membantu memahami pola permintaan penyewaan sepeda.

## Dashboard

Dashboard dapat diakses secara online melalui tautan berikut:

**[Bike Sharing Analysis Dashboard](https://bike-sharing-dashboard-gembnjmbjxzwcyu6onk5ur.streamlit.app/)**

## Pertanyaan Bisnis

1. Bagaimana pola rata-rata jumlah penyewaan sepeda per jam pada hari kerja dibandingkan hari nonkerja selama periode 2011–2012?
2. Bagaimana perbedaan rata-rata jumlah penyewaan sepeda berdasarkan kondisi cuaca selama periode 2011–2012?

## Dataset

Proyek ini menggunakan Bike Sharing Dataset yang berisi data penyewaan sepeda selama tahun 2011–2012.

* `hour.csv` — **dataset utama (`main_data`)** yang berisi catatan penyewaan sepeda per jam. Dataset ini digunakan dalam proses analisis, visualisasi, dan dashboard.
* `day.csv` — dataset harian bawaan dari sumber yang sama, disertakan sebagai data pendukung dan tidak digunakan dalam analisis utama.

Analisis utama menggunakan `hour.csv` karena menyediakan informasi per jam yang sesuai dengan pertanyaan bisnis.

## Proses Analisis

1. **Data Wrangling:** Memuat dataset, memeriksa tipe data, nilai kosong, duplikasi, dan konsistensi data.
2. **Exploratory Data Analysis (EDA):** Menganalisis pola rata-rata penyewaan berdasarkan jam, jenis hari, dan kondisi cuaca.
3. **Analisis Lanjutan:** Mengelompokkan jam ke dalam periode dini hari, pagi, siang, dan malam menggunakan teknik binning.
4. **Visualisasi Data:** Menyajikan hasil analisis melalui grafik untuk mempermudah interpretasi.
5. **Dashboard Interaktif:** Menggunakan Streamlit untuk menampilkan visualisasi dan memungkinkan pengguna memfilter jenis hari.

## Temuan Utama

* Pola penyewaan sepeda berbeda antara hari kerja dan hari nonkerja. Hari kerja menunjukkan pola permintaan yang lebih menonjol pada jam-jam perjalanan, sedangkan hari nonkerja memiliki pola yang berbeda.
* Rata-rata penyewaan cenderung lebih tinggi pada kondisi cuaca yang lebih baik dan menurun ketika kondisi cuaca memburuk.
* Data mencakup periode 1 Januari 2011 hingga 31 Desember 2012.
* Beberapa tanggal memiliki catatan kurang dari 24 jam. Oleh karena itu, ketidaklengkapan data per jam perlu dipertimbangkan saat menafsirkan hasil analisis.

## Rekomendasi

* Mengoptimalkan distribusi dan ketersediaan sepeda berdasarkan jam dengan permintaan tinggi.
* Mempertimbangkan kondisi cuaca saat merencanakan operasional dan ketersediaan sepeda.
* Memantau kelengkapan pencatatan data agar analisis dan keputusan operasional lebih akurat.

## Struktur Proyek

```text
submission/
├── dashboard/
│   └── app.py
├── data/
│   ├── hour.csv
│   └── day.csv
├── notebook.ipynb
├── README.md
├── requirements.txt
└── url.txt
```

Keterangan:

* `dashboard/app.py`: kode sumber dashboard Streamlit.
* `data/hour.csv`: dataset utama untuk analisis dan dashboard.
* `data/day.csv`: dataset harian pendukung.
* `notebook.ipynb`: notebook yang berisi proses analisis data.
* `requirements.txt`: daftar library Python yang dibutuhkan.
* `url.txt`: tautan dashboard yang telah dipublikasikan.

## Cara Menjalankan Dashboard

### Persyaratan

* Python telah terinstal.
* Terminal atau command prompt tersedia.
* Library yang tercantum dalam `requirements.txt` telah diinstal.

### Langkah-langkah

1. Buka terminal pada direktori proyek.

2. Instal library yang diperlukan:

   ```bash
   python -m pip install -r requirements.txt
   ```

3. Jalankan dashboard dari direktori proyek:

   ```bash
   python -m streamlit run dashboard/app.py
   ```

4. Buka alamat lokal yang ditampilkan oleh Streamlit pada terminal.

**Catatan:** Dashboard harus membaca dataset melalui path yang sesuai dengan lokasi `hour.csv`. Jika struktur folder diubah, path dataset pada `app.py` perlu disesuaikan.

## Teknologi yang Digunakan

* Python
* Pandas
* Matplotlib
* Seaborn
* Streamlit