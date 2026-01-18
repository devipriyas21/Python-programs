a=int(input("enter any four digit number in which digits must be in order "))
# find smallest of a or reverse
x=a
rev=0
while x!=0 :
     r=x%10
     rev=rev*10+r
     x=x//10
b=rev
c=a-b
print("a value is ",a)
print("b value is ",b)
print("kaprekar constant is ",c)