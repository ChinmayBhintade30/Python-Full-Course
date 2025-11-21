#guessing game --> you have to guess number 
# you wil get only 3 chances or attempts 
#you dont know whether to increase or decrease the number


# just use the names of the variable very professionally like a project

#using while loop  you can guess the number and also use if statement in it for == to the secret number 

#use else part for while part 


secret_number = 9
guess_count = 0
guess_limit = 3
while guess_count  < guess_limit:
    guess = int(input("Enter the guesss: "))
    guess_count += 1
    #as it starts from 0 to < 3 means only upto 2 

    if guess == secret_number:
        print("you won!")
        break

else:
    #to tell the user you made 3 guesses but none of them made it 
    print("Sorry ! you failed")

# Enter the guesss: 3
# Enter the guesss: 5
# Enter the guesss: 6
# Sorry ! you failed



# Enter the guesss: 9
# you won!


