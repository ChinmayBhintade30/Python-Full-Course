#using puauto gui for getting the position of the cursor so that the screen shot of that cursor can be feeded to openai


import pyautogui

while True:
    a = pyautogui.position()
    print(a)
    #1350 , 1165 are the cordinates of whatsapp tab in my desktop for now --> 

    # 1817 , 493 coordinates of left corner
    
    # 1754 , 1001 right corner coordinates

#we can run this code again and again to generate the coordinates of the python file so that 
#there remain the accuracy fot the dragginng of the mouse cursor 