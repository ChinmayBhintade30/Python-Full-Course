#write a python program using recurssion function to print the sum of natural numbers


'''
Lets derive the formula for recurssion of Sum of n natural numbers
sum(n) = 1 + 2 + 3 + 4 + 5 + ...... + n

sum(1)   = 1
sum(2)   = 1 + 2
sum(3)   = 1 + 2 +3
sum(4)   = 1 + 2 +3 +4 
sum(5)   = 1 +2 +3 +4 +5


formula:-
sum(n) - becomes
sum(n) = sum(n-1) + n

this formula will be called again and again in the function definition

if n = 5 , then sum(n-1) + 5
sum(n-1) + 4 + 5
....


1 + 2 + 3 + 4 + 5

'''

# as we know that base conditon for n natural numbers it will start from 1 so n==1 it returns 1

def sum(n):
    if(n==1):
        #base condition of the 
        return 1
    
    return sum(n-1) + n
#here sum(n-1) + n calls the sum function itself again and again
#here base condition is used to hit the n == 1 and the function returns 1 and print the final sum so that it does not go to -1, -2...

n = int(input('Enter the number: '))

print(f"The sum of n natural number is: {sum(n)}")
#here we used print to print the value of func as we used return statement in the function




# Enter the number: 7
# The sum of n natural number is: 28

#1 + 2 + 3 + 4 + 5 + 6 + 7
