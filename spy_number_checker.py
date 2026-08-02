number = int(input("Enter a number: "))

original = number
sum_of_digits = 0
product_of_digits = 1

while number > 0:
    digit = number % 10
    sum_of_digits += digit
    product_of_digits *= digit
    number //= 10

if sum_of_digits == product_of_digits:
    print(f"{original} is a Spy Number.")
else:
    print(f"{original} is not a Spy Number.")
