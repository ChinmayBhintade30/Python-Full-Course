#Write a program to create a dictionary of hindi words with values as their english translation .
#Provide user to access it to know the meaning of hindi word

words = {
    "madad":"Help",
    "billi":"Cat",
    "behen":"sister",
    "maa":"mother"
}

word = input("Enter the word of which  do you want to know the meaning: ")

print(words[word])
# Enter the word of which  do you want to know the meaning: maa
# mother

#so here we created a dict of hindi and its english meaning words
#then word is variable which takes input from the  user that will be the key of the dictionary, 
#It prints the value when placed in dictionary indexing

