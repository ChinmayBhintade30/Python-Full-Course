class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"the class attribute is {cls.a}")

    @property
    def name(self):
        return f"{self.fname} {self.lname}"
    
    @name.setter
    def name(self,value):
        self.fname = value.split(" ")[0]
        self.lname = value.split(" ")[1]

#harry khan came into value and split function creates a list and assigns value
#to self.fname and lname objects 

#this objects  get returned in the property decorated name method
e = Employee()
e.a = 45


e.name = "harry khan"
print(e.fname,e.lname)

e.show()

#name is an attribute which is created using existing instance attribute
# harry khan
# the class attribute is 1


#This is just to show that user only types his full name but behing it , the whole process of 
#splitting the name into fname and lname occurs 
#called as abstraction and encapsulation


