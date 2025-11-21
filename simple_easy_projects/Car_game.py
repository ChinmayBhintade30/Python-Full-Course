#our car game doesnot have any type of grahical interface GUI now , we are just focusing on
#build the engine function of the game



"""
the user will type help and it gives 3 options for it 

start - to start the car 
stop - to stop the car 

quit - to exit the game

and if user enters any other text , is should print i dont understand



start -->  Car started .. ready to go!!
stop --> Car stopped 
quit --> terminate the program
"""

command = ""
started = False  # car is initially stopped

while command != "quit":
    command = input("> ").lower()

    if command == "start":
        if started:
            print("Car is already started!")
        else:
            started = True
            print("Car started... Ready to go!")

    elif command == "stop":
        if not started:
            print("Car is already stopped!")
        else:
            started = False
            print("Car stopped.")

    elif command == "help":
        print("""
start - to start the car
stop - to stop the car
quit - to exit
        """)

    elif command == "quit":
        print("Game ended. Goodbye!")

    else:
        print("Sorry, I don't understand that.")

"""
there multiple condition that car is already started or already stopped

#so we also need a boolean value that is true for started and false for not started

#to check whether the car is already started or not or it is not started 



"""


# > stop
# Car is already stopped!
# > start 
# Sorry, I don't understand that.
# > start
# Car started... Ready to go!
# > start
# Car is already started!
# > help

# start - to start the car
# stop - to stop the car
# quit - to exit

# > jdoskd
# Sorry, I don't understand that.
# > quit
# Game ended. Goodbye!