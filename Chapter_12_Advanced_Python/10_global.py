#local variable and global variable

a = 83
def fun():
    # global a
    #global a changes the value of globally defined a variable as 83 to 3 

    a = 3
    print(a)

fun()
print(a)



"""
here a inside the def fun is local variable and a= 83 is global variable 
local variable has scope only inside the function 


"""

#global variable a = 83 can be accessed throughout the function

