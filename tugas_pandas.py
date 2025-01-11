#amsa efraim cicio tarigan 
#152023120
#tugas dataframe 

import pandas as pd

# 1. Membaca data dari file CSV
file_path = r"D:\KULIAH\SEMESTER3\PEMDAS\tugas dataframe & lambda\opendata.jabarprov.go.id_dataset_od_16985_jumlah_produksi_sampah_berdasarkan_kabupatenkota_v3_csv\data.jabarprov.go.id\data_sampah.csv"
df = pd.read_csv(file_path)

# 2. Mengubah nama kolom 
df.rename(columns={
    'nama_kabupaten_kota': 'Kabupaten/Kota',
    'jumlah_produksi_sampah': 'Jumlah Produksi Sampah (ton)',
    'tahun': 'Tahun'
}, inplace=True)

# 3. Menghapus kata "TON PER HARI" 
df['Jumlah Produksi Sampah (ton)'] = df['Jumlah Produksi Sampah (ton)'].replace(' TON PER HARI', '', regex=True).astype(float)

# 4. Menghilangkan spasi 
df['Kabupaten/Kota'] = df['Kabupaten/Kota'].str.strip()

# 5.  total produksi sampah per tahun menggunakan iterrows
total_per_tahun = {}

for index, row in df.iterrows():
    tahun = row['Tahun']
    produksi = row['Jumlah Produksi Sampah (ton)']
    
    if tahun not in total_per_tahun:
        total_per_tahun[tahun] = 0
    total_per_tahun[tahun] += produksi

# total produksi sampah per tahun
print("Total Produksi Sampah per Tahun:")
for tahun, total in total_per_tahun.items():
    print(f"Tahun {tahun}: {total:.2f} ton")

# 6. jumlah data per Kota/Kabupaten per tahun menggunakan iterrows
total_per_kabupaten_tahun = {}

for index, row in df.iterrows():
    kota = row['Kabupaten/Kota']
    tahun = row['Tahun']
    produksi = row['Jumlah Produksi Sampah (ton)']
    
    if (kota, tahun) not in total_per_kabupaten_tahun:
        total_per_kabupaten_tahun[(kota, tahun)] = 0
    total_per_kabupaten_tahun[(kota, tahun)] += produksi

# total produksi sampah per Kota/Kabupaten per Tahun
print("\nTotal Produksi Sampah per Kota/Kabupaten per Tahun:")
for (kota, tahun), total in total_per_kabupaten_tahun.items():
    print(f"{kota} - Tahun {tahun}: {total:.2f} ton")

# Menyimpan hasil ke CSV dan Excel
# Membuat DataFrame untuk total per kota/kabupaten dan tahun
df_total_per_kabupaten_tahun = pd.DataFrame(
    [(kota, tahun, total) for (kota, tahun), total in total_per_kabupaten_tahun.items()],
    columns=['Kabupaten/Kota', 'Tahun', 'Jumlah Produksi Sampah (ton)']
)

# Menyimpan ke CSV
df_total_per_kabupaten_tahun.to_csv('total_per_kabupaten_tahun.csv', index=False)

# Menyimpan ke Excel
df_total_per_kabupaten_tahun.to_excel('total_per_kabupaten_tahun.xlsx', index=False)

print("\nHasil telah disimpan ke CSV dan Excel.")