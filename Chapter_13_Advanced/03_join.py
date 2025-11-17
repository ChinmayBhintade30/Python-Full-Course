#join methosd is used to join the elements of the list to join with some certain symbols like - , :: etc

a = ["harry","rohan","Shubham"]

final = "::".join(a)

print(final)

# harry::rohan::Shubham

#here final is new variable in which --> "::" is inserted between every element of list by using .join(varible_name)

fruits = ["mango","apple","banana"]

result = ", and ,".join(fruits)

print(result)

# mango, and ,apple, and ,banana

#Anything between " " is inserted between the elements of the string called as join methods for strings
