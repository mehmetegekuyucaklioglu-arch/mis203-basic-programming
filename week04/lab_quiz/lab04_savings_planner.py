def main():
    print("=== Savings Goal Planner ===")
    
    while True:
        try:
            starting_balance = float(input("Enter starting balance: "))
            if starting_balance >= 0:
                break
            print("Error: Starting balance cannot be negative. Try again.")
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        try:
            monthly_deposit = float(input("Enter monthly deposit: "))
            if monthly_deposit > 0:
                break
            print("Error: Monthly deposit must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        try:
            monthly_rate = float(input("Enter monthly interest rate (%): "))
            if monthly_rate >= 0:
                break
            print("Error: Interest rate cannot be negative.")
        except ValueError:
            print("Error: Please enter a valid number.")

    while True:
        try:
            savings_goal = float(input("Enter savings goal: "))
            if savings_goal > 0:
                break
            print("Error: Savings goal must be greater than 0.")
        except ValueError:
            print("Error: Please enter a valid number.")

    balance = starting_balance
    total_interest = 0.0

  
    if balance >= savings_goal:
        print("\nStarting balance already meets or exceeds your goal!")
        print("Goal reached in 0 months.")
        print(f"Final Balance: ${balance:.2f}")
        print(f"Total Interest Earned: ${total_interest:.2f}")
        return


    print(f"\n{'Month':<6} | {'Interest Earned':<16} | {'New Balance':<12}")
    print("-" * 42)

    reached_goal = False
    final_months = 0

    for month in range(1, 61):
       
        interest = balance * (monthly_rate / 100)
        total_interest += interest
        balance += interest
        balance += monthly_deposit

        print(f"{month:<6} | ${interest:<15.2f} | ${balance:<11.2f}")

    
        if balance >= savings_goal:
            reached_goal = True
            final_months = month
            break
    else:
       
        final_months = 60

    print("-" * 42)

  
    if reached_goal:
        print(f"Goal reached in {final_months} months.")
    else:
        print("Goal not reached within 60 months.")

    print(f"Final Balance: ${balance:.2f}")
    print(f"Total Interest Earned: ${total_interest:.2f}")

if _name_ == "_main_":
    main()
