# Create a class with a class attribute a; create an object from it and set ‘a’
# directly using ‘object.a = 0’. Does this change the class attribute?


#here class attribute doesnot change, as we know that as object attribute is set , but 
#that doesn't mean that class attributes changes

class Demo:
    a = 4

o = Demo()
print(o.a) #prints the class attribute because instance attribute is not yet created and presnt


o.a  = 4 #instance attribute is created in this
print(o.a)
#prints the instance attributes as object attribute is now set to 0 and it has highest priority


print(Demo.a)

#this proves that class attribute in the demo class deosnot change
