#__init__() --> constructor whhich is automatically called when an object is created

class Employee:
    language = "py"
    salary = 120000

    def __init__(self): #dunder method which is called automatically
        print(f"I am creating this object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print(f"hii there good morning!")


harry = Employee()
harry.name = "harry"
 #this is an instance of object
print(harry.name,harry.salary)


# I am creating this object
# harry 120000

#why this def __init__() got printed although i didnt called it

#constructor --> has that property that it is a methods function , which is automcatically called
#without any function call , or without any object attribute or class attribute using . operator


#__init__() init method is just called when automatically


