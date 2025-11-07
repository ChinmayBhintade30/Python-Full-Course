#you can use multiple context managers in single with statement by using () parenthesis


with(
    open("file1.txt") as f1
    open("file2.txt") as f2

):
    

#process files