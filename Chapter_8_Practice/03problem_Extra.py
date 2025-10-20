#Write a program to convert from fahrenheit to degree celsius

def temperature(f):
    return (f-32) * 5/9


f = int(input("Enter the temperature in Fahrenheit: "))
c = temperature(f)
#here we created a variable c for readability of the code 

#we also want decimal places upto 2 


'''
Use round() function to round upto to decimal places
- round(variable, 2) here 2 represents the decimal places upto which you want

'''
print(f"The temperature in degree celsius is {round(c,2)} C") 
#Enter the temperature in Fahrenheit: 100
#The temperature in degree celsius is:  37.78 C


# Enter the temperature in Fahrenheit: 98
# The temperature in degree celsius is: 36.666666666666664



