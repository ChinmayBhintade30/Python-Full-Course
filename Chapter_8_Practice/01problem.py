#Write a program using functions to find greatest of three numbers.

def greatest(a,b,c):
    if(a>b and a>c):
        return a
    elif(b>a and b>c):
        return b
    elif(c>a and c>b):
        return c


a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))


print(greatest(a,b,c))



'''
Enter the number: 23
Enter the number: 34
Enter the number: 5
34

'''

'''
here we know that - greatest is the function having all the logic of finding the greatest number

we know that -  When it is called and variables are passed , they get reflectes into fuction definition and 
executes the problem

'''
#you need to print the values of the function , as the function has retuen statement , so , it returns the value but 
#you need to display the value using print statement

#if there was no return statement and there was a print statement , then you could directly call the function

# 