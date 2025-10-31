# 1. Create a class (2-D vector) and use it to create another class representing a 3-D
# vector.


#we will use super().__init__(self, parameters of parent class or super class which you want to call)


class twoDvector:
    def __init__(self,i,j):
        self.i = i
        self.j = j
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j")


    
class threeDvector(twoDvector):
    #inherited the class twoDvector
    def __init__(self,i,j,k):
        #gets 3 dimensions i , j , k as it is three D vector
        super().__init__(i,j)
        self.k = k
    def show(self):
        print(f"The vector is {self.i}i + {self.j}j + {self.k}k")
a = twoDvector(1,2)
a.show ()
b = threeDvector(1,2,3)
b.show()    


#we have first created 2d vector which has 2 dimensions x and y , so we took i and j axis
#then using self and init we set them using self.i and self.j

#we used super() method to call i, j in the 3d vector class , so that we can call i, j and then set the k
#we set k using self.k = k

#so we have to also call twoDvector in threeDvector class by inheritance
        

# Output:-->
        
# The vector is 1i + 2j
# The vector is 1i + 2j + 3k