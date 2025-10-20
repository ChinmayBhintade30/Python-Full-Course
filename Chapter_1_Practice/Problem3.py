#Install a python external Module and use it to perform an operation of your interest

#pyttx - python to text to speech module used to convert text to speech conversion 
#kind of jarvis/NLP/Alexa


import pyttsx3
engine = pyttsx3.init()
engine.say("Hii Cheif , i am Jarvis! Welcome to the Iron Man program,This is the world of Avengers " \
"I will be with you working for Iron man suit")
engine.runAndWait()


