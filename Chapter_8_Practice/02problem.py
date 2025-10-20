#Write a python program to convert from celsius to fahrenheit

'''
formula for celsius to fahrenheit

f = (c * 9/5) + 32


formula for fahrenheit to celsius

c = (f-32) * 5/9

'''

def temperature(c):
    f = (c * 9/5) + 32
    return f

c = int(input("Enter the temperature in celsius: "))
print(f"The Temperature in the fahrenheit is: {temperature(c)}")


# Enter the temperature in celsius: 35
# The Temperature in the fahrenheit is: 95.0