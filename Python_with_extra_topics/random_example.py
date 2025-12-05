#generating random numbers

import random

#use for loop with range function to iterate 3 times 
for i in range(3):
    print(random.randint(10,20))
    #this takes a range of number to generate the random numbers 
# 16
# 14
# 16

"""
random.random() generates random numbers betweene 0 and 1 

and for i in range( 3 ) gives it 3 times the iteration and execution of the code

"""

# 0.3725213925214923
# 0.47068179507053887
# 0.7987040653499615

#these are the numbers generated randomly between 0 and 1 with many decimal places --> and everytime it will change

#there is a method called random.choice - which will choose any random choice from the list 

members = ['john','mary','bob','mosch']
leader = random.choice(members)
print(leader)

# mosch - first time is chose mosch

# john - second time it chose john 
