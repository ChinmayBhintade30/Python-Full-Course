#readilines() function is used to read the content of the file which gives the contents of the file 
# as list and also type of the file is list


f = open("file.txt","r")
# lines = f.readlines()
# print(lines, type(lines))

# line1 = f.readline()
# print(line1,type(line1))

# line2 = f.readline()
# print(line2,type(line2))

# line3 = f.readline()
# print(line3,type(line3))

# line4 = f.readline()
# print(line4,type(line4))

# line5 = f.readline()
# print(line5 == "")

# line6 = f.readline()
# print(line6 == "",type(line6))

#line 6 has no string , so it prints empty strings as --> as true
line = f.readline()
while(line != ""):
    print(line)
    line = f.readline()

f.close()

# here line = f.readline()
# while line!= "" means --> untill when line!= "" print the line 
# it prints 4 lines and then after when line gets equal to "" blank string , 
#loop  gets exit 

#jab tak sari lines print ho jati hai , yeh loop chalega

