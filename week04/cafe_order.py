import math
import random

print("=" * 45)
print("     KAMPÜS KAFE & SİPARİŞ OTOMASYONU")
print("=" * 45)

total_revenue = 0.0
total_items = 0
lucky_winners = 0

while True:
  customer_name = input("Müşteri adı (Çıkış için 'q' yazın): ").strip()

  if customer_name.lower() == "q":
    break

  print("Ürünler: 1- Kahve (80 TL) | 2- Sandviç (120 TL) | 3- Tatlı (90 TL)")
  choice = input("Seçtiğiniz ürün numarası (1, 2 veya 3): ").strip()

  if choice == "1":
    item_name = "Kahve"
    base_price = 80.0
  elif choice == "2":
    item_name = "Sandviç"
    base_price = 120.0
  elif choice == "3":
    item_name = "Tatlı"
    base_price = 90.0
  else:
    print("Geçersiz seçim yaptınız! Lütfen tekrar deneyin.\n")
    continue

  is_student = input("Öğrenci misiniz? (yes/no): ").strip().lower()

  if is_student == "yes":
    discount = 0.25  
  else:
    discount = 0.0

  lucky_chance = random.randint(1, 10)
  if lucky_chance == 1:
    print(
        "🎉 Tebrikler! Günün şanslı müşterisi oldunuz, ekstra %50 indirim"
        " kazandınız!"
    )
    discount += 0.50
    lucky_winners += 1

  final_price = base_price * (1 - discount)

  final_price = math.ceil(final_price)

  print(
      f"--> {customer_name} için {item_name} ücreti: {final_price} TL"
      f" (İndirimli)\n"
  )

  total_revenue += final_price
  total_items += 1

print("\n" + "=" * 45)
print("             GÜNLÜK KASA RAPORU")
print("=" * 45)
print(f"Toplam Satılan Ürün Sayısı : {total_items}")
print(f"Toplam Ciro                : {total_revenue} TL")
print(f"Şanslı Çekiliş Kazanan     : {lucky_winners} kişi")
print("=" * 45)
print("Program başarıyla sonlandırıldı.")
