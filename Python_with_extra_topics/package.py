import ecommerce.shipping

#we write package name and module name using . operator in it 
#import package.module/file name

ecommerce.shipping.calc_shipping()

#now we can access the function inside the module used in  package ecommmerce 
#package.module.function



"""
we can use another approach that is from statement 

"""

#as the above method as complex structure of . operator 

from ecommerce.shipping import calc_shipping

calc_shipping()
calc_shipping()


#we can call the function multiple times directly using the from import statement method


#there is another method used in it
from ecommerce import shipping

shipping.calc_shipping()

#this is method in which we just imported the shipping module from the ecommerce package 
#and using the . operator with shipping.calc_shipping() we use the fucntion n it directly 
