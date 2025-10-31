# 3. Create a class ‘Employee’ and add salary and increment properties to it.
# Write a method ‘salaryAfterIncrement’ method with a @property decorator with a setter
# which changes the value of increment based on the salary.


#as the question implies create a class Employee and add properties salary and increment to it

#we have written salary and increment in class Employee

class Employee:
    salary = 10000
    increment = 20

    @property
    #this is getter which gets self obj and gets the value and returns it as class properties are set
    def salaryAfterIncrement(self):
        return (self.salary + self.salary * (self.increment/100))

    @salaryAfterIncrement.setter
    #here value is salary which is new incremented
    def salaryAfterIncrement(self,salary):
        self.increment = ((salary/self.salary)-1) * 100
e = Employee()
#just salaryAfterIncrement method is used to print the operation
print(e.salaryAfterIncrement)
e.salaryAfterIncrement = 12000
#we changes the incrment property by using setter 
print(e.increment)

#if we want to add instance properties we can write 
#a.salary and a.increment will be included in object 





#what is salary after the incrment --> salary + salary*(increment/100)

#increment is in percentage so 





# 12000.0

#his salary increased to 12000 after 20 % increase in 10000



#we have to change the increment value according to the salary using setter

#setter is used to change the value of increment property