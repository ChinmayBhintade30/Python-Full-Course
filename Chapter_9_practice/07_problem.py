# Write a program to find out the line number where python is present from ques 6.


with open("log.txt") as f:
    lines = f.readlines()

lineno = 1
for line in lines:
    if("python" in lines):
        print(f"Yes python is present in the file at line no : {lineno}")
        break
    lineno += 1 

else:
    print("No python is present in the file")
#here else is else block used with for , which executes only after the for loop exhausts

#if the break statement executes , then else doesnot executes

#if break statement and whole for loop exhausts then only else executes

