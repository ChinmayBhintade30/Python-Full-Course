 #multi level inheritance

class Employee:
    def __init__(self):
        print("The is constructor of Employee")
    a = 1
    

class Programmer(Employee):
    def __init__(self):
        print("The is constructor of Programmer")
    b = 2

class Manager(Programmer):
    def __init__(self):
        super().__init__()
        #also prints the constructor of the programmer first

        print("The is constructor of Manager")
        #then prints the constructor of the Manager
        
    c = 3

# o = Employee()
# print(o.a)
#prints the attribute a as object o is created using Employee class

# o = Programmer()
# print(o.a,o.b)
#here as programmer inherits the properties of Employee ,but not of Manager 
#we cannot print c attribute


o = Manager()
print(o.a,o.b,o.c)
# Multilevel inheritance which inherits the properties of class Employee and class Programme
  #we can print all 3 attributes a, b,c in this , as we have inherited the classes one into another
