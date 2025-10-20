# Write a program to find the sum of first n natural numbers using while loop.


n = int(input("Enter the limit of first n natural numbers: "))


i = 1
sum = 0 
while(i<=n):
    sum += i
    i += 1

print(f"The sum of first n natural numbers is : {sum}")
    
"""
Enter the limit of first n natural numbers: 5
The sum of first n natural numbers is : 15

"""

#here we used while loop from 1 to <= n as we want to print the sum of natural numbers

#we iterated i from 1 upto the nth number and addes the each number in sum variable

