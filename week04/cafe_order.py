import math
import random

print("=" * 45)
print("     CAMPUS CAFE & ORDER AUTOMATION")
print("=" * 45)

total_revenue = 0.0
total_items = 0
lucky_winners = 0

while True:
  customer_name = input("Customer name (Type 'q' to quit): ").strip()

  if customer_name.lower() == "q":
    break

  print("Products: 1- Coffee (80 TL) | 2- Sandwich (120 TL) | 3- Dessert (90 TL)")
  choice = input("Selected product number (1, 2, or 3): ").strip()

  if choice == "1":
    item_name = "Coffee"
    base_price = 80.0
  elif choice == "2":
    item_name = "Sandwich"
    base_price = 120.0
  elif choice == "3":
    item_name = "Dessert"
    base_price = 90.0
  else:
    print("Invalid selection! Please try again.\n")
    continue

  is_student = input("Are you a student? (yes/no): ").strip().lower()

  if is_student == "yes":
    discount = 0.25  
  else:
    discount = 0.0

  lucky_chance = random.randint(1, 10)
  if lucky_chance == 1:
    print(
        "🎉 Congratulations! You are today's lucky customer, you won an extra"
        " 50% discount!"
    )
    discount += 0.50
    lucky_winners += 1

  final_price = base_price * (1 - discount)

  final_price = math.ceil(final_price)

  print(
      f"--> Price for {customer_name} - {item_name}: {final_price} TL"
      f" (Discounted)\n"
  )

  total_revenue += final_price
  total_items += 1

print("\n" + "=" * 45)
print("             DAILY CASH REGISTER REPORT")
print("=" * 45)
print(f"Total Items Sold : {total_items}")
print(f"Total Revenue    : {total_revenue} TL")
print(f"Lucky Draw Winners: {lucky_winners} people")
print("=" * 45)
print("Program successfully terminated.")
