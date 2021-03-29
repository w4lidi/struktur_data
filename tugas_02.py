def gaji_pokok (self, gaji): #sebuah fungsi dengan nama gaji_pokok; tapi tidak digunakan; ????
	self.gaji=gaji
	return self.gaji

gaji=int(input("massukkan gaji pokok : ")) #mengambil inputan user dan di simpan di variable gaji
print("gaji masuk = ",gaji)                #inputan user ditampikan kelayar sebagai gaji masuk;
print("=====================================")

transport = gaji * 0.2                     #hitung jumlah transport sebesar 20% dari gaji pokok, simpan di variabel transport;

print("jumlah transport = ",transport)     #jumlah transport ditampilkan kelayar;
anak=""                                    #variable untuk menyimpan jenis kelamin anak;

while (anak != ("perempuan" or "laki-laki")):   #perulangan untuk megulangi inputan jika inputan user salah;
	anak=input("jenis kelamin anak? => [ laki-laki ATAU perempuan ] : ")	 #mengambil inputan user dan di simpan di variable anak;  
	if anak == "laki-laki" :               #cek kondisi 1 jika anak laki-laki
		transport_anak = 15000             #set variabel dengan value 15000;
		total_transport = transport + transport_anak  #hitung total transport;
		break                              #perintah untuk meghentikan looping;
	elif anak == "perempuan":              #cek kondisi 2 jika anak perempuan
		transport_anak = 20000             #set variabel dengan value 20000;
		total_transport = transport + transport_anak  #hitung total transport;
		break                              #perintah untuk meghentikan looping;
	else:                                  #kondisi jika 1 dan 2 tidak terpenuhi
		print("jenis kelamin salah! Coba lagi..!!! ")   #beri tahu user bahwa input jenis kelamin salah;
	
print("transport untuk anak ",anak,"= ",transport_anak) #tamilkan jenis kelamin anak dan transport untuk anak;
print("total transport = ", total_transport) #tmpilkan total transport;
print("=====================================")

total_gaji= total_transport + gaji          #hitung total gaji;

print("jumlah total gaji pokok : ", total_gaji) #tamilkan total gaji;
