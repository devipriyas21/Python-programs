# Optimized Prime Number Check
num = int(input("Enter a number: "))
is_prime = True
for i in range(2, int(math.sqrt(num)) + 1):
    if num % i == 0:
       is_prime = False
       break
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")