# Import semua library yang dibutuhkan
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Judul Dashboard
st.title('Dashboard Analisis Polusi Udara dan Cuaca')

# Gathering Data - Mengupload file CSV
st.header("1. Upload Dataset")


# Membaca dataset
air_data = pd.read_csv("https://raw.githubusercontent.com/rachelfasella/Projek-Analisis-Data/refs/heads/main/PRSA_Data.csv")

# Menampilkan preview dataset
st.subheader("Preview Dataset")
st.write(air_data.head())

# Assessing Data - Memeriksa Missing Values, Duplicate dan Tipe Data
st.header("2. Assessing Data")

# Missing values
st.subheader("a. Missing Values")
missing_value = air_data.isnull().sum()
st.write(missing_value)

# Duplikasi data
st.subheader("b. Data Duplikasi")
duplicates = air_data.duplicated().sum()
st.write(f"Jumlah Data yang Duplikasi: {duplicates}")

# Tipe data
st.subheader("c. Tipe Data dari Masing-masing Kolom")
st.write(air_data.dtypes)

# Cleaning Data - Menghilangkan Missing Values
st.header("3. Cleaning Data")
st.markdown("""
- **Metode yang digunakan untuk membersihkan data:**
- Missing value diatasi dengan metode interpolasi.
""")

# Membersihkan Missing Values dengan interpolasi pada kolom numerik
numeric_cols = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3', 'TEMP', 'PRES', 'DEWP', 'RAIN', 'WSPM']
for col in numeric_cols:
    air_data[col] = air_data[col].interpolate(method='linear', limit_direction='forward')

# Forward fill untuk kolom kategori
air_data['wd'] = air_data['wd'].ffill()

# Memeriksa kembali Missing Values setelah cleaning
st.subheader("Hasil Setelah Cleaning")
missing_value_cleaned = air_data.isnull().sum()
st.write(missing_value_cleaned)

# Visualisasi dan Analisis Data
st.header("4. Exploratory Data Analysis (EDA)")

st.subheader("a. Pengaruh Intensitas Hujan terhadap Polusi Udara")
st.markdown("**Pengaruh Curah Hujan terhadap PM2.5**")

# Visualisasi 1: Pengaruh RAIN terhadap PM2.5, NO2, CO
plt.figure(figsize=(18, 6))

# Subplot untuk PM2.5
plt.subplot(1, 3, 1)
sns.scatterplot(x='RAIN', y='PM2.5', data=air_data)
plt.title('Pengaruh Curah Hujan terhadap PM2.5')


st.pyplot(plt.gcf())

# Analisis Karakteristik Polusi berdasarkan waktu
st.subheader("b. Perbandingan Karakteristik Polusi Berdasarkan Waktu (bulan dengan tahun) ")

plt.figure(figsize=(18, 18))

# Subplot untuk PM2.5 berdasarkan jbulan
plt.subplot(3, 1, 1)
sns.lineplot(x='hour', y='PM2.5', hue='month', data=air_data)
plt.title('Karakteristik Jam PM2.5 Berdasarkan Bulan')

# Subplot untuk PM2.5 berdasarkan tabun
plt.subplot(3, 1, 2)
sns.lineplot(x='month', y='PM2.5', hue='year', data=air_data)
plt.title('Karakteristik Bulanan PM2.5 Berdasarkan Tahun')



st.pyplot(plt.gcf())



## Conclusion Section
st.header("5. Kesimpulan dari Analisis")
st.markdown("""
### 1. **Pengaruh Curah Hujan terhadap Polusi Udara**:
- **Hubungan Curah Hujan dengan Polutan PM2.5**:
- Hujan berperan signifikan dalam mengurangi tingkat polusi udara, terutama pada partikel PM2.5. Berdasarkan visualisasi yang dibuat, semakin tinggi intensitas hujan maka semakin rendah tingkat PM2.5 di udara.

### 2. **Karakteristik Polusi Berdasarkan Waktu**:
- Polusi udara mengikuti pola musiman dengan peningkatan yang jelas, karena kondisi atmosfer yang cenderung memerangkap partikel udara.
""")



