students = {} 
while True: 
    print("\n1. Add Student\n2. Update Marks\n3. Display All\n4. Exit") 
    choice = int(input("Enter your choice: ")) 
    if choice == 1: 
        name = input("Enter student name: ") 
        marks = int(input("Enter marks: ")) 
        students[name] = marks 
    elif choice == 2: 
        name = input("Enter student name to update: ") 
        if name in students: 
            students[name] = int(input("Enter new marks: ")) 
        else: 
            print("Student not found!") 
    elif choice == 3: 
        for name, marks in students.items(): 
            print(f"{name}: {marks}") 
    elif choice == 4: 
        break 
 
    else: 
        print("Invalid choice!") 