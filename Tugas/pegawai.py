# Muhammad Amar Dafi 0110221095
pegawai1 = 'Ahmad'
pegawai2 = 'Alex'
agama1 = 'Islam'
agama2 = 'Kristen Protestan'
gaji_pokok1 = 4000000
gaji_pokok2 = 6000000
jumlah_anak1 = 2
jumlah_anak2 = 5
tunjangan_jabatan1 = gaji_pokok1 * (20/100)
tunjangan_jabatan2 = gaji_pokok2 * (20/100)
tunjangan_keluarga1 = 0
tunjangan_keluarga2 = 0

if (jumlah_anak1 > 0 and jumlah_anak1 <= 2):
    tunjangan_keluarga1 = gaji_pokok1*(10/100)
elif (jumlah_anak1 > 2):
    tunjangan_keluarga1 = gaji_pokok1*(20/100)

if jumlah_anak2 > 0 and jumlah_anak2 <= 2:
    tunjangan_keluarga2 = gaji_pokok2*(10/100)
elif jumlah_anak2 > 2 :
    tunjangan_keluarga2 = gaji_pokok2*(20/100)

gaji_kotor1 = gaji_pokok1 + tunjangan_jabatan1 + tunjangan_keluarga1
gaji_kotor2 = gaji_pokok2 + tunjangan_jabatan2 + tunjangan_keluarga2

zakat_profesi1 = (0,0.025)[agama1 == 'Islam' and gaji_kotor1 >= 6000000] * gaji_kotor1
zakat_profesi2 = (0,0.025)[agama2 == 'Islam' and gaji_kotor2 >= 6000000] * gaji_kotor2

gaji_bersih1 = gaji_kotor1 - zakat_profesi1
gaji_bersih2 = gaji_kotor2 - zakat_profesi2

print("Slip gaji PT XYZ")
print("-----------------")
print("Nama Pegawai \t \t :", pegawai1)
print("Agama \t \t \t :", agama1)
print("Jumlah Anak \t \t :", jumlah_anak2)
print("Gaji Pokok \t \t : Rp.", gaji_pokok2)
print("Tunjangan Jabatan \t : Rp.", tunjangan_jabatan2)
print("Tunjangan Keluarga \t : Rp.", tunjangan_keluarga2)
print("Gaji Kotor \t \t : Rp.", gaji_kotor2)
print("Zakat Profesi \t \t : Rp.", zakat_profesi2)
print("Take Home Pay \t \t : Rp.", gaji_bersih2)
print(" ")
print("Slip gaji PT XYZ")
print("-----------------")
print("Nama Pegawai \t \t :", pegawai2)
print("Agama \t \t \t :", agama2)
print("Jumlah Anak \t \t :", jumlah_anak2)
print("Gaji Pokok \t \t : Rp.", gaji_pokok2)
print("Tunjangan Jabatan \t : Rp.", tunjangan_jabatan2)
print("Tunjangan Keluarga \t : Rp.", tunjangan_keluarga2)
print("Gaji Kotor \t \t : Rp.", gaji_kotor2)
print("Zakat Profesi \t \t : Rp.", zakat_profesi2)
print("Take Home Pay \t \t : Rp.", gaji_bersih2)
print(" ")


