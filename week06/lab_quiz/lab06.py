
BRANSLAR = ("Yazılım", "Tasarım", "Pazarlama")


tum_ogrenciler = []



ogrenci1_isim = " Ahmet ".strip()
ogrenci1_branslar = [BRANSLAR[0], BRANSLAR[2]]  
tum_ogrenciler.append([ogrenci1_isim, ogrenci1_branslar])

ogrenci2_isim = " Zeynep ".strip()
ogrenci2_branslar = [BRANSLAR[1]]  
tum_ogrenciler.append([ogrenci2_isim, ogrenci2_branslar])

ogrenci3_isim = " Can ".strip()
ogrenci3_branslar = [BRANSLAR[0]] 
tum_ogrenciler.append([ogrenci3_isim, ogrenci3_branslar])

print("--- ADIM 2: İlk Öğrenci Listesi ---")
print(tum_ogrenciler)
print()



baskan_isim = " Mert (Başkan) ".strip()
baskan_branslar = [BRANSLAR[0], BRANSLAR[1], BRANSLAR[2]]
tum_ogrenciler.insert(0, [baskan_isim, baskan_branslar])


print("--- ADIM 3: Başkan Eklendikten Sonra ---")
print(f"Toplam Kayıtlı Öğrenci Sayısı: {len(tum_ogrenciler)}")
print(tum_ogrenciler)
print()



silinecek_isim = "Zeynep"
ogrenci_nesnesi = None

for ogrenci in tum_ogrenciler:
    if ogrenci[0] == silinecek_isim:
        ogrenci_nesnesi = ogrenci
        break

if ogrenci_nesnesi in tum_ogrenciler:
    tum_ogrenciler.remove(ogrenci_nesnesi)


if len(tum_ogrenciler) > 0:
    son_cikan_ogrenci = tum_ogrenciler.pop()
    print("--- ADIM 4: Öğrenci Çıkarma İşlemleri ---")
    print(f"Sistemden en son çıkan öğrenci: {son_cikan_ogrenci[0]}")
else:
    print("Uyarı: Liste boş olduğu için pop() yapılamadı.")

print(f"Güncel Liste: {tum_ogrenciler}")
print()



yeni_ogrenci_isim = " Burak Tan ".strip()
yeni_ogrenci_branslar = [BRANSLAR[1]]  
tum_ogrenciler.append([yeni_ogrenci_isim, yeni_ogrenci_branslar])

print("--- ADIM 5.1: Burak Tan Eklendi ---")
print(tum_ogrenciler)
print()


gecici_sirali_liste = sorted(tum_ogrenciler, key=lambda x: x[0])

print("--- ADIM 5.2: Geçici Sıralama (sorted) ---")
print("Geçici Sıralı Kopya :", gecici_sirali_liste)
print("Orijinal Liste      :", tum_ogrenciler)
print("(Kanıt: sorted() orijinal listeyi kalıcı olarak değiştirmemiştir.)")
print()


tum_ogrenciler.sort(key=lambda x: x[0])

print("--- ADIM 5.3: Kalıcı Sıralama (sort) ---")
print("Kalıcı Sıralanmış Liste:", tum_ogrenciler)
