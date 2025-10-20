# Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.
# l = ["Harry", "Soham", "Sachin", "Rahul"]

#we are going to use S. startswith() function to check whether the name starts with S or not 

#iterate 'name' variable in list l







l = ["Harry", "Soham", "Sachin", "Rahul"]

for name in l:
    if(name.startswith('S')):
        print(f"Hello {name}")

        #again f string is used as hello {name} and in built method is used to check whether the name starts with S 

        #name is variable which iterates the list l such as index  -0,1,2... so on 
        #we dont use range function for iterating over - List, tuple, and strings
        

# Hello Soham
# Hello Sachin

 