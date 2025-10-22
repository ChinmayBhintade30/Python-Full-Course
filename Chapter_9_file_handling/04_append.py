#append the file to add something at the end 


st = "hey harry you are amazing!"

f = open("myfile.txt","a")

f.write(st)
# here the text st , appends at the end of the file "myfile.txt"

f.close()

