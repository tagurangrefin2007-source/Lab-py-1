balance = 1000  # starting balance

while True:
    try:
        
        print("\nOptions:")
        print("1 - Check Balance")
        print("2 - Withdraw")
        print("3 - Exit")



        choice = input("Choose an option: ")

        if choice == "1":
                print("Your balance is:", balance)
        elif choice == "2":
                amount = float(input("Enter amount to withdraw: "))
                if amount > balance:
                    print("Insufficient funds!")
                else:
                    balance -= amount
                    print("Withdrawal successful!")
                    print("Remaining balance:", balance)
        elif choice == "3":
                print("Thank you!")
                break
        else:
                print("Invalid choice.")

    except ValueError:
        print("Invalid input! Please enter a number.")
        print("Remaining balance:", balance)
