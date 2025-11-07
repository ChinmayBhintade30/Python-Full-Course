#advances type hints like typing can be imported 

#it is used to import types like list , tuples, unions, dict


from typing import List , Union , Dict , Tuple


#list of integers-->
numbers: List[int]  = [1,2,3,4,5]

#as we know that list is always represented in [] and int is the type of element 
#in numbers variable

#Tuple of a string and an integer:

person: Tuple[str, int] = ("Alice", 30)

#here Tuple -- > and datatype str for alice and int or 30 is given in Tuple with square bracket[]

#here () is used for tuple 

#Dictionary with string keys and ineteger/ number values

scores = Dict[str, int] = {"Alice": 90,"bob":85}

#unoion type for variation that can hold multiple types 

identifier : Union[int , str] = "IDE123"
identifier = 12345

print(numbers)
print(person)
print(scores)
print(identifier)


