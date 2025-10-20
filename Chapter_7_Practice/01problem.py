#Write a program to print multiplication table of a given number using for loop.

# we can use f string to include variables in it

num = int(input("Enter the number: "))

for i in range(1,11):
    result = num * i
    print(f"{num} * {i} = {result}")
    
# 5 * 1 = 5
# 5 * 2 = 10
# 5 * 3 = 15
# 5 * 4 = 20
# 5 * 5 = 25
# 5 * 6 = 30
# 5 * 7 = 35
# 5 * 8 = 40
# 5 * 9 = 45
# 5 * 10 = 50

#using f string - we wrote multiplication table in full format
#range is from 1 to 11  as , we have to print it till 10 , 11 is excluded , 1 to 10 iterations for mutliplication

