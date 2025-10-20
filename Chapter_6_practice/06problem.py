# Write a program to find out whether a given post is talking about “Harry” or not

#As we know that 'in' keyword is has case sensitive

post = input("Enter the post: ")

if("Harry".lower() in post.lower()):
    print("This is talking about harry")
else:
    print("This post in not talking about harry")

# Enter the post: harry is the best guy ever and he is great
# This post in not talking about harry

#because the Harry in if condition is 'H' and 
# 'in' is case sensitive


# Enter the post: Harry is good and he is the greatest coder
# This is talking about harry


#To get output at any post without case sensitivity


# Enter the post: harRy is good boy
# This is talking about harry