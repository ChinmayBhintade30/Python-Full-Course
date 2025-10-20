# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.


#In exam your score needs to be greater or equal to the passing criteria

#so use logical operator for total marks >= 40 and each subject marks greater than equal to 33


marks1 = int(input("Enter the marks1: "))
marks2 = int(input("Enter the marks2: "))
marks3 = int(input("Enter the marks3: "))

#let us asssume the each subject pf 100 marks


total_percentage = ((marks1 + marks2 + marks3)/300)*100



if(total_percentage >= 40 and marks1 >= 33 and marks2 >= 33 and marks3>= 33):
    print("You are passed! Congratulations", total_percentage)

else:
    print("You failed!, Try again next year!", total_percentage)

#  Enter the marks1: 70
# Enter the marks2: 90
# Enter the marks3: 100
# You are passed! Congratulations 86.66666666666667   



