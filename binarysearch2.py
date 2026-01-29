# Program to check if a student has cleared the exam using Binary Search
# Read total number of students
from array import *
n = int(input("Enter number of students: "))

# create an empty integer array
roll_numbers= array('i', [])

# Read sorted roll numbers from user
print("Enter roll numbers of students:")
for i in range(n):
    roll = int(input(f"Student {i+1}: "))
    roll_numbers.append(roll)

# sort the array using sorted function
roll_numbers = array('i', sorted(roll_numbers))

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

# Display sorted array
print("given array in sorted order ")
print(roll_numbers)

# Display result
if found:
    print("Student has cleared the exam.")
else:
    print("Student has not cleared the exam.")