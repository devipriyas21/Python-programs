import string

sentence = input("Enter a sentence: ")

sentence = sentence.lower()

is_pangram = True

for letter in string.ascii_lowercase:
    if letter not in sentence:
        is_pangram = False
        break

if is_pangram:
    print("The given sentence is a Pangram.")
else:
    print("The given sentence is not a Pangram.")
