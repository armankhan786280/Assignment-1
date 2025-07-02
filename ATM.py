
user_pin = "8233"
balance = 5000  


def display_menu():
    print("\n========= ATM MENU =========")
    print("1. Check Balance  ")
    print("2. Deposit Money  ")
    print("3. Withdraw Money ")


pin_attempt = input("Enter your 4-digit PIN: ")

if pin_attempt == user_pin:
    print("\nPIN verified successfully!")
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")

        if choice == '1':
            print(f"\nYour current balance is: ₹{balance}")

        elif choice == '2':
            amount = float(input("Enter amount to deposit: ₹"))
            if amount > 0:
                balance += amount
                print(f"₹{amount} deposited successfully.")
                print(f"Updated balance: ₹{balance}")
            else:
                print("Invalid amount. Please enter a positive number.")

        elif choice == '3':
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount > 0:
                if amount <= balance:
                    balance -= amount
                    print(f"₹{amount} withdrawn successfully.")
                    print(f"Remaining balance: ₹{balance}")
                else:
                    print("Insufficient balance.")
            else:
                print("Invalid amount. Please enter a positive number.")

        elif choice == '4':
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Please select 1-4.")

else:
    print("Incorrect PIN. Access Denied.")
