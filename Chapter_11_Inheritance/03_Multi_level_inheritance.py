 #multi level inheritance

class Employee:
    a = 1

class Programmer(Employee):
    b = 2

class Manager(Programmer):
    c = 3

o = Employee()
print(o.a)
#prints the attribute a as object o is created using Employee class

o = Programmer()
print(o.a,o.b)
#here as programmer inherits the properties of Employee ,but not of Manager 
#we cannot print c attribute


o = Manager()
print(o.a,o.b,o.c)
# Multilevel inheritance which inherits the properties of class Employee and class Programme
  #we can print all 3 attributes a, b,c in this , as we have inherited the classes one into another
