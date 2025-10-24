# Write a program to find out whether a file is identical & matches the content of
# another file.


#take two files text from the folder itself and compare it using == operator


with open("this.txt","r") as f:
    content1 = f.read()


with open("this_copy.txt","r") as f:
    content2 = f.read()

if(content1 == content2):
    print("yes the files are idenctical")

else:
    print("No the files are not identical")





