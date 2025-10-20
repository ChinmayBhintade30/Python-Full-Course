#Write a python function using recursive call to print the following pattern

def pattern(n):
    if(n==0):
        return
    print("*" * n)
    #prints the asterisk for n times

    pattern(n-1)
    #this is recursive call to the function which again calls itself by substituting value 3-1 = 2 , 1..

pattern(5)
pattern(3)

#dirct call to function did the work of printing too



#here we used directly the function name and asterisk pattern  gets prinetd - how come?
#it is because we have used print statement for asterisk and return used for base condition does not return any value

