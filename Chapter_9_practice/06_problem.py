#Write a program to mine a log file and find out whether it contains ‘python’

#we will use html lorem435 to generate text in random file and add python word in it

#as use file read () and if condition


with open("log.txt","r") as f:
    content = f.read()

if("python" in content):
    print("Yes , python is present in the log file")

else:
    print("No , python is not present in the log file")


#here if and else condition is used --> to check the content variable 
#which has the data in file , and checks the word python in the log file


# PS D:\Python_Full_Course\Chapter_9_practice> python 06_problem.py 
# Yes , python is present in the log file



