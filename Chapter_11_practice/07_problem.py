#7. Override the __len__() method on vector of problem 5 to display the dimension of the
# vector

#there can be multiple solutios on this so , by directly uisng the problem number 5 or 7

class Vector:
    def __init__(self,l):
        # self.x , self.y , self.z = l
        self.l = l
        

    
    
    def __len__(self):
        return len(self.l)
    
v1 = Vector([1,2,3])
#passed as list 
print(len(v1))#it gives an error
# 3


#this can be also done if there is variable length for this--> 

#pass the length of the vector
