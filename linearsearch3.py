# Program to check if a student has submitted the assignment using Linear Search
# Read total number of students

from array import *
n = int(input("Enter number of students: "))
# create an empty integer array
roll_numbers= array('i', [])

# Read roll numbers of students
print("Enter roll numbers of students:")
for i in range(n):
    roll = int(input("enter roll number  "))
    roll_numbers.append(roll)

# Read roll number to search
search_roll = int(input("Enter roll number to search: "))

# Initialize a flag to indicate if roll number is found
found = False

# Linear Search
for roll in roll_numbers:
    if roll == search_roll:
        found = True
        break

# Display result
if found:
    print("Student has submitted the assignment.")
else:
    print("Student has not submitted the assignment.")