#list comprehension

mylist =[4,9,3,5,8,2]

# squaredlist = []
# for item in mylist:
#     squaredlist.append(item * item)

# print(squaredlist)

# [16, 81, 9, 25, 64, 4]
#this is a normal way to create a new list which has square of previous number in it by using for loop
#we get the squares of each number as item iterates over the list 


#This code can be simplified and made  easy using single line of code using 

"""
list comprehension

"""


squaredlist = [i*i for i in mylist]

print(squaredlist)
# [16, 81, 9, 25, 64, 4]
# we get the same output as previous one

#we made use of i * i operation in same list [] and also for loop in same line of code using i variable 
#iterating over the mylist
