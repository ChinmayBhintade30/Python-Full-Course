#Recurssion is function which calls itself
#ek aisa function hai jo apne aap ko hi call karta hai

#ek function call itself - because there is logic attached to it

'''
factorial(0) = 1
factorial(1) = 1
factorial(2) = 2 x 1
factorial(3) = 3 x 2 x 1
factorial(4) = 4 x 3 x 2 x 1
factorial(5) = 5 x 4 x 3 x 2 x 1


factorial = n * (n-1) * (n-2) * ....... 3 * 2 * 1
#recurssive call is written like this

means this is the logic of factorial inside the function names factorial

we got this formula of factorial for recurssive call of factorial function


factorial(n) = n * factorial(n-1)
we used this property and rewrite the formula in function definition and then it calls itself in same function definition


'''
#factorial fun calls itself in def again and again repetatively , and performs the factorial operation 
#base condition for factorial is if n==1 or n==0 

def factorial(n):
    if(n==1 or n==0):
        return 1
    return n * factorial(n-1)

#this is factorial function whcich is stack function

#this recurssion formula is not correct   then  - it will give infinite error when it will get executed




n = int(input("Enter the number: "))

print(f"The factorial of the following number is:{factorial(n)}")

# Enter the number: 5 
# The factorial of the following number is:120


# Enter the number: 7
# The factorial of the following number is:5040

# heere we know that the  factorial fucntion 

#Recurssion is the best direct way to code an algorithm

