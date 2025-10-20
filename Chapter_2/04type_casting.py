#type function() - used to find the datatype of the given variable

#type casting - used to convert the from one datatype to another datatype 

a = 31
print(type(a)) #<class 'int'>

b = "31"

print(type(b)) #<class 'str'>

c = 31
print(str(c))
print(float(c))
#31
# 31.0

d = "harry"
t = type(d)
print(t)


#by using type() function in python we can determine the datatype of any variable

#we can use inbuilt function to convert from one datatype to another

"""
str()
float()
int()
bool()

"""

e = "31.2"
r = float(e)
print(r)
print(type(r))
#31.2 is printed as floating type and type is float
#31.2
#<class 'float'>
#I want to convert this string type into floating point number 



