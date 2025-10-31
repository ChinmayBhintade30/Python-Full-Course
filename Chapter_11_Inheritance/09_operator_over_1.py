#__str__() method used to call the method to convert the object which is to be printed into str format


class Student:
    def __init__(self,name):
        self.name = name

    def __str__(self):
        return f"Student name is : {self.name}"
    

s = Student("chinmay")

print(s)
print(str(s))
        
#both print statments have the same result 

#print(s) also calls the __str__(self) to print the self.name as string 

#same way the next print(str(s)) statement also prints the same result in str format

#str () is used to conver the object s into str which is not necessary for __str__()

# Student name is : chinmay
# Student name is : chinmay


    