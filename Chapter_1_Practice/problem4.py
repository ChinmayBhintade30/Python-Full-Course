# Write a program to print contents of directory using the OS module . Search Online for the function which does that
import os

# Get the path of the directory (you can change this)
path = "/"
# List all files and directories in the given path
contents = os.listdir(path)

print("Contents of directory:", path)
for item in contents:
    print(item)

# using / in path - it gives all content of C drive and prints it

