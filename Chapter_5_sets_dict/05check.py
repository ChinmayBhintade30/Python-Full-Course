#these methods are used to check the subsets , supersets and disjoint 
#return boolean values


#issubset:-
#Checks if all elments are in another set or not


#Syntax  - 
#(a.issubset/isdisjoint/issuperset(b))
#always a should be the subset of b

a = {1,2}
b = {1,2,3}
print(a.issubset(b))
# True



#issuperset
#check is set contains all element of another set

c = {1,2,3}
d ={1,2}
print(c.issuperset(d))

# True

#disjoint sets:-
#Checks if two sets have no common elements

e = {1,2}
f = {4,5}

#no common elements - true
#if found common elements - false

print(e.isdisjoint(f))
#true

print(a.isdisjoint(b))
#false
