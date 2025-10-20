#Write a python program function to remove a given word from  a list and strip it at the same time


def rem(l,word):
    n = []
    for item in l:
        if not(item == word):
            n.append(item.strip(word))
    return n

l = ["harry","Rohan","Shubham","an"]

print(rem(l,"an"))


# ['harry', 'Roh', 'Shubham']

#here we used rem function with list l and word 'an' whcih we want to remove

#as item iterates in l as if item not equal to word given, then append it into new string 
#if not(item == word)
#and remove an from rohan and elements get added to newly formed list l
#n.append() used to add the element to  new list,  and prints the rest of the values

