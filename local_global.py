x = 10   # global variable
# user defined function
def show():
    x = 20   # local variable with same name
    print("Local x inside function =", x)
    print("Global x inside function =", globals()['x'])
# main program or driver code
show()
print("global variable outside function x =", x)