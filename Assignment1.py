transactions = 0
MAX_TRANSACTIONS = 3
while True:
    print("\n===== ATM MENU =====")
    print("1. Withdraw Money")
    print("0. Exit")
    choice = int(input("Enter your choice: "))
    if choice == 0:
        print("Thank you! Exiting the application.")
        break
    elif choice == 1:
        if transactions >= MAX_TRANSACTIONS:
            print("Transaction limit reached for today (3 transactions).")
            break
        amount = int(input("Enter withdrawal amount: "))
        if amount <= 0 or amount % 100 != 0:
            print("Invalid amount! Amount should be a positive multiple of 100.")
            continue
        # Calculate currency notes
        notes_500 = amount // 500
        amount %= 500
        notes_200 = amount // 200
        amount %= 200
        notes_100 = amount // 100
        transactions += 1
        print("\nTransaction Successful!")
        print("Currency Notes:")
        print("₹500 notes:", notes_500)
        print("₹200 notes:", notes_200)
        print("₹100 notes:", notes_100)
        print("Transactions left:", MAX_TRANSACTIONS - transactions)
    else:
        print("Invalid choice! Please select again.")
    # Continue or Exit
    cont = input("\nDo you want to continue? (yes/no): ").lower()
    if cont != "yes":
        print("Thank you for using the ATM.")
        break
