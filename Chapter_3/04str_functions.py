name = "harry"

print(len(name))
# 5

print(name.endswith("rry"))
# True

print(name.endswith("ya"))
# False

print(name.endswith("rY"))
# False


#here the string function in python are case sensitive
#here upper case and lower case letter also matter and it checks in endswith() and startswith()


print(name.startswith("ha"))
# True

print(name.startswith("HA"))

# False


print(name.capitalize())#Harry


string = "abracadabra"
print(string.count("c"))
# 1


string1 = "hello world"
print(string1.find("world"))
# 6
#index of the first occurence of the word in the string
#It returns the index number of  occurence of the first character of the required word to find
#the first index of the world word is 6th 

print(string1.replace("world","python"))

# hello python

print(str(123))
# 123

word = "hello there"
print(word.upper())
# HELLO THERE

word1 = "HELLO ALL"

print(word1.lower())
# hello all


print(word.title())
# Hello There


print(word.rfind("e"))
# 10


print(word.split())
# ['hello', 'there']
#split() is used to seperate the words from the string into a list



word2 = "  hello  "

print(word2.strip())

# hello

word4 = " hello"
print(word4.lstrip())


word5 = "hello "
print(word5.rstrip())
#hello



#Check strings function - Boolean checks
char1 = "chinmay123"

print(char1.isalnum())
# True

char2 = "chinmay"
print(char2.isalpha())
#True


char3 = "12345"
print(char3.isnumeric())
#True

print(char3.isdigit())
#True


print(char2.islower())
#True

print(char2.isupper())
# False