
from functools import reduce
#Map example-->

l = [1,2,3,4,5]

square = lambda x: x*x
sqlist = map(square , l)
#collaborates the sqaure lambda function with the list l


#map function is used to map a lambda function and its expression with the 
#given list or datatype

# sqlist is variable used to store the value of map function 


# te map function sudha, is only for lambda keyword function using expression

#map(function_name, list_name)
print(list(sqlist))



#Filter function example
def even(n):
    if(n%2 == 0):
        return True
    return False

onlyEven = filter(even, l)
#filter -->/ filters the even numbers from list mentioned as per the condition 
#in even function only even function will return true , 
print(list(onlyEven))

# [1, 4, 9/, 16, 25]
# [2, 4]
#this even number gets sorted from the list 



def sum(a,b):
    return a+b

print(reduce(sum,l)) #15
#it forms the sequential computation in this addition


#the first argumemt of reduce is function  that is sum , and next arg is the variable

#sum function needs two bariables for addition

#it works as 2 by 2 form

"""
for e.g first  1+ 2 = 3 , then result of first two that is 3 and the next 3 gets added 
that is  6 + 4 that is 10 , but 10+5 needs to be 15 finally 

so the result of whole list is 15

"""

#we can also use lambda function for this reduce function

mul = lambda x,y:x*y

print(reduce(mul,l))
# 120
#it works as 1 * 2 = 3 then 2 * 3 is 6 , then 6 * 4 is 24 , then 24 * 5 is 120


