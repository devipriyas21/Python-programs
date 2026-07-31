def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


number = int(input("Enter a number: "))
original = number
sum_of_factorials = 0

while number > 0:
    digit = number % 10
    sum_of_factorials += factorial(digit)
    number //= 10

if sum_of_factorials == original:
    print(f"{original} is a Strong Number.")
else:
    print(f"{original} is not a Strong Number.")
