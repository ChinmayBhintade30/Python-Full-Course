import pyautogui
import time
import pyperclip
#firts it imported all the libraries in it that is pyautoui for finding the location of the cursor





# step 1 : Click on the chrome  icon at coordinate (1102, 1179)
pyautogui.click(1346, 1169)

#time delay generated to wait for one sec to ensure the click is registered

# Step 2: Drag from (664, 175) to (1869, 1037) to select the text 
pyautogui.moveTo(659, 169)
pyautogui.dragTo(1533, 1034, duration=1.0, button='left')
#button left means the mouse left click to drag the text 
#drag for 1 sec


# Step 3: Copy the selected text to the clipboard
pyautogui.hotkey('ctrl', 'c') # to copy the text to the clipboard
pyautogui.click(1533, 1034)
time.sleep(1) #wait for 1 sec to ensure the copy command is completed 

# step 4 : retrive the text from the clipboard and store it in the text variable
# Paste copied content into a variable
text = pyperclip.paste()
#we make a variable text to copy the text in the pyperclip paste 


#step 5 : print the copied text to verify the code
print("Captured Text:")
print(text)

