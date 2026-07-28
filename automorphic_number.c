number = int(input("Enter a number: "))

square = number * number
temp = number

is_automorphic = True

while temp > 0:
    if (temp % 10) != (square % 10):
        is_automorphic = False
        break
    temp //= 10
    square //= 10

if is_automorphic:
    print(f"{number} is an Automorphic Number.")
else:
    print(f"{number} is not an Automorphic Number.")
