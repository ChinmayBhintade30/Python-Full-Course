#list methods / Inbuilt functions
#Lists are mutable in nature.
# we can make changes in same variable in list


friends = ["Apple","Orange",5,345.06,False,"Aakash","Rohan"]
friends.append("Harry")
print(friends)
# ['Apple', 'Orange', 5, 345.06, False, 'Aakash', 'Rohan', 'Harry']


l1 = [1,34,62,2,6,11]

# l1.reverse()
# [11, 6, 2, 62, 34, 1]

#l1.sort() #[1, 2, 6, 11, 34, 62]

# l1.insert(3,3333)
# [11, 6, 2, 3333, 62, 34, 1]

# l1.pop(3)
# [11, 6, 2, 34, 1]
#return value 2 when print the l1.pop(3)

# l1.remove(2)
# [1, 34, 62, 6, 11]
#print(l1)

l2 = [1 , 34, 54, 23, 45, 33, 33, 24]
print(l2.count(33))
# 2
# print(l2)
# [1, 34, 54, 23, 45, 33, 33, 24]


#here we see that there is no change in original list when count function is applied 
#as it return numeric value when the l2.count(value) is printed using print statement return the value 2
l2.clear()
print(l2)
# []

l3 = [1,34,23,45,22,65,45]
print(len(l3))

# 7

print(sum(l3))
# 235

print(max(l3))
# 65

print(min(l3))
# 1
