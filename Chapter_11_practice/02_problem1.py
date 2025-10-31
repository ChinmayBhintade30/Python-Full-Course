class Animals:
    pass

#just dont complicate any class by using any init method or self objct 
#you just want to show the inheritance happening

class pets(Animals):
    pass

#we have not included any implementation detail in pets and animals class , becuase it was not necessary


class dog(pets):
    #we need a bark method 
    #use static method to directly print it , without any self obj

    @staticmethod
    def bark():
        print(f"bow bow!")

d = dog()
d.bark()

#it prints bow bow!
