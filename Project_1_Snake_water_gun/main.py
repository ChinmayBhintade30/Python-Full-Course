#We always save project in main.py file name
'''
We all have played snake, water gun game in our childhood. If you haven’t, google the
rules of this game and write a python program capable of playing this game with the
user


Snake Water Gun is a simple hand game, similar to Rock-Paper-Scissors,
 where players simultaneously form one of three shapes: a snake, water, or a gun. 
 
 The winner is determined by 

 set of rules: snake eats water, water douses gun, and gun shoots snake
 s - w = s
 w - g = w
 g - s = g
'''

#This project is built using random library and also exception handling that is try and error block but
#This way is different

'''
We  have to convert everything in mathematical form for computation

1 - snake
-1 - water
0 - gun

'''

#use dictionary for choices and assign values as 1, -1 , 0 
#create variable which will access the value of dict by enetering key in form of s, w or g


#younum is having value of youDict by accesing it through user choice and accessed by youDict


#here we have to consider all the possibilities by the computer and the user

#using if else and elif condition
import random


computer = random.choice([-1,0,1])
#this will generate random choice by the computer 

youstr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reversedict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]
print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")
#this line tells that you chosed and access it as key in reverse dict and also puts the computer variable in indexing of reverse dict to access the option chosen by computer






#I want to know what user chose and what computer chose for that create a reversestring variable and 
#give key as 1, -1 and 0 and value as snake water gun

#This is example of nested if else ladder 
#if computer and you chose same choice - then there is condition of draw 
if (computer == you):
    print("Its a draw")

else:
    #we considered every pattern and possibilities for the game


    if(computer == -1 and you == 1): 
        print("you Win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")


    elif(computer == 1 and you == 0):
        print("you Win!")

    elif(computer == 0 and you == 1):
        print("you lose!")

    elif(computer == 0 and you == -1):
        print("you Win")

    else:
        print("Something went Wrong!!! Try again")

# You chose Snake
# computer chose Water
# you Win!
#basic working of snake water gun game


'''

This create infinite random possbilities:-

You chose Gun
computer chose Gun
Its a draw

You chose Snake
computer chose Water
you Win!


You chose Gun
computer chose Snake
you Win!

You chose Water
computer chose Snake
You lose!

You chose Water
computer chose Water
Its a draw

'''