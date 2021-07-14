import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id)
engine.setProperty('voice', voices[1].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak(f"Good Morning!")
        print("Good Morning!")

    elif hour>=12 and hour<18:
        speak(f"Good Afternoon!")
        print("Good Afternoon!")   

    else:
        speak(f"Good Evening!")
        print("Good Evening!")    

    speak("I am Alexa Sir. Please tell me how may I help you")  
    print("I am Alexa Sir. Please tell me how may I help you")      

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()


        # Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")   


        elif 'play song' in query:
            music_dir = 'D:\\PHONE\\Music'
            songs = os.listdir(music_dir)
            #print(songs)    
            os.startfile(os.path.join(music_dir, songs[random.randint(0,144)]))

        elif 'what is the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Sir, the time is {strTime}")

        elif 'open my coding area' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath)

        elif 'how are you alexa' in query:
            speak(f"I'm fine,sir")

        elif 'open my whatsapp' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\WhatsApp\\WhatsApp.exe"
            os.startfile(codePath)

        elif 'open amazon prime' in query:
            codePath = ""    

        elif 'some motivation' in query:
            speak(f"motherfucker asshole,u bastard")    

        elif 'stop alexa' in query:
            exit()    

 

        

 