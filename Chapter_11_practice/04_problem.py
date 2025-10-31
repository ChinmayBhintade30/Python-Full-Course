# 4. Write a class ‘Complex’ to represent complex numbers, along with overloaded
# operators ‘+’ and ‘*’ which adds and multiplies them.


# (a+bj)×(c+dj)=(ac−bd)+(ad+bc)j
# this is the formula for multiplication for complex numbers


class Complex:
    def __init__(self,r,i):
        self.r = r
        self.i = i

    def __add__(self,c2):
        #we use __add__ dunder method to add the self obj + c2 (real + img_part  i )

        return Complex(self.r + c2.r,self.i + c2.i)
    
    def __mul__(self,c2):
        # return Complex((self.r * c2.r - self.i * c2.i) + (self.r * c2.i + self.i * c2.r))
        real_part = self.r * c2.r - self.i * c2.i
        img_part = self.r * c2.i + self.i * c2.r
        return Complex(real_part,img_part)
    #this passes the parameters in complex as constructor init used at the beginning
    #which replaces it as self . r and self.i
    
    
    def __str__(self):
        return f"{self.r} + {self.i}i"
    
c1 = Complex(1,2)
c2 = Complex(3,4)
print(c1+c2)
print(c1*c2)

        

# 4 + 6i
#here we used __str__

# -5 + 10i
#we used complex number formula using chatgpt --> to write the mul method

#we used mul method and figured img part and real part and passed in Complex class
#dunder methods are used for operator over loading

# we use class name when to be used in dunder method to declare and perform the operations

