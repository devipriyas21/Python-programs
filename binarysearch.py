n = int(input("Enter number of students: ")) 
# Create a list to store sorted roll numbers 
roll_numbers = [] 
# Read sorted roll numbers from user 
print("Enter sorted roll numbers of students:") 
for i in range(n): 
    roll = int(input(f"Student {i+1}: ")) 
    roll_numbers.append(roll) 
# Read roll number to search 
search_roll = int(input("Enter roll number to search: ")) 
# Initialize low and high pointers 
low = 0 
high = n - 1 
# Binary Search 
found = False 
while low <= high: 
    mid = (low + high) // 2 
    if roll_numbers[mid] == search_roll: 
        found = True 
        break 
    elif search_roll < roll_numbers[mid]: 
        high = mid - 1 
    else: 
        low = mid + 1 
# Display result 
if found: 
    print("Student has cleared the exam.") 
else: 
    print("Student has not cleared the exam.")