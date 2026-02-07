# Program to count vowels and consonants in a given sentence
# read input from user
sentence = input("Enter a sentence: ")
# convert sentence to lowercase for easy comparison
sentence = sentence.lower()
# define vowels
vowels = "aeiou"
# initialize counters
vowel_count = 0
consonant_count = 0
# loop through each character in the sentence
for ch in sentence:
    if ch.isalpha():  # check if character is a letter
        if ch in vowels:
            vowel_count += 1
        else:
            consonant_count += 1
# display results
print("Number of vowels:", vowel_count)
print("Number of consonants:", consonant_count)