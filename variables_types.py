x = 10   # global variable
# user defined function
def show():
    y = 20   # local variable
    print("Inside function  x =", x)
    print("Inside function y =", y)
# main program or driver code
show()
print("Outside function x =", x)