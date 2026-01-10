# Program to find the largest number in a list

numbers = [12, 45, 7, 89, 23]
largest = numbers[0]

for num in numbers:
    if num > largest:
        largest = num

print("Largest number in the list:", largest)
