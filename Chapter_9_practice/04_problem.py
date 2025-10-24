# A file contains a word “Donkey” multiple times. You need to write a program
# which replace this word with ##### by updating the same file. 

#here we have to create a file with word donkey in it and replace it with #####

word = "Donkey"
#here word is defind as donkey

with open("file.txt","r") as f:
    content = f.read()

#file is opened in read mode--> in content variable


contentNew = content.replace(word,"######")

#replace --> the word donkey using .replace function and store it in new variable


with open("file.txt","w") as f:
    f.write(contentNew)


#again open the file in  write mode --> and write the contentNew in the file
