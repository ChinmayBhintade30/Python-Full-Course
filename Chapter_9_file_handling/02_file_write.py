"""
This is for python write function

"""

#here this file is used to create a new file and write data into it

st = "hey harry you are amazing!"

f = open("myfile.txt","w")

f.write(st)

f.close()

# open ("myfile.txt", "w") doesnot exist , it is created and written in the folder

#write () function is used to write the data using the variable st in which we have our string

#we can see after this code is run , we get our file names myfile.txt in the folder created and get 
#string as hey harry you are amazing stored in st variable



