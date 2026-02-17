s1 = "Abc"
s2 = "Xyz"

# get string length
s1_length = len(s1)
s2_length = len(s2)

# get length of a bigger string
length = s1_length if s1_length > s2_length else s2_length
result = ""

# reverse s2
s2 = s2[::-1]

# iterate string 
# s1 ascending and s2 descending
for i in range(length):
    if i < s1_length:
        result = result + s1[i]
    if i < s2_length:
        result = result + s2[i]

print(result)
