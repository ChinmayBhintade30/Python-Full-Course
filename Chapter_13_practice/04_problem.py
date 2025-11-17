l = [5,3,7,2,10,15,20,34,65,70]

def divisible(n):
    if(n%5 == 0):
        return True
    return False

s = filter(divisible,l)

print(list(s))

# [5, 10, 15, 20, 65, 70]

#here we used the l in which we have given some value list
