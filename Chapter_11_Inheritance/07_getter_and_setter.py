class Student:
    def __init__(self,marks):
        self._marks = marks
    
    @property
    def marks(self):
        return self._marks  
    
    @marks.setter
    def marks(self,value):
        if(value < 0):
            print("Marks  cannot be negative")
        else:
            self._marks = value
            #is marks are above 0 , then assign the new value in object to self._marks
        


s = Student(85)
print(s.marks)
#calls getter to get the value as self and return the marks 
#as we have entered the marks first time

s.marks = 45
print(s.marks)
#calls setter to update the value safely using <property.setter.


s.marks = -12
#calls setter showing the warning of if condition