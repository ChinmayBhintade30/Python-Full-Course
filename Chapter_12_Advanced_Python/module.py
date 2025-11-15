def myfunc():
    print("hello there")



#here myfunc is  defined and it is  called below it

#this file is copied to the main.py file by using the keyword from


if __name__ == "__main__":
    #If this code is directly used or executed by running the file by the file its present in
    print("We are directly running this codwe from the file module itself ")

    myfunc()
    print(__name__)