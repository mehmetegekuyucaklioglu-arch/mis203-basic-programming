# Öğrenci Kulübü Kayıt Otomasyonu (Lab 06)

Bu proje, Python'daki temel veri yapılarını (`List` ve `Tuple`) ve liste yönetim metotlarını kullanarak bir öğrenci kulübünün kayıt otomasyonunu simüle eder.

---

## 📌 Kullanılan Veri Yapıları ve Nedenleri

1. **Tuple `()` (Demet):** 
   - Kulübün 3 ana branşı (`"Yazılım"`, `"Tasarım"`, `"Pazarlama"`) sonradan **değiştirilemez (immutable)** bir yapıda tutulması gerektiği için `Tuple` olarak tanımlanmıştır.
2. **İç İçe Liste `[ ]` (Nested List):** 
   - Öğrenci kayıtları `["Öğrenci Adı", ["Seçtiği Branşlar"]]` yapısında tutularak her öğrencinin adı ve seçtiği branşlar düzenli bir şekilde saklanır.

---

## 🛠 Projede Uygulanan Adımlar ve Kullanılan Metotlar

- **Adım 1:** Değiştirilemez `BRANSLAR` demeti ve tüm öğrencileri toplayacak boş `tum_ogrenciler` listesi oluşturuldu.
- **Adım 2:** Listeye 3 öğrenci eklendi. Girdilerdeki hatalı boşluklar `strip()` ile temizlendi.
- **Adım 3:** `insert(0, ...)` metodu ile listenin en başına **Başkan** eklendi. Toplam öğrenci sayısı `len()` ile ekrana yazdırıldı.
- **Adım 4:** İsteğiyle ayrılan bir öğrenci `remove()` ile silindi. Sistemden en son çıkan öğrenci `pop()` metodu ile listeden çıkarıldı ve ismi ekrana yazdırıldı. *(Hata almamak için `if` kontrolleri eklendi).*
- **Adım 5:** 
  - `append()` ile listenin sonuna yeni bir öğrenci ekledi.
  - `sorted()` ile listenin **orijinal sırası bozulmadan** geçici bir kopyası alfabetik olarak ekrana yazdırıldı.
  - `sort()` ile ana liste **kalıcı olarak** alfabetik sıraya dizildi ve güncel liste ekrana basıldı.

---

## 🚀 Çalıştırma Talimatı

Kodu çalıştırmak için terminalden aşağıdaki komutu yürütebilirsiniz:

```bash
python week06/lab-quiz/lab06.py
