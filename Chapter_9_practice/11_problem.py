# Write a python program to rename a file to “renamed_by_ python.txt.

#it can be done by 2 methods

# --> either you can copy the content of file to other new file and rename it to renamed_by_python.txt

#either import os module 

with open("old_file.txt","r")as f:
    content  = f.read()

with open("renamed_by_python.txt","w")as f:
    f.write(content)

