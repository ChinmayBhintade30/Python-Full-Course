##classmethod is a decorator which is similar like staticmethod 
#which is used to overcome the priority of class attribute over object attribute

class Employee:
    a = 1   
    @classmethod
    #classmethod used on method using cls object 
    def show(cls):
        print(f"The class is attribute of a is {cls.a}")

# The class is attribute of a is 1


e = Employee()
e.a = 45    

e.show()
#this prints the class attribute as 1 now after using classmethod
#this will definitely print 45 , as object attribute > class attribute



# he class is attribute of a is 45


