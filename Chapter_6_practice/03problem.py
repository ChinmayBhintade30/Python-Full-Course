#spam detection by detecting certain comments  containing following keywords

# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams

# Use  'in ' keyword to check the existence of particular string in variable or statement


p1 = "Make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message  = input("Enter the comment: ")
# "in " keyword used to check existing or not


if((p1 in message) or (p2 in message) or (p3 in message) or (p4 in message)):
    print("The comment is spam")

else:
    print("The comment is not a spam")

# Enter the comment: Hey I am good, please buy now
# The comment is spam


# Enter the comment: click this link , you will get the offer
# The comment is spam

