#  Write a program to print multiplication table of n using for loops in reversed
# order.


#for reverse order 
# 11 - i -> when  i = 1,  if n = 5, then 5 X 10 = 50

n = int(input("Enter the number: "))

for i in range(1,11):
    print(f"{n} * {11-i} = {n*(11-i)}")

#here the  logic is - (11-i) means we have i from 1 to 10 , it performs the operations like number into 10,9,8,7,....


"""
5 * 10 = 50
5 * 9 = 45
5 * 8 = 40
5 * 7 = 35
5 * 6 = 30
5 * 5 = 25
5 * 4 = 20
5 * 3 = 15
5 * 2 = 10
5 * 1 = 5

"""