#try has an else block like how loop has else blocks

#if the try block gets executed successfully , it enters in  the else block

#otherwise  if the except block executes then --> it doesnot includes or executes the else block

try:
    a = int(input("Enter the number: "))
    print(a)

except Exception as e:
    print(e)

else:
    print("I am inside else")


# Enter the number: 34
# 34
# I am inside else

#it executes the try block and runs the else block
