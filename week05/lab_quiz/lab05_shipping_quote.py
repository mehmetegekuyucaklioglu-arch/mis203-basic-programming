
def calculate_subtotal(unit_price, quantity):
    """Ürün fiyatı ve miktarına göre ara toplamı hesaplar."""
    return unit_price * quantity

def calculate_discount_rate(subtotal):
    """
    Ara toplama göre indirim oranını belirler.
    1000 TL ve üzeri alışverişlerde %10 (%0.10) indirim uygulanır.
    """
    if subtotal >= 1000:
        return 0.10
    else:
        return 0.0

def calculate_shipping_fee(subtotal, is_member):
    """
    Kargo ücretini hesaplar.
    Üye olanlar veya ara toplamı 500 TL ve üzeri olanlar kargo ödemez (0 TL).
    Diğer durumlarda kargo ücreti 50 TL'dir.
    """
    if is_member or subtotal >= 500:
        return 0.0
    else:
        return 50.0

def calculate_final_total(unit_price, quantity, is_member):
    """Tüm fonksiyonları birleştirerek nihai toplam tutarı hesaplar."""
    subtotal = calculate_subtotal(unit_price, quantity)
    discount_rate = calculate_discount_rate(subtotal)
    
    discount_amount = subtotal * discount_rate
    discounted_subtotal = subtotal - discount_amount
    
    shipping_fee = calculate_shipping_fee(subtotal, is_member)
    
    final_total = discounted_subtotal + shipping_fee
    return final_total



assert calculate_subtotal(500, 2) == 1000.0, "Subtotal testi başarısız!"


assert calculate_final_total(600, 2, is_member=False) == 1080.0, "Final total test 1 başarısız!"


assert calculate_final_total(200, 2, is_member=False) == 450.0, "Final total test 2 başarısız!"

print("Tüm assert testleri başarıyla geçildi!")


print("\n--- ÖRNEK SİPARİŞ 1 ---")
order1_price = 450.0
order1_qty = 3
order1_member = True

sub1 = calculate_subtotal(order1_price, order1_qty)
disc1 = calculate_discount_rate(sub1)
ship1 = calculate_shipping_fee(sub1, order1_member)
total1 = calculate_final_total(order1_price, order1_qty, order1_member)

print(f"Ara Toplam: {sub1} TL")
print(f"İndirim Oranı: {disc1 * 100}%")
print(f"Kargo Ücreti: {ship1} TL")
print(f"Genel Toplam: {total1} TL")


print("\n--- ÖRNEK SİPARİŞ 2 ---")
order2_price = 250.0
order2_qty = 2
order2_member = False

sub2 = calculate_subtotal(order2_price, order2_qty)
disc2 = calculate_discount_rate(sub2)
ship2 = calculate_shipping_fee(sub2, order2_member)
total2 = calculate_final_total(order2_price, order2_qty, order2_member)

print(f"Ara Toplam: {sub2} TL")
print(f"İndirim Oranı: {disc2 * 100}%")
print(f"Kargo Ücreti: {ship2} TL")
print(f"Genel Toplam: {total2} TL")
