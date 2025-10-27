# . Create a class “Programmer” for storing information of few programmers
# working at Microsoft.


class Programmer():
    company = "Microsoft"

    def __init__(self,name,salary, pin):
        self.name = name
        self.salary = salary
        self.pin = pin

p = Programmer("harry",1300000,232782)
print(p.name,p.salary,p.pin,p.company)

r = Programmer("rohan",1200000,327328)
print(r.name,r.salary,r.pin,r.company)


# harry 1300000 232782 Microsoft
# rohan 1200000 327328 Microsoft