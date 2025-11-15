l = [4, 532, 23, 234]

# index = 0
# for item in l:
#     index += 1
#     print(f"The item number {index} is {item}")


#this can be simplified using enumerate
# Enumerate function in python


for index , item in enumerate(l):
    print(f"The item number at the index {index} and {item}")

#this enumerate function get the index number and the element at the same time
