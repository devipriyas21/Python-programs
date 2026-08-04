number = int(input("Enter a number: "))

if number < 0:
    print("Please enter a non-negative number.")
else:
    binary = bin(number)[2:]

    print("Binary Representation:", binary)

    if binary == binary[::-1]:
        print(f"{number} is a Binary Palindrome.")
    else:
        print(f"{number} is not a Binary Palindrome.")
