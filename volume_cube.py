def volume_cube(l,b=2.2,h=3.3):   
    vol=l*b*h    # here vol is local variable to the function 
    return vol 
# main program or driver code 
result1=volume_cube(5.1,6.1,7.1) 
print("volume of first cube is",result1) 
result2=volume_cube(1.1) 
print("volume  of second cube is",result2) 