
from utils import find_max
numbers = [4,7,11,2,9,8]

maximum  = find_max(numbers)
print(maximum )# 11 is the largest number from the list 

#note :-> we have max built in function , although it is not showing any error 
#but using a built in function and redefining it is a bad practice of coding 


print(max(numbers))
#here when we used max in built function , it was confused which max function to call either the built in or used defined


# we used different name for variable to call the find_max function from the module 