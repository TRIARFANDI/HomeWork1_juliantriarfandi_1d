print('selamat datang di rental mobil maju jaya')
print('=========================================================')
nama = input (       'masukan nama anda              :')
tersedia_merk = ['avanza', 'xenia', 'brio']
print(tersedia_merk)
merk = input (       'merk mobil yg akan di sewa     :')
perhari = 350000
berapa_hari = int(input('1 hari 350.000.rental berapa hari)             :'))
total = (berapa_hari * perhari)
jenis_pembayaran = ['cash', 'dana', 'm-banking', 'ovo', 'gopay',]  
print(jenis_pembayaran)
print(total)      

pembayaran = input(       'masukan jenis pembayaran       :')
bayar = int(input(        'masukan jumlah pembayaran anda :'))
serah_kunci = True
print(serah_kunci)

hasil =('selamat anda berhasil' if bayar==total and
         serah_kunci==True and pembayaran in jenis_pembayaran and merk in tersedia_merk and berapa_hari else 'maaf anda gagal')

print(hasil)
print('============================================================================')
