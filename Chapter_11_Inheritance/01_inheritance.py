class Employee:
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary of the employee is {self.salary}")


# class Programmer:
    # company = "ITC infotech"
    # def show(self):
    #     print(f"The name is {self.name} and the salary is {self.salary}")

    # def showLanguage(self):
    #     print(f"The name is {self.name} and he is good with {self.language} language")


#instead of using seperate class and copying the methods , we can use Inheritance

class Programmer(Employee):
    company = "ITC"
    def showLanguage(self):
        print(f"The name is {self.name} and he is good with {self.language} language")


#we can use the methods and attributes in Programmer from Employee
#inheritance is creating a new class from an existing class

a = Employee()

b = Programmer()

print(a.company,b.company)