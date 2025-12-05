#logical operators are used combine two or more statements or conditions

#AND operator

"""
if applicant has high income and good credit score then eligible for loan should be print

"""

has_high_income = True
has_good_credit = False
has_criminal_record = False

if has_good_credit and not has_criminal_record:
    print("Eligible for loan")
    #this will evaluate as true result and print the message as not operator gets validated

if has_high_income and has_good_credit:
    print("Eligible for loan")

#Eligible for loan  --> as both the variable are true, it returns the true and executes the statement 


#And operator is has a result true when both the inputs are true

#either one of the above is false it will return false




"""
OR operator
"""

#same condition if high income OR good credit score then print eligible for loan


if has_good_credit or has_high_income:
    print("Eligible for loan ")


#In OR operator returns true if one of the 2 inputs either true and false is true

#when both the inputs are false --> the output is false

#AND : both should be true 
#OR : atleast one should be true
#NOT : inverts the result 


