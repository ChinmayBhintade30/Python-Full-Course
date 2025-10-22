#with statement is used to automatically open and close the file without using open and close statement


# f = open("file.txt")
# print(f.read())
# f.close()


# The same can be written using with statement like this!

with open ("file.txt") as f:
    print(f.read())

#this is the best way to operate that is open and close the file automatically



#you dont have to explicaitly close the file


