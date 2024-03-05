import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Memuat data
@st.cache_data
def load_data():
    data_hour = pd.read_csv("hour.csv")
    data_day = pd.read_csv("day.csv")
    return data_hour, data_day

data_hour, data_day = load_data()

# Header
st.title('🚴‍♂️Proyek Analisis Data : [Bike Sharing Dataset] 🚴‍♀️')

# Informasi Kontak
st.markdown('🚀 **Nama:** Ricky Adinata Robianto')
st.markdown('📧 **Email:** m200d4ky1653@bangkit.academy')
st.markdown('🔍 **ID Dicoding:** m200d4ky1653')

# Pertanyaan Bisnis
st.markdown('## Menentukan pertanyaan bisnis 🤔')
st.markdown('- Bagaimana korelasi antara suhu, kelembaban, dan kecepatan angin dengan penyewaan sepeda? 🌡️💧💨')
st.markdown('- Apakah ada hubungan antara kondisi cuaca dan penggunaan sepeda? ☀️🌧️❄️')

# Import Semua Packages/Library yang Digunakan
st.markdown('## Import Semua Packages/Library yang Digunakan 🛠️')
st.markdown('```python')
st.code('import pandas as pd\nimport numpy as np\nimport matplotlib.pyplot as plt\nimport seaborn as sns', language='python')
st.markdown('```')

# Penilaian Data
st.markdown('## Assessing Data 🕵️‍♂️')
st.markdown('```python')
st.code("""
# Membaca data
data_hour = pd.read_csv("hour.csv")
data_day = pd.read_csv("day.csv")

# Info dataset
print("Info dataset per jam:")
print(data_hour.info())
print("\nInfo dataset per hari:")
print(data_day.info())

# Menampilkan beberapa baris pertama
print("\nBeberapa baris pertama dataset per jam:")
print(data_hour.head())
print("\nBeberapa baris pertama dataset per hari:")
print(data_day.head())

# Memeriksa nilai yang hilang
data_hour.isnull().sum()
data_day.isnull().sum()
""", language='python')
st.markdown('```')

# Pembersihan Data
st.markdown('## Cleaning Data 🧹')
st.markdown('Tidak ada pembersihan yang diperlukan karena tidak ditemukan kejanggalan dalam proses sebelumnya')

# Analisis Data Eksploratif (EDA)
st.markdown('## Analisis Data Eksploratif 🚀')

# Pertanyaan 1: Korelasi antara variabel
st.markdown('#### Korelasi antara Variabel')
st.markdown('**Statistik deskriptif untuk dataset per jam:**')
st.dataframe(data_hour.describe())

st.markdown('**Statistik deskriptif untuk dataset per hari:**')
st.dataframe(data_day.describe())

correlation_hour = data_hour[['temp', 'hum', 'windspeed', 'cnt']].corr()
correlation_day = data_day[['temp', 'hum', 'windspeed', 'cnt']].corr()

st.markdown('**Heatmap Korelasi antara Suhu, Kelembaban, Kecepatan Angin, dan Jumlah Penyewaan Sepeda:**')
plt.figure(figsize=(14, 6))
sns.heatmap(correlation_hour, annot=True, cmap='coolwarm', fmt=".2f")
st.pyplot(plt.gcf())

st.markdown('**Scatterplot Korelasi Suhu dan Jumlah Penyewaan Sepeda:**')
plt.figure(figsize=(14, 6))
sns.scatterplot(x='temp', y='cnt', data=data_hour)
st.pyplot(plt.gcf())

# Kesimpulan
st.markdown('## Kesimpulan')

# Kesimpulan untuk Pertanyaan 1
st.markdown('''- **Wawasan dari Pertanyaan 1:** Heatmap korelasi menunjukkan bahwa suhu udara memiliki korelasi positif yang signifikan dengan penyewaan sepeda. Semakin tinggi suhu, semakin tinggi jumlah penyewaan sepeda. Kelembaban memiliki korelasi negatif yang kuat dengan penyewaan sepeda, menandakan bahwa kelembaban tinggi menyebabkan jumlah penyewaan sepeda rendah. Kecepatan angin ('windspeed') menunjukkan korelasi yang lemah dengan penyewaan sepeda.''')

# Pertanyaan 2: Hubungan antara kondisi cuaca dan jumlah pengguna sepeda
st.markdown('#### Menerjemahkan Cuaca: Hubungan antara Kondisi Cuaca dan Pengguna Sepeda')
# Visualisasi & Analisis Penjelasan

# Boxplot variabel cuaca vs. jumlah penyewaan sepeda
st.markdown('**Boxplot Korelasi Cuaca dan Jumlah Penyewaan Sepeda:**')
plt.figure(figsize=(14, 6))
sns.boxplot(x='weathersit', y='cnt', data=data_hour)
st.pyplot(plt.gcf())

# Kesimpulan
st.markdown('## Kesimpulan')

# Kesimpulan untuk Pertanyaan 2
st.markdown('''- **Wawasan dari Pertanyaan 2:** Dari boxplot, kita melihat variasi penyewaan sepeda berdasarkan kondisi cuaca. Pada dataset per jam, cuaca cerah dengan sedikit awan cenderung memiliki penyewaan sepeda lebih tinggi dibandingkan dengan kondisi cuaca lain seperti kabut, salju ringan, dan hujan deras. Temuan ini konsisten dengan dataset per hari, di mana penyewaan sepeda tertinggi terjadi saat cuaca cerah dengan sedikit awan. Kesimpulannya, suhu, kelembaban, dan kondisi cuaca memengaruhi penyewaan sepeda, dengan suhu dan kondisi cuaca memiliki dampak yang lebih besar. Informasi ini dapat membantu penyedia layanan penyewaan sepeda dalam mengoptimalkan strategi berdasarkan faktor cuaca dan lingkungan.''')
