
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(
    page_title="Bike Sharing Dashboard",
    page_icon="🚲",
    layout="wide"
)

st.title("🚲 Bike Sharing Analysis Dashboard")
st.write(
    "Dashboard untuk mengeksplorasi pola penyewaan sepeda "
    "berdasarkan jam, jenis hari, dan kondisi cuaca."
)

@st.cache_data
def load_data():
    base_dir = Path(__file__).resolve().parent.parent
    data = pd.read_csv(base_dir / "data" / "hour.csv")
    data["dteday"] = pd.to_datetime(data["dteday"])
    return data

df = load_data()

# Sidebar filters
st.sidebar.header("Filter Data")

day_option = st.sidebar.selectbox(
    "Jenis Hari",
    ["Semua", "Hari kerja", "Hari nonkerja"]
)

if day_option == "Hari kerja":
    filtered_df = df[df["workingday"] == 1]
elif day_option == "Hari nonkerja":
    filtered_df = df[df["workingday"] == 0]
else:
    filtered_df = df.copy()

# Summary metrics
col1, col2, col3 = st.columns(3)

col1.metric("Total Penyewaan", f"{filtered_df['cnt'].sum():,}")
col2.metric(
    "Rata-rata per Jam",
    f"{filtered_df['cnt'].mean():.1f}"
)
col3.metric(
    "Jumlah Catatan",
    f"{len(filtered_df):,}"
)

st.divider()

# Question 1: Hourly demand
st.header("1. Pola Penyewaan Berdasarkan Jam")

hourly = (
    filtered_df.groupby("hr")["cnt"]
    .mean()
    .reindex(range(24))
)

fig1, ax1 = plt.subplots(figsize=(12, 5))
sns.lineplot(x=hourly.index, y=hourly.values, marker="o", ax=ax1)
ax1.set(
    title="Rata-rata Penyewaan Sepeda per Jam",
    xlabel="Jam",
    ylabel="Rata-rata Penyewaan"
)
ax1.set_xticks(range(24))
ax1.grid(alpha=0.3)
st.pyplot(fig1)
plt.close(fig1)

st.caption(
    "Grafik menunjukkan perubahan rata-rata penyewaan pada "
    "setiap jam berdasarkan filter jenis hari yang dipilih."
)

# Question 2: Weather
st.header("2. Penyewaan Berdasarkan Kondisi Cuaca")

weather_labels = {
    1: "Cerah / sedikit berawan",
    2: "Berkabut / berawan",
    3: "Hujan ringan / kondisi buruk",
    4: "Cuaca buruk ekstrem"
}

weather = (
    filtered_df.groupby("weathersit")["cnt"]
    .mean()
    .reindex([1, 2, 3, 4])
    .dropna()
)

weather.index = [weather_labels[i] for i in weather.index]

fig2, ax2 = plt.subplots(figsize=(10, 5))
weather.plot(kind="bar", ax=ax2)
ax2.set(
    title="Rata-rata Penyewaan Berdasarkan Cuaca",
    xlabel="Kondisi Cuaca",
    ylabel="Rata-rata Penyewaan"
)
ax2.tick_params(axis="x", rotation=20)
fig2.tight_layout()
st.pyplot(fig2)
plt.close(fig2)

st.caption(
    "Kategori cuaca terburuk hanya memiliki sedikit observasi "
    "dalam dataset, sehingga hasilnya perlu ditafsirkan hati-hati."
)

# Advanced analysis: time periods
st.header("3. Penyewaan Berdasarkan Periode Hari")

period_df = filtered_df.copy()
period_df["Periode"] = pd.cut(
    period_df["hr"],
    bins=[-1, 5, 11, 17, 23],
    labels=[
        "Dini Hari (00–05)",
        "Pagi (06–11)",
        "Siang (12–17)",
        "Malam (18–23)"
    ]
)

period_demand = (
    period_df.groupby("Periode", observed=False)["cnt"]
    .mean()
    .dropna()
)

fig3, ax3 = plt.subplots(figsize=(10, 5))
period_demand.plot(kind="bar", ax=ax3)
ax3.set(
    title="Rata-rata Penyewaan per Periode Hari",
    xlabel="Periode Hari",
    ylabel="Rata-rata Penyewaan"
)
ax3.tick_params(axis="x", rotation=15)
fig3.tight_layout()
st.pyplot(fig3)
plt.close(fig3)

st.divider()

st.subheader("Kesimpulan")
st.write(
    "Pola penyewaan berbeda menurut jam dan jenis hari. "
    "Rata-rata penyewaan juga cenderung lebih tinggi pada cuaca "
    "yang lebih baik. Informasi ini dapat membantu perencanaan "
    "distribusi sepeda dan operasional."
)

st.info(
    "Catatan: beberapa tanggal tidak memiliki catatan untuk "
    "seluruh 24 jam. Dashboard menggunakan data yang tersedia "
    "tanpa menganggap jam yang tidak tercatat sebagai nol."
)
