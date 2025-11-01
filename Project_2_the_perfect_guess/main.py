# We are going to write a program that generates a random number and asks the user to guess it.


#  If the player’s guess is higher than the actual number, the program displays “Lower number please”. 
# Similarly, if the user’s guess is too low, the program prints “higher number please”. 

# When the user guesses the correct number, the program displays the number of guesses the player used to arrive at the number.



import random

n = random.randint(1,100)
a = -1
#as a has to be defined and it will never become -1

guesses = 1
#beacuse by default you atleast need a single guess for it
#as we want to calculate and display the number of guesses

#while condition untill the guess doesnot becomes equal to the number generated randomly

while(a!=n):
    a = int(input("Guess the number: "))
    if(a>n):
        print("Lower number please")
        guesses += 1

    elif(a<n):
        print("Higher number please")
        guesses += 1



#as a == n the loop will end
print(f"you have guessed the number {n} correctly in {guesses} attempts")



# Guess the number: 34
# Lower number please
# Guess the number: 24
# Lower number please
# Guess the number: 14
# Higher number please
# Guess the number: 26
# Lower number please
# Guess the number: 25
# Lower number please
# Guess the number: 13
# Higher number please
# Guess the number: 17
# Higher number please
# Guess the number: 19
# Higher number please
# Guess the number: 21
# Lower number please
# Guess the number: 20
# Higher number please
# you have guessed the number 20 correctly in 10 attempts
