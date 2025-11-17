import speech_recognition as sr
import webbrowser
import pyttsx3
import musicLibrary
import requests
#pip install pocketsphinx


#we imported speech recognition library as sr to make use in our code
#As per the python , webbrowser named module is a built in module in python 
#so need to include or install that 
#there is package called pyttsx3 which is package which converts text to speech 

recognizer = sr.Recognizer()
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    newsapi = "69e0c91ae59041489a27f6cd6ad6771d"

def processCommand(c):
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "facebook" in c.lower():
        webbrowser.open("https://facebook.com")
    elif "youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif "linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif c.lower().startswith("play"):
        song = c.lower().split(" ")[1]
        link = musicLibrary.music[song]
        #store this value of the valyue of the key from the dict in the varible key

        webbrowser.open(link)
    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&apiKey={"69e0c91ae59041489a27f6cd6ad6771d"}")
        if r.status_code == 200:
            data = r.json()

            articles = data.get("articles",[])

            for article in articles:
                speak(article['title'])
    

if __name__ == "__main__":
    speak("Initializing Jarvis")
    while True:
        #listen for the wake word jarvis
        #obtain audio  from the microphone
        r = sr.Recognizer()
        
        print("Recognizing....")
        
        #recognize using google function
        try:
            with sr.Microphone() as source:
                print("Listening..")
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            word = r.recognize_google(audio)
            if(word.lower() == "jarvis"):
                speak("Ya") 

                #Listen for command

                #again you have to take user input command from the listen function using microphone

                with sr.Microphone() as source:
                    print("jarvis Active...")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    processCommand(command)
                    #this sr.microphone will again take the user input from the user
                    #listen to the command with the help of r.recognizer and 
                    #will listen via listen function and store into command using google function

                    #write one function which will run after the command input

                   
                    #command we spoke after the jarvis become active , it print the command we spoke to him
                    # it takes command and replaces with the c in the processCommand

        except Exception as e:
            print("Error;{0}".format(e))

            












#I want that there should be two way interaction between me and jarvis

#we have many functions associated with recognize function liker ibm , google , aws , amazon etc 

#we will use google instead of sphinx
