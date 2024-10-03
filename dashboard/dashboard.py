import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import seaborn as sns
import streamlit as st
from babel.numbers import format_currency
sns.set(style='dark')

# Membaca data dari file CSV
all_df = pd.read_csv("dashboard/main_data.csv")
st.header('Wardita Proyek Analisis Data Dashboard :sparkles:')

st.subheader('Pengaruh Hari Kerja Terhadap Jumlah Penyewa')

# Menampilkan kolom DataFrame untuk debugging
print(all_df.columns)

# Mengelompokkan data berdasarkan hari kerja dan menghitung jumlah penyewaan
def create_working_day_influence_df(df):
    working_day_df = df.groupby('workingday_x').agg({
        'cnt_x': 'sum'  # Menjumlahkan total penyewaan berdasarkan hari kerja
    }).reset_index()
    working_day_df.rename(columns={'workingday_x': 'working_day', 'cnt_x': 'total_rentals'}, inplace=True)
    return working_day_df

# Buat DataFrame untuk pengaruh hari kerja
working_day_influence = create_working_day_influence_df(all_df)

# Visualisasi pengaruh hari kerja terhadap jumlah penyewaan
def plot_working_day_influence(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='working_day', y='total_rentals', data=df)
    plt.title('Pengaruh Hari Kerja terhadap Jumlah Penyewaan')
    plt.xlabel('Hari Kerja (0: Tidak, 1: Ya)')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(ticks=[0, 1], labels=['Tidak', 'Ya'])  # Menambahkan label pada sumbu x
    st.pyplot(plt)  # Render plot di Streamlit

# Panggil fungsi plot
plot_working_day_influence(working_day_influence)

# Visualisasi pengaruh cuaca terhadap jumlah penyewaan
st.subheader('Pengaruh Cuaca Terhadap Jumlah Penyewa')

def create_weather_influence_df(df):
    weather_df = df.groupby('weathersit_x').agg({
        'cnt_x': 'sum'  # Menjumlahkan total penyewaan berdasarkan kondisi cuaca
    }).reset_index()
    weather_df.rename(columns={'weathersit_x': 'weather_condition', 'cnt_x': 'total_rentals'}, inplace=True)
    return weather_df

# Buat DataFrame untuk pengaruh cuaca
weather_influence = create_weather_influence_df(all_df)

# Visualisasi pengaruh cuaca terhadap jumlah penyewaan
def plot_weather_influence(df):
    plt.figure(figsize=(10, 6))
    sns.barplot(x='weather_condition', y='total_rentals', data=df)
    plt.title('Pengaruh Cuaca terhadap Jumlah Penyewaan')
    plt.xlabel('Kondisi Cuaca (1: Cerah, 2: Berawan, 3: Hujan Ringan, 4: Hujan Lebat)')
    plt.ylabel('Jumlah Penyewaan')
    plt.xticks(ticks=[0, 1, 2, 3], labels=['Cerah', 'Berawan', 'Hujan Ringan', 'Hujan Lebat'])  # Menambahkan label pada sumbu x
    st.pyplot(plt)  # Render plot di Streamlit

# Panggil fungsi plot untuk cuaca
plot_weather_influence(weather_influence)


st.subheader('Tren Penyewa Sepeda Harian')
# Create DataFrame for daily rentals
def create_daily_rentals_df(df):
    daily_rentals_df = df.groupby('dteday').agg({
        'cnt_x': 'sum'  # Ensure to use the correct column name for rentals
    }).reset_index()
    return daily_rentals_df

# Create DataFrame for daily rentals
daily_rentals = create_daily_rentals_df(all_df)

# Visualize daily rentals trend
def plot_daily_rentals(df):
    plt.figure(figsize=(12, 6))
    sns.lineplot(x='dteday', y='cnt_x', data=df)  # Use the correct column name
    plt.title('Tren Penyewaan Sepeda Harian')
    plt.xlabel('Tanggal')
    plt.ylabel('Jumlah Penyewaan')
    
    # Formatting date ticks
    plt.xticks(rotation=45)
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator())  # Set major ticks to each month
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%m-%d'))  # Format ticks as 'Year-Month'
    
    st.pyplot(plt)

# Call plot function for daily rentals
plot_daily_rentals(daily_rentals)

# Visualize distribution of rental counts
st.subheader('Distribusi Jumlah Penyewaan')

def plot_rental_distribution(df):
    plt.figure(figsize=(8, 6))
    sns.histplot(df['cnt_x'], kde=True)  # Use the correct column name
    plt.title('Distribusi Jumlah Penyewaan')
    plt.xlabel('Jumlah Penyewaan')
    plt.ylabel('Frekuensi')
    st.pyplot(plt)

# Call the function to plot the rental distribution
plot_rental_distribution(daily_rentals)
