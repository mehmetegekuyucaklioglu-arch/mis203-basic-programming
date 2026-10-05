
order_amount = float(input("Enter order amount (TRY): "))
available_stock = int(input("Enter available stock: "))
requested_quantity = int(input("Enter requested quantity: "))
is_member_input = input("Is the customer a member? (yes/no): ").strip().lower()

is_member = (is_member_input == "yes")

if requested_quantity <= 0:
    print("Order Rejected: Invalid requested quantity.")

elif order_amount <= 0:
    print("Order Rejected: Invalid order amount.")

elif requested_quantity > available_stock:
    print("Order Rejected: Insufficient stock.")

else:
   
    if is_member and order_amount >= 500:
        discount = order_amount * 0.10
        final_price = order_amount - discount
        print("Order Approved: Member discount (10%) applied.")
    else:
        final_price = order_amount
        print("Order Approved: Standard price applied.")
    
    print(f"Final Price: {final_price:.2f} TRY")
