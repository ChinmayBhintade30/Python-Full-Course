#It is similar to the mathematics sets 
#Venn diagram - union, intersection, difference, symmetric difference


#Common syntax:-

# print(s1.union/intesection/difference.(s2))



#Union():-
#Combines two sets (return new set)
a = {1,2}
b = {2,3}
#it also detects the duplicate values in set and takes only once
#return the element including all the elements in both sets - union
print(a.union(b))
# {1, 2, 3}



#intersection:-

#return common elements
#return the elements   which are common in both elements


c = {1,2,3}
d= {2,3,4}
#2 is common
#return element which are common in both the sets
print(c.intersection(d))
# {2, 3}


#difference:- Elements in first set but not in second
print(c.difference(d))
# {1}
#1 is in c but not in d



#symmetric difference:-
#elements in either set that is  present in only one set not in both
print(c.symmetric_difference(d))
# {1, 4}
#return set with curly braces {1,4} which are only present in c and d 


#repeatition of elements while union is not allowes in sets 


#difference one more method:-
#A-B
# >>> s1 = {1,2,3}
# >>> s2 = {2,3}
# >>> s1-s2
# {1}



