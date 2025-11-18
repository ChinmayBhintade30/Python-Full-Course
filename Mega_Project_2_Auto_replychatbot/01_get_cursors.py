#using puauto gui for getting the position of the cursor so that the screen shot of that cursor can be feeded to openai


import pyautogui

while True:
    a = pyautogui.position()
    print(a)
    #1102 1179 --> chrome tab coordinates

    # 664, 175 coordinates of left corner
    #1869 , 1037
    # #1146 1121 right corner coordinates

#we can run this code again and again to generate the coordinates of the python file so that 
#there remain the accuracy fot the dragginng of the mouse cursor 