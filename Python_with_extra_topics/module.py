import converter_module
"""
here the above syntax import module_name just imports the module and we have to use prefix object name with . operator
to call the function everytime


"""
from converter_module import lbs_to_kgs
"""
this method has different syntax as it says from module import the specific function in it so that 
we can directly call the function without using the . operator
"""
#we have imported or taken or used the file converter_module as py file which is called as an module

#here we just copy paste the code from the module file to reuse it here in well stuctured and oraganized way

#so that we need not to write every single line of code in the main py file

print(converter_module.lbs_to_kgs(70))
print(converter_module.kgs_to_lbs(60))
print(lbs_to_kgs(20))#9.0 --> it also return the same result because of specific function imported we can directly use the function

"""
we use . operator everytime to call the module file and use their functions which are written in it 

and pass the value for the function here so that it can return the value by executing th function 
"""

# 31.5/
# 133.33333333333334


#there are 2 methods to import a module - either by importing whole file and using . operator and
#either by specifically including the function from the module