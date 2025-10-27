# Write a class “Calculator” capable of finding square, cube and square root of a
# number.



class Calculator:
    def __init__(self,n):
        self.n = n

    def square(self):
        print(f"The Sqaure is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The sqaure root is {self.n ** 1/2}")

#here we created 3 functions in for the calculator in the calculator class

a = Calculator(4)
a.square()
a.cube()
a.squareroot()


# The Sqaure is 16
# The cube is 64
# The sqaure root is 2.0

#just call to the methods via object.method() 
#__init__() constructor is used to store the value of n that is 4 in self.n and used as variable
