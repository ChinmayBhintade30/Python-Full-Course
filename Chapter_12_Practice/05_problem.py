#  Store the multiplication tables generated in problem 3 in a file named Tables.txt.

 #we will use append mode to add table of every number , inside the file Table.txt

#by using open file and mode as f
#we will also add the table in str format

n = int(input("Enter the number: "))

#we will use the same method enumerate used in the 3rd question to take the output in same line 
# to iterate and print the item multiplied in it

#we use for i in range loop to iterate over the range 1 to 10 

# and operation n * i  that iteration number


table = [n*i for i in range(1,11)]

with open("Table.txt","a") as f:
    f.write(f"Table of {n} : {str(table)} \n")





