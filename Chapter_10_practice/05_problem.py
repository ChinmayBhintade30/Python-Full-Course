# Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats)
# and get fare information of train running under Indian Railways.

from random import randint
class Train:
    
    def __init__(self,trainNo):
        self.trainNo  = trainNo
    
    def book(self, fro ,to):
        print(f"Ticked is booked in train number : {self.trainNo} from {fro} to {to}")


    def getStatus(self):
        print(f"Train no : {self.trainNo} is running on time")

    def getFare(self,fro ,to):
        print(f"Ticket fare in train no: {self.trainNo} from {fro} to {to} is {randint(222,4999)}")


t = Train(12345)
t.book("bengaluru","delhi")
t.getStatus()
t.getFare("bengaluru","delhi")

# Ticked is booked in train number : 12345 from bengaluru to delhi
# Train no : 12345 is running on time
# Ticket fare in train no: 12345 from bengaluru to delhi is 4621