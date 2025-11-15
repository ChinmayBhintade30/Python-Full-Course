# 3. Write a list comprehension to print a list which contains the multiplication table of a
# user entered number.


n = int(input("Enter the number: "))

table = [n*i for i in range(1,11)]

# the first operation is between i the iterating variable and the input number by the user''


print(table)
#we print the table in the form of the list 

#i iterates in the range from  1 to 10 (11 not included)

# Enter the number: 5
# [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]


