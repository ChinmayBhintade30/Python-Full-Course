#self parameter is a concept where self is used in methods defined  in class which takes argument of the object for it


class Employee:
    language = "py"
    salary = 120000

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print(f"hii there good morning!")


harry = Employee()
harry.language = "javascript" #this is an instance of object




#what happens is
harry.getinfo()
harry.greet()

# The language is javascript. The salary is 120000
# hii there good morning!


#Employee.getinfo(harry)



# The language is javascript. The salary is 120000



