# Write a program to calculate the factorial of a given number using for loop

#factorial is nothing but the product of numbers starting from itself till 1 in reverse direction

#5! = 5*4*3*2*1

#n! = (n) * (n-1) * (n-2) * (n-3)....


#so for program sake - it can be 1 to the number itself also as multiplication does not change in any order


# 1 to 5 if  n = 5

n = int(input("Enter the number: "))

product = 1
#As we know sum = 0 , for sum as we add , but for multiplication we need 1 

for i in range(1,n+1):
    product = product * i
#here as we know range function iterates from 1 to n-1 element excluding n , so we have done n+1 here

#Thats why we written 1 to n+1  so that it iterate from 1 to n (1 t 6)
print(f"The factorial of the {n} is {product}")


"""
Enter the number: 6
The factorial of the 6 is 720

"""