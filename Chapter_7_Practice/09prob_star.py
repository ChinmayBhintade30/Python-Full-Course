# Write a program to print the following star pattern.
'''

***
* * for n = 3
***
we have 3 asterisk in 1st row and 3 in last row 

space in between 2nd row

only one space between stars of 2nd row
'''
#use if condition for the i==1 and i==n that is first and last 3rd row to print asterisk - ***
# as we know either condition for 3 asterisk should be true so use or operator


n = int(input("Enter the number: "))

for i in range(1,n+1):
    if(i==1 or i==n):
        print("*" * n,end="") 
    else:
        print("*", end="")
        print(" " * (n-2), end="")
        print("*", end="")
    print("")
    # this line is for every new iteration in the row
    



"""
***
* *
***




*******
*     *
*     *
*     *
*     *
*     *
*******

"""
