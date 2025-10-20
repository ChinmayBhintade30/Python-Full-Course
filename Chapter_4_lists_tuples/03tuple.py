a = (1,3,5,6,3,4)
print(a)
print(type(a))
# (1, 3, 5, 6, 3, 4)
# <class 'tuple'>

b  = ()
print(type(b))
# <class 'tuple'>

c = (2,)
print(type(c))
# <class 'tuple'>



#tuple too can store different types of data it is heterogenous

a = (1,45, 342, 3424, False, "Rohan","Shivanm")
print(a)
print(type(a))

# (1, 45, 342, 3424, False, 'Rohan', 'Shivanm')
# <class 'tuple'>

# a[0] = 453
# Traceback (most recent call last):
#   File "d:\Python_Full_Course\Chapter_4_lists_tuples\03tuple.py", line 26, in <module>
    # a[0] = 453
    # ~^^^
# TypeError: 'tuple' object does not support item assignment


no = a.count(45)
print(no)
# 1

idx1 = a.index("Rohan")
print(idx1)
# 5
#rohan string is present on 5th index value of the tuple



my_tuple = (1,2,3)

repeated = my_tuple * 3

print(repeated)

# (1, 2, 3, 1, 2, 3, 1, 2, 3)


print(3 in my_tuple) #True

print(5 in my_tuple)  #False


print(len(my_tuple))
# 3


print(min(my_tuple))
# 1

print(max(my_tuple))
# 3

print(sum(my_tuple))
# 6

my_tuple2 = (8,3,5,2,9,4)

print(sorted(my_tuple2))
# [2, 3, 4, 5, 8, 9]
#sorted function returned the tuple into list form 


#same slicing concept like list and strings:

my_tuple3 = (1,2,3,4,5)
sliced = my_tuple3[1:4]
print(sliced)
# (2, 3, 4)