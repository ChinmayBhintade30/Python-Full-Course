letter = ''' Dear <|Name|>,
You are selected!
<|Date|> '''


#what can be done - use string operation fucntion .replace and replace it with your name and date

# as letter is variable in which string is stored

#we can use .replace() twice in  a print statment for single variable and to replace multiple strings in it

print(letter.replace("<|Name|>","harry").replace("<|Date|>","24 september 2030"))

"""
 Dear harry,
You are selected!
24 september 2030


"""



