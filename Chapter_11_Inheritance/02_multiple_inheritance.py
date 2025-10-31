class Employee:
    company = "ITC"
    name = "Default name"
    salary = 120000
    def show(self):
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")


class Coder:
    language = "python"
    def printLanguages(self):
        print(f"from all the languages here is your language: {self.language}")

    
        


#instead of using seperate class and copying the methods , we can use Inheritance

class Programmer(Employee,Coder):
    company = "ITC infotech" 
    def showLanguage(self):
        print(f"The name is {self.company} and he is good with {self.language} language")


#we can use the methods and attributes in Programmer from Employee
#inheritance is creating a new class from an existing class

a = Employee()

b = Programmer()

b.show() #method inherited from parent class Employee
b.showLanguage()# method from the child class Programmer itself no inherited
b.printLanguages()#method inherited from the 2nd parent class Coder



# The name of the employee is Default name and the salary of the employee is 120000
# The name is ITC infotech and he is good with python language
# from all the languages here is your language: python

#all the method from derived class as well as parent class are executes


#The order of the method in class depends on the function call of the user
