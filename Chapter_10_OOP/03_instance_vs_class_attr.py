#if there are same attributes with the name in class and object 

#always instance attributes will be fetched and given the priority

class Employee:
    language = "py"  #this is class attribute
    salary = 1200000

harry = Employee()
harry.language = "javascript" #this ia an object attribute
print(harry.language,harry.salary)


# javascript 1200000

#Intance attributes takes preference over the class attributes during assignment and retrieval
