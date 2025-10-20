#star pattern :-
# Write a program to print the following star pattern.
#   *
#  ***
# *****
#  for n = 3

"""
    *
   ***
  *****
 ********
**********

this pattern has n = 5,and it has 4 spaces in first row , and then 3,2,1 keep decreasing 

so (n-i) is the number of spaces for every first row and others follow it

to asterisk = (2*i-1)
"""

#here there are 2 space and 1 star in first row , 1 space and 3 stars in 2nd row and no space and 5 stars in 3rd row

n = int(input("Enter the number: "))
# now we know that if we want 3 rows then 1 to n (n+1) so that we can have 3 rows

for i in range(1, n+1):
    print(" " * (n-i) ,end="") 
    print("*" * (2*i - 1) , end="") 
    print("")

# this prints the * to the row
# this prints the number of spaces in row (" "(one space ) into (n-i) and then end gives again the same space )
#this third line only creates the new line for the pyramid:-
#As we know both the above lines does not have new line because we are working on same line that is spaces and asterisks



#end = "" doesnot give new line by default - so we use it after every line 

#didnt gave / baskslash n because it will create new line double


    
