# 2. Write a program to print third, fifth and seventh element from a list using enumerate function


#Enumerate is the function used to acces or print the element in the list using i iterating variable 
# in one single statement

l = [1,2,3,4,5,6,7,8]

#we use enumerate fucntion (l) in the for loop 
for  i ,item in enumerate(l):
    if(i==2 or i==4 or  i==4 or i==6):
        print(item)


#as we know that we have been iterating the index i over the list l 

# so we have taken the index number from 0, 1,2,3  so 
#i==2 , i==4 , i==6

# 3
# 5
# 7



