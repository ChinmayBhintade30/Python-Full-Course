#write a program to print the content of a list using while loop

l = [1,"harry",False,"This","rohan","Shubham","Shubhi"]

i = 0

while(i < len(l)):
    print(l[i])
    i += 1


#here i = 0 , which iterates from 0 to len(l) that is 7 , but as we know the rule- it iterated till 6th element which is shubhi

# 1
# harry
# False
# This
# rohan
# Shubham
# Shubhi

#all the elements of the list are printed 

#when i gets to 7 , 7<7 this condition gets false - so while loop gets exited


