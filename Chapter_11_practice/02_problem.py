# 2. Create a class ‘Pets’ from a class ‘Animals’ and further create a class ‘Dog’ from
# ‘Pets’. Add a method ‘bark’ to class ‘Dog’.


class Animals:
    def __init__(self):
        print(f"this is the class animals")
    
class pets(Animals):
    def __init__(self):
        print(f"This is class pets which is inherited from animals")


class dogs(pets):
    def __init__(self):
        print(f"This class is dogs which is inherited from pets")
        super.__init__()
    def bark(self,name):
        self.name = name
        print(f"This is the barking of the dog {self.name}")



d1 = dogs()
d1.bark("bhau")
    