s = "geeksforgeeks"
v = set('aeiou')
if v.issubset(set(s.lower())):
    print("True")
else:
    print("False")
