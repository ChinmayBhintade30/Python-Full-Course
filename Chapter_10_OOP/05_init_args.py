class Employee:
    language = "py"
    salary = 120000

    def __init__(self,name,salary, langauge): #dunder method which is called automatically
        self.name = name
        self.salary = salary
        self.language = langauge

        print(f"I am creating this object")

    def getinfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod
    def greet(self):
        print(f"hii there good morning!")


harry = Employee("harry",1300000,"Javascript")
# harry.name = "harry"
 #this is an instance of object
print(harry.name,harry.salary,harry.language)

# I am creating this object
# harry 1300000 Javascript