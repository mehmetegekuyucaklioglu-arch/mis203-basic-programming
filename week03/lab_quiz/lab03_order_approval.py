
order_amount = float(input("Sipariş tutarını girin (TRY): "))
available_stock = int(input("Mevcut stok miktarını girin: "))
requested_quantity = int(input("İstenen miktarı girin: "))
is_member_input = input("Müşteri üye mi? (evet/hayır): ").strip().lower()

is_member = (is_member_input == "evet")

if requested_quantity <= 0:
    print("Sipariş Reddedildi: Geçersiz sipariş miktarı.")

elif order_amount <= 0:
    print("Sipariş Reddedildi: Geçersiz sipariş tutarı.")

elif requested_quantity > available_stock:
    print("Sipariş Reddedildi: Yetersiz stok.")

else:
    if is_member and order_amount >= 500:
        discount = order_amount * 0.10
        final_price = order_amount - discount
        print("Sipariş Onaylandı: Üye indirimi (%10) uygulandı.")
    else:
        final_price = order_amount
        print("Sipariş Onaylandı: Standart fiyat uygulandı.")
    
    print(f"Nihai Fiyat: {final_price:.2f} TRY")
