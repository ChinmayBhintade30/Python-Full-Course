'''
a = 3
b = 4
c = 5

average = (a+b+c)/3

print(average)


a = 34
b = 23
c = 56

average = (a+b+c)/3

print(average)



#or

a = int(input("Enter the number: "))
b = int(input("Enter the number: "))
c = int(input("Enter the number: "))

average = (a+b+c)/3

print(average)
'''

#for how many times you going to repeat this same task:-

#here comes the function -
#certain block of code which is repeated into the code as per the requirement
#It increases the reusability of the code
#reduces the code lines
#reduces the complexity

#function definition def fun_name():

'''
def avg():
    a = int(input("Enter the number: "))
    b = int(input("Enter the number: "))
    c = int(input("Enter the number: "))

    average = (a+b+c)/3

    print(average)

avg() #function call by its name

'''
#logic should be reused 
#function increases the reusability of the code
#using def we can define the function and its code logic

def fun1():
    print("Hello world!")

fun1()
#we can call the function by its function name followed by its parenthesis

# Hello world!
