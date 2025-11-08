#!/usr/bin/env python3
"""
ATM System with deposit and withdrawal functionality
"""

def main():
    # Get user information
    first_name = input("Enter your first name: ").strip()
    last_name = input("Enter your last name: ").strip()
    
    balance = 0.0
    deposit_limit = 1000
    withdraw_limit = 500
    
    print(f"\nWelcome {first_name} {last_name}!")
    print(f"Current balance: ${balance:.2f}")
    print(f"Deposit limit: ${deposit_limit}")
    print(f"Withdrawal limit: ${withdraw_limit}\n")
    
    # Main loop
    while True:
        print("\n" + "="*50)
        print("ATM Menu:")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            # Deposit functionality
            while True:
                try:
                    deposit_amount = float(input(f"\nEnter deposit amount (max ${deposit_limit}): $").strip())
                    
                    if deposit_amount < 0:
                        print("Amount is invalid, try again")
                        continue
                    
                    if deposit_amount > deposit_limit:
                        print(f"You cannot deposit more than ${deposit_limit}")
                        continue
                    
                    balance += deposit_amount
                    print(f"Deposit successful! New balance: ${balance:.2f}")
                    break
                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == "2":
            # Withdraw functionality
            while True:
                try:
                    withdraw_amount = float(input(f"\nEnter withdrawal amount (max ${withdraw_limit}): $").strip())
                    
                    if withdraw_amount < 0:
                        print("Amount is invalid, try again")
                        continue
                    
                    if withdraw_amount > withdraw_limit:
                        print(f"You cannot withdraw more than ${withdraw_limit}")
                        continue
                    
                    if balance < withdraw_amount:
                        print("You don't have necessary fund to withdraw")
                        break
                    
                    balance -= withdraw_amount
                    print(f"Withdrawal successful! New balance: ${balance:.2f}")
                    break
                    
                except ValueError:
                    print("Invalid input. Please enter a valid number.")
        
        elif choice == "3":
            # Check balance
            print(f"\nCurrent balance: ${balance:.2f}")
        
        elif choice == "4":
            # Exit
            print(f"\nThank you {first_name} {last_name} for using our ATM!")
            print(f"Final balance: ${balance:.2f}")
            break
        
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()

