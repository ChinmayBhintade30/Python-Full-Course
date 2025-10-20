#Write a python program to convert the inches to centimeters
'''
formula conversion for inches into cms :

cm = inches * 2.54

inches = cm / 2.54

'''

def inch_to_cms(inch):
    return inch * 2.54

inch = int(input("Enter the inches: "))


cms = inch_to_cms(inch)
print(f"The corresponding cms to given inches is : {cms}")

#here we have used print statement again the same reason - that - we are using return statement in the function definition


# Enter the inches: 10
# 25.4