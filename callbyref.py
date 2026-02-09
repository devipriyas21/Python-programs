def modify(lst):
    lst.append(10)
    lst[2]=555
    print("Inside function:", lst)

# main or driver code
x = [1, 2, 3] # list mutable object
modify(x)
print("Outside:", x)