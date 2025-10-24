# 5. Repeat program 4 for a list of such words to be censored.

words = ["Donkey","ganda","bad"]
#we have list of words  and by iterating it , we can check wether the words are present in text file or not
with open("file.txt","r") as f:
    content = f.read()


for word in words:
    content = content.replace(word,"#" * len(word))
#here the # is multiplied by the length of the words which are mentioned in the list



with open("file.txt","w") as f:
    f.write(content)


