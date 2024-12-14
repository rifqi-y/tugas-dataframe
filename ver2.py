import pandas as pd

total_sampah = {
    '2015': {'wilayah': [], 'jumlah_sampah': []},
    '2016': {'wilayah': [], 'jumlah_sampah': []},
    '2017': {'wilayah': [], 'jumlah_sampah': []},
    '2018': {'wilayah': [], 'jumlah_sampah': []},
    '2019': {'wilayah': [], 'jumlah_sampah': []},
    '2020': {'wilayah': [], 'jumlah_sampah': []},
    '2021': {'wilayah': [], 'jumlah_sampah': []}
}
df_data_sampah = pd.read_csv("data_sampah.csv", usecols=['nama_kabupaten_kota', 'jumlah_produksi_sampah', 'tahun'])
df_data_sampah.dropna(inplace=True)

for index, row in df_data_sampah.iterrows():
    
    match row['tahun']:
        case 2015:
            total_sampah['2015']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2015']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2016:
            total_sampah['2016']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2016']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2017:
            total_sampah['2017']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2017']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2018:        
            total_sampah['2018']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2018']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2019:
            total_sampah['2019']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2019']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2020:
            total_sampah['2020']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2020']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case 2021:
            total_sampah['2021']['wilayah'].append(row['nama_kabupaten_kota'])
            total_sampah['2021']['jumlah_sampah'].append(row['jumlah_produksi_sampah'])
        case _:
            pass

df_total_sampah = pd.DataFrame(total_sampah)
print(df_total_sampah)

print(sum(df_total_sampah['2020']['jumlah_sampah']))

print()    