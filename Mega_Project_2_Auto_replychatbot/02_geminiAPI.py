import pyautogui
import time
import pyperclip
import google.generativeai as genai

# -----------------------------
#  Configure Gemini API key
# -----------------------------
genai.configure(api_key="AIzaSyAOvIfeYMB3V4aD-lDH-u4k_JA97H_cZwY")  # <-- replace with new key

# Use correct model name
model = genai.GenerativeModel("models/gemini-1.5-flash")  

# ---------------------------------------------------------
# Step 1: Click on the icon
# ---------------------------------------------------------
pyautogui.click(1350 , 1165)
time.sleep(1)

# ---------------------------------------------------------
# Step 2: Drag mouse to select the text
# ---------------------------------------------------------
pyautogui.moveTo(1817 , 493)
pyautogui.dragTo(1754 , 1001, duration=1.0, button='left')

# ---------------------------------------------------------
# Step 3: Copy selected text
# ---------------------------------------------------------
pyautogui.hotkey('ctrl', 'c')
time.sleep(1)

# ---------------------------------------------------------
# Step 4: Retrieve text from clipboard
# ---------------------------------------------------------
text = pyperclip.paste()
print("Copied Text:")
print(text)

# ---------------------------------------------------------
# Step 5: Send text to Gemini
# ---------------------------------------------------------
prompt = f"""
You are a polite assistant.
Read this text and generate a clear, short helpful reply for the student:

{text}
"""

response = model.generate_content(prompt)

# ---------------------------------------------------------
# Step 6: Print Gemini reply
# ---------------------------------------------------------
print("\nGemini Reply:")
print(response.text)
