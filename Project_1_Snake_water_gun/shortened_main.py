import random


computer = random.choice([-1,0,1])

youstr = input("Enter your choice: ")
youDict = {"s":1,"w":-1,"g":0}
reversedict = {1:"Snake",-1:"Water",0:"Gun"}
you = youDict[youstr]
print(f"You chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer == you):
    print("Its a draw") 

   
else:
    '''

    #we considered every pattern and possibilities for the game


    if(computer == -1 and you == 1): 1-(-1) = -2
        print("you Win!")

    elif(computer == -1 and you == 0): -1 - 0 = -1
        print("You lose!")

    elif(computer == 1 and you == -1): 1 - (-1) = 2
        print("You lose!")


    elif(computer == 1 and you == 0):   1 - 0 = 1
        print("you Win!")

    elif(computer == 0 and you == 1): 0 -1 = -1
        print("you lose!")

    elif(computer == 0 and you == -1):  0 -(-1) = 1
        print("you Win")

    else:
        print("Something went Wrong!!! Try again")

    '''
    if((computer - you) == 1 or (computer - you == -2)):
       print("You win!")

    else:
        print("You  lose!")

'''
here to reduce the number of lines there is a logic of computer - you answer in condition
there is pattern that when it is (1,-2 ) in computer - you of value of condition - answer is Win

or if it is -1 and 2 , then it is lose



'''