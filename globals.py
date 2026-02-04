# user defined function
def show():
    y = 20   # local variable
    global x
    print("Inside function  x =", x)
    print("Inside function y =", y)
    x=x+5
    print("after updating global Inside function  x =", x)
# main program or driver code
show()
print("Outside function x =", x)
