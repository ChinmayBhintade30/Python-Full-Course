# Write a program to read the text from a given file ‘poems.txt’ and find out
# whether it contains the word ‘twinkle’.

f = open("poem.txt")
content = f.read()
#here f.read is opened in the variable content

if("twinkle" in content):
    print("The word 'twinkle' is present in the text file")
    #here we check that is the word twinkle present in the content or not

else:
    print("The word 'twinkle' is not present in the text file")

f.close()
#closing the file 


#output
# The word 'twinkle' is present in the text file

