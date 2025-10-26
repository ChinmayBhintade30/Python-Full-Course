#object attribute and class attributes


class Employee:
    language = "py"  #this is class attribute
    salary = 1200000

harry = Employee()
harry.name = "harry" #this ia an object attribute
print(harry.name,harry.language,harry.salary)


rohan = Employee()
rohan.name = "Rohan robinson roro"
print(rohan.name, rohan.language,rohan.salary)


# harry py 1200000
# Rohan robinson roro py 1200000


#here vs code also tell with the colour that
#name is object attribute and language and salary are the class attributes
#salary and language directly belong to the class

