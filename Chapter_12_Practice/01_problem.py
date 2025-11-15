# 1. Write a program to open three files 1.txt, 2.txt and 3.txt if any these files are not
# present, a message without exiting the program must be printed prompting the same.

"""
without exiting a problem means --> program should not crash by itself due to error it should 
display a message regarding  the error


using try and exception block for 3 files opening and to showcase the error 


"""
try:
    with open("1.txt","r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("2.txt","r") as f:
        print(f.read())

except Exception as e:
    print(e)

try:
    with open("3.txt","r"):
        print(f.read())

except Exception as e:
    print(e)

print("Thank you")



# this will get you the error message as try and error block and at the last print the thank you message

# [Errno 2] No such file or directory: '1.txt'
# [Errno 2] No such file or directory: '2.txt'
# [Errno 2] No such file or directory: '3.txt'
# Thank you

#If i create a file named 2.txt then the file will get read


