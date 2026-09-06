
# a menu that will keep showing until user quits
balance = 10000
 
while True:
    print()
    print("=== Mini Bank === ")
    print("1. Check balance ")
    print("2. Deposit ")
    print("3. Withdraw ")
    print("4. Exit")
    print()
 
    choice = input("Choose option: ")
 
    if choice == "1":
        print(f"Balance: Ksh {balance}")
    elif choice == "2":
        deposit_amount = float(input("Deposit amount: "))
        balance += deposit_amount   # balance = balance + deposit_amount
        print(f"Deposited Ksh {deposit_amount}. New balance: Ksh {balance}")
    elif choice == "3":
        withdraw_amount = float(input("Withdraw amount: "))
        if withdraw_amount > balance:
            print("Insufficient balance")
        else:
            balance -= withdraw_amount
            print(f"Withdrew Ksh {withdraw_amount}. New balance: Ksh {balance}")
    elif choice == "4":
        print("Thank you. Goodbye!")
        break
    else:
        print("Invalid option. Try again.")