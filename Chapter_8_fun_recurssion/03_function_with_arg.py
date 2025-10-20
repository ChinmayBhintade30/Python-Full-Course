#we can write variable inside the parenthesis of the function to print the value given in functional call

#for example

def greet(name):
    print("Good day " + name)

greet("harry")
greet("Rohan")
greet("Chinmay")
greet("Saurabh")

# Good day harry

'''
Good day harry
Good day Rohan
Good day Chinmay
Good day Saurabh

'''

#name is the variable passed has argument in the greet function
#name is printed doing concatenation

#function call is passed with a "harry"

#harry passed has argument goes to defn of function and goes inside the name variable and gets executed in function 


#It is related to concept of pass by value and pass by reference

#The "harry" - string passed in function call goes in function defn defined with argument - variable -name 

#we can print as many as statements by passing different names in function call