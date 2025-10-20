#Write a program whether the name given is present in the list or not

l = ["Harry","Rohan","Shubham","Divya"]

name = input("Enter you name: ")

if(name in l):
    print("your name is in the list")
else:
    print("your name is not in the list")



#As we know that - 'in' keyword is case sensitive so 
#is you enter - harry or shubham it will print the else block



# Enter you name: Shubham
# your name is in the list


