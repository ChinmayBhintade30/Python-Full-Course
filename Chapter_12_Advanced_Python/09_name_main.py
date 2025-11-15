from module import myfunc

#here from keyword is used  to copy the whole module file created in the folder

#in this whole module file is copied in this file and myfunc function is run  in this
if __name__ == "__main__":
    #If this code is directly used or executed by running the file by the file its present in
    print("We are directly running this codwe from the file module itself ")

    myfunc()
    print(__name__)


#here the output is nothing as __name__ is not equal to the "main" in this main.py 


