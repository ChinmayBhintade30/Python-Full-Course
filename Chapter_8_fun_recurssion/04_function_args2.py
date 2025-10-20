#Also we can pass multiple arguments in function definition and pass the values in function call

'''
def greet(name,ending):
    print("Good day," + name )
    print(ending)

greet("rohan","Thank You!")
greet("harry","Thank You!")
# Good day,rohan Thank You!
'''


#Return value takes that value to the outside  variable of the function


# Good day,rohan
# Thank You!
# Good day,harry
# Thank You!


#we can simultanously print two variable values and pass it in function call seperated by (,)



#we can also create a variable and give it the value of function call 
#we can also give variable in function defintion and return that value
'''
def greet(name):
    gr ="hello " + name
    return gr


a = greet("harry")
print(a)
'''

# hello harry


#a is the variable which contains greet function call value which has parameter harry

#importance of return value
def goodDay(name,ending):
    print("Good day, "+name)
    print(ending)
    return "done"

a  = goodDay("harry","Thank you!")
print(a)
# None

# done
#as we have done as return value - we get done stored in a
#so the conclusion is - whatever we store in a will be the return value of the function



#Why none  - because you did not return any value
