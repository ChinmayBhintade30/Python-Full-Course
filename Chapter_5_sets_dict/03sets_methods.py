s = {1,23,45,34,5,"harry"}
print(s,type(s))
# {1, 34, 5, 23, 'harry', 45} <class 'set'>



s.add(54)
#adds an element to the set

print(s,type(s))
# {1, 34, 'harry', 5, 23, 54, 45} <class 'set'>


s.update([45,33])
print(s)
# {1, 34, 33, 5, 54, 23, 'harry', 45}
#update adds multiple elements from another iterable
#45 and 33 are addes to the sets in unordered form


s.remove(45)
print(s)
#45  is removed from the set

# {1, 34, 'harry', 33, 5, 54, 23} 
#removes ele 45 from the set and if not then it returns error


s.discard(5)
print(s)
# 5 is discarded from the set
# {1, 34, 33, 'harry', 54, 23} 


#pop
x = s.pop()
print(x,s)
#removes random element from the set 
# 1 {34, 33, 54, 23, 'harry'}
#it removes 1 randomly from the set and returned the rest of thelist

#copy()

#creates shallow copy of the set
t = s.copy()
print(t)
# {'harry', 34, 33, 54, 23}
#also order of the elements in set changes randomly


s.clear()
print(s)
#clear removes all the elements from the set
# set()
#empty set always returned as set()

s1  = {3,2,4,5,56,4}
print(len(s1))
# 5
#len function return the length of the set





