# Write a program to input name, marks and phone number of a student and format it
# using the format function like below:
# “The name of the student is Harry, his marks are 72 and phone number is 99999888”



name = input("Enter the name: ")
marks = int(input("Enter the marks: "))
phone = int(input("Ente the phone: "))

s = "The name of the studenrt is {}, his marks  are {} and phone number is {} ".format(name,marks,phone)

print(s)


# Enter the name: chinmay
# Enter the mar/ks: 100
# Ente the phone: 83473749
# The name of the studenrt is chinmay, his marks  are 100 and phone number is 83473749