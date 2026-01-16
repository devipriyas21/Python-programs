# Electricity Billing System using match-case
units = int(input("Enter units consumed: "))
print("enter consumer category Domestic or Commercial or Industrial")
category = input().lower()  # convert to lowercase for consistency
match category:
        case "domestic":  # Domestic Users
            if units <= 100:
                bill = units * 3
            elif units <= 200:
                bill = (100 * 3) + (units - 100) * 5
            else:
                bill = (100 * 3) + (100 * 5) + (units - 200) * 8
            total_bill = bill + 50  # service charge
            print("total bill is",total_bill)
        case "commercial": # for commercial users
            if units <= 300:
                bill = units * 6
            elif units <= 600:
                bill = (300 * 6) + (units - 300) * 8
            else:
                bill = (300 * 6) + (300 * 8) + (units - 600) * 12
            total_bill = bill + 200   # service charge
            print("total bill is",total_bill)
        case "industrial":  # for Industrial Users
            if units <= 500:
                bill = units * 9
            elif units <= 1000:
                bill = (500 * 9) + (units - 500) * 15
            else:
                bill = (500 * 9) + (500 * 15) + (units - 1000) * 20
            total_bill = bill + 1000   # service charge
            print("total bill is",total_bill)
        case _:  print("invalid category")