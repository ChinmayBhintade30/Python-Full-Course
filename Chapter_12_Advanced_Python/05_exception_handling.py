try:
    a = int(input("Enter the number: "))
    print(a)
except Exception as e:
    print(e)

#try block should have atleast one except block objected as e and should print the error message automatically 
print("Thank you")


# Enter the number: sidy syd
# invalid literal for int() with base 10: 'sidy syd'
# Thank you

#but if i had not included the except and try block , then program would crash from the input statement itself
