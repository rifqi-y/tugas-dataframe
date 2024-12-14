import pandas as pd
from collections import defaultdict

df_data_sampah = pd.read_csv("data_sampah.csv", usecols=['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun'])
df_data_sampah.dropna(inplace=True)
print(df_data_sampah)

total_sampah_2020 = []
for index, row in df_data_sampah.iterrows():
    if row['tahun'] == 2020:
        total_sampah_2020.append(row['jumlah_produksi_sampah'])

print(sum(total_sampah_2020))


total_sampah_pertahun = defaultdict(int)

for index, row in df_data_sampah.iterrows():
    total_sampah_pertahun[row['tahun']] += row['jumlah_produksi_sampah']

total_sampah_pertahun = dict(total_sampah_pertahun)

for index, row in total_sampah_pertahun.items():
    print(f"Total Sampah Tahun {index}: {round(row, 2)} ")

df_pertahun = pd.DataFrame(list(total_sampah_pertahun.items()), columns=['tahun', 'total_sampah'])
df_pertahun.to_csv('sampah_pertahun.csv', index=False)
df_pertahun.to_excel('sampah_pertahun.xlsx', index=False)


total_sampah_perkota = defaultdict(int)

for index, row in df_data_sampah.iterrows():
    total_sampah_perkota[row['nama_kabupaten_kota']] += row['jumlah_produksi_sampah']

total_sampah_perkota = dict(total_sampah_perkota)
print(total_sampah_perkota)
for index, row in total_sampah_perkota.items():
    print(f"Total sampah di {index} periode 2015-2021: {round(row, 2)}")

df_perkota = pd.DataFrame(list(total_sampah_perkota.items()), columns=['wilayah', 'total_sampah'])
# print(df_perkota)
df_perkota.to_csv('sampah_perkota.csv', index=False)
df_perkota.to_excel('sampah_perkota.xlsx', index=False)


for index, row in df_data_sampah.iterrows():
    print(f"Total sampah di {row['nama_kabupaten_kota'].title()} pada {row['tahun']}: {row['jumlah_produksi_sampah']}")