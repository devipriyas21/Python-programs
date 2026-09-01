print("====================================")
print("       PASSWORD STRENGTH ANALYZER")
print("====================================")

password = input("Enter your password: ")

length = len(password)
upper = 0
lower = 0
digit = 0
special = 0

# Analyze each character
for char in password:
    if char.isupper():
        upper += 1
    elif char.islower():
        lower += 1
    elif char.isdigit():
        digit += 1
    else:
        special += 1

# Calculate strength score
score = 0

if length >= 8:
    score += 2

if length >= 12:
    score += 1

if upper > 0:
    score += 1

if lower > 0:
    score += 1

if digit > 0:
    score += 1

if special > 0:
    score += 1

print("\n----------- ANALYSIS -----------")
print(f"Password length       : {length}")
print(f"Uppercase letters     : {upper}")
print(f"Lowercase letters     : {lower}")
print(f"Digits                : {digit}")
print(f"Special characters    : {special}")

print("\nStrength: ", end="")

if score <= 2:
    print("WEAK")
    print("Suggestion: Use a longer password with numbers and symbols.")

elif score <= 4:
    print("MEDIUM")
    print("Suggestion: Add more character types and increase the length.")

elif score <= 5:
    print("STRONG")
    print("Good password! Increasing the length can make it even better.")

else:
    print("VERY STRONG")
    print("Excellent! Your password meets most strength requirements.")

print("--------------------------------")
