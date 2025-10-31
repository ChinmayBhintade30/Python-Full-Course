#we have to add and multiply two vector using dot product means
#dot product --> simple multiply x , y and z terms with i , j , k and add them


# 5. Write a class vector representing a vector of n dimensions. Overload the + and *
# operator which calculates the sum and the dot(.) product of them.



#as we know vector is generally of 3 dimensions x , y , and z which represent as
# i , j , k 


class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    # dunder methods used to operator overloading
    #__add__ , __sub__,__mul__, etc

    def __add__(self,other):
        result = Vector(self.x +other.x , self.y + other.y ,+ self.z + other.z)
        return result
    #this methods adds individual elements

#here other represents the vector which is taken to be with vector1 which will be assigned as self
    def __mul__(self, other):
        result = self.x * other.x + self.y * other.y + self.z * other.z 
        #when there is dot product multiplication  , we simply multiply x * x and then add it , as we want magnitude
        # dot product only provides --> A * B --> |A| |B| 
        #multiplied and sum 
        return result


    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})" 


#Test the implementation
v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = Vector(7,8,9)

#as we took 3 dimensions so use only 3 dimensions
#hyahca ek changla ahe ki , same dimension vector ahe


print(v1 + v2)
print(v1 * v2)
print(v1 + v3)
print(v1 * v3)

# Output-->

# Vector(5,7,9)
# 32
# Vector(8,10,12)
#50