def goodday(name, ending = "Thank you"):
    print(f"Good day, {name}")
    print(ending)

goodday("harry","Happy ending")

#by default:-

# Good day, harry
# Thank you

#user given:-
# Good day, harry
# Happy ending


'''
Here we have given default value of ending variable in definition itself , so either we can pass another value in 
ending , or if we dont pass and print the value of ending,it prints the Thank you which is default value in 
Definition of function.Thank you directly reflects from the definition to the function call


'''

