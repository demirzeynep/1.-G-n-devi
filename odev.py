#DEĞİŞKENLER
baslik = "HABERİNİZ OLSUN"
vade = 12
faiz0rani1 = 1.47
faiz0rani2 = 1.44
faiz0rani = 1.47

#değişken tipleri
print(baslik)
print(type(baslik))
print(type(vade))
print(type(faiz0rani))

#string değişkenlerle işlemler
mesaj = "Hoş Geldin"
musteriAdi = "Zeynep"
musteriSoyadi = "Demir"
sonucMesaj = mesaj+" "+musteriAdi+ " "+musteriSoyadi+"!"
print(sonucMesaj)

#integer değişkenlerle işlemler
sayi1 = 10
sayi2 = 20
print(sayi1+sayi2)

# ŞART BLOKLARI
dolarDun = 7.65
dolarBugün = 7.65

if dolarDun>dolarBugün:
    print("Azalış Oku")
elif dolarDun<dolarBugün:
    print("Artış Oku")
else:
    print("Eşittir Oku")
print("Bitti.")

#LİSTELER
krediler = ["Hizli Kredi", "Maaşini Halkbanktan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]
print(type(krediler))
print(krediler)
print(krediler[0])
print(krediler[1])
print(krediler[2])
print(len(krediler))

krediler[0] = "Çabuk Kredi"
print(krediler)
#print(krediler[3]) aralık dışında olduğundan index hatası verir.


#DÖNGÜLER
krediler = ["Hizli Kredi", "Maaşini Halkbanktan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]

for kredi in krediler:
    print("<option>"+kredi+"<option>") #option açılır kutu görünümü sağlar.
for i in range(len(krediler)):
    print(krediler[i])
for i in range(3,10):
    print(i)
for i in range(0,11,2):
    print(i)

#FONKSİYONLAR
def kredileriListele():
    krediler = ["Hizli Kredi", "Maaşini Halkbanktan Alanlara Özel", "Mutlu Emekli İhtiyaç Kredisi"]
    for kredi in krediler:
        print("<option>"+kredi+"<option>") #option açılır kutu görünümü sağlar.
kredileriListele()