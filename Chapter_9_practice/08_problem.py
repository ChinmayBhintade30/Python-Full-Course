# Write a program to make a copy of a text file “this. txt”

#to create a file names this.txt and read it and then write it to other file using
#open function and modes like r and w , and check whether the data in the file gets copied or not

with open("this.txt","r") as f:
    content = f.read()


with open("this_copy.txt","w") as f:
    f.write(content)

