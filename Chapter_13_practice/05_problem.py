# Write a program to find the maximum of the numbers in a list using the reduce
# function.

from functools  import reduce
#we need to import the reduce function from using import


l = [3,6,2,8,1,7]

def greater(a,b):
    if(a>b):
        return a
    return b

    

print(reduce(greater,l))


#reduce calls the function greater in 2 values using a and b , and operates
#on the operation of a > b or a<b , and it returns the value a or b 

#it starts comparing the valeues inside the list ,  one by one , and shifts the values
#of a and b one after another 

#first a = 3 , b = 6 , then as b > a  , it returns b and iterates the value 
#the value for which the it gets returns the var , the other variable changes its value and moves to the next 
