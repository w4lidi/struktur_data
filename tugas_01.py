#tugas struktur data
#nama : walidi wahyu pratama
#NIM / kelas : TI17200054 / TI (B)

hari = ["Senin","Selasa", "Rabu", "Kamis", "Jum'at", "Sabtu", "Minggu"] #list untuk menampung nama hari.
for i in range(len(hari)):              #perulangan FOR untuk mengulagi perintah sampai kondisi mejadi FALSE.
    print(i + 1,hari[i])                #perintanh untuk menampikan nomor dan nama hari ke layar.
    if i == 4:                          #logika pertama, jika nilai i sama degan 4 maka akan mejalankan
        print("     hari masuk kuliah") #perintah ini untuk menampikan ke layar.
    elif i == 6:                        #logika kedua, jika nilai i sama dengan 6 maka akan mejalankan
        print("     Hari libur kuliah") #perintah ini untuk menampikan ke layar.
        
        
        
