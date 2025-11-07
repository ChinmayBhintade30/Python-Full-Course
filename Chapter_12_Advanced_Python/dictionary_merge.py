#there are new operators | and |= used to merge dictionary and update the dictionaries

dict1 = {'a':1,'b':2}
dict2 = {'b':3,'c':4}
merged = dict1 | dict2
print(merged)


#output
# {'a': 1, 'b': 3, 'c': 4}