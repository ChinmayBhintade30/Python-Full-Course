age = int(input("Enter the age: "))

#if else elif ladder

if(age >= 18):
    print("You are the above the age of consent")
    print("Good for you")

elif(age < 0):
    print("you are entering an invalid negative age")

elif(age == 0):
    print("Your are entering an invalid age ")

else:
    print("you are below the age of consent")


print("End of the Program")

