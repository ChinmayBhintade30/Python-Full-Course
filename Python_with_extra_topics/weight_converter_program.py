#write a python program to convert the input weight from user input and 
#also give user the option of selecting the option of kg or lbs - pounds
#and print the value


"""
formula for wwight conversion is 
if you enter the weight in lbs
kgs = weight * 0.45

if you enter the weight in kgs
lbs = weight / 0.45


"""

weight = int(input("Enter the weight: "))
unit = input('(L)lbs or (K)kg: ')

if unit.upper() == "L":
    converted = weight * 0.45
    print(f"you are {converted} Kgs")

else:
    converted = weight / 0.45
    print(f"you are {converted} lbs")


# Enter the weight: 50 
# (L)lbs or (K)kg: k/
# you are 111.11111111111111 lbs
