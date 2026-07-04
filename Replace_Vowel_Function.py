def vow_replace(string, vowel):
 vowels = "aeiou"
 result = ""

 for char in string:
 if char in vowels:
 result += vowel
 else:
 result += char

 return resul
