# Write a program to print the following star pattern:
# *
# **
# *** 


n = int(input("Enter the number: "))
# now we know that if we want 3 rows then 1 to n (n+1) so that we can have 3 rows

for i in range(1, n+1): 
    print("*" * (i) , end="") 
    print("")


#here we have to just print the i times asterisk as here it is now 1, 3, 5 odd combinations

#rest the logic for the space remains the 

"""
*
**
***
****
*****
here only we have to print the asterisk for i times


"""