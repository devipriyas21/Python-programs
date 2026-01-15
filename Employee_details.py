name = input("Enter employee name: ")
emp_id = input("Enter employee ID: ")
salary = float(input("Enter salary: "))

tax = salary * 0.05

print("\n--- Employee Information ---")
print("Name      :", name)
print("ID        :", emp_id)
print("Salary    :", salary)
print("Tax (5%)  :", tax)