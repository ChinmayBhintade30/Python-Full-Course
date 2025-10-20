#Write a program  to input eight numbers from the user  and display all the unique numbers
s = set()
#Always an empty set is created like this
#to create empty set we need set() keyword and () to assign it to variable

# In quesion it is mentioned as unique number - so set is the only thing which has unique numbers 
#non repetitive numbers



number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)

number = int(input("Enter the number: "))
s.add(number)


print(s)

#here 2 is entered for two times still it is displayed in set for once

# Enter the number: 2
# Enter the number: 4
# Enter the number: 5
# Enter the number: 3
# Enter the number: 6
# Enter the number: 7
# Enter the number: 2
# Enter the number: 8
# {2, 3, 4, 5, 6, 7, 8}


