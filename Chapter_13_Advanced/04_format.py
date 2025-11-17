#format methods strings

a = "{} is a good {}".format("harry","rohan")

print(a)

#the {} gets replaced with the string present in the format() 

#"contains {} and the text to be displayed "

#.format is used to add the elements on the right position , similar to f string

#Also we can give numbering for it for e. g 0 for harry and 1 for rohan 

b = "{1} is good {0}".format("Harry","Rohan")

print(b)

#we can just assign the index number to print the next element previously and the first element at the last 

# here 1 and 0 are replaced to change the values


# harry is a good rohan
# Rohan is good Harry