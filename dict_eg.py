accounts = {}
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Display All\n5. Exit")
    ch = int(input("Enter your choice: "))
    if ch == 1:
        acc = input("Enter Account Number: ")
        name = input("Enter Name: ")
        bal = float(input("Enter Opening Balance: "))
        accounts[acc] = {"Name": name, "Balance": bal}
    elif ch == 2:
        acc = input("Enter Account Number: ")
        amt = float(input("Enter Deposit Amount: "))
        if acc in accounts:
            accounts[acc]["Balance"] += amt
        else:
            print("Account not found!")

    elif ch == 3:
        acc = input("Enter Account Number: ")
        amt = float(input("Enter Withdraw Amount: "))
        if acc in accounts:
            if accounts[acc]["Balance"] >= amt:
                accounts[acc]["Balance"] -= amt
            else:
                print("Insufficient balance!")
        else:
            print("Account not found!")
    elif ch == 4:
        for acc, info in accounts.items():
            print(f"{acc} → {info}")
    elif ch == 5:
        break
