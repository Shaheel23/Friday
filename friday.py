import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia 
import webbrowser
import os

def takecommand():
    #It takes input from user and return string output


    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening......!")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing......")
        query = r.recognize_google(audio, language='en-in') 
        print(f"User said: {query}\n")

    except Exception as e:

        print("say that again please")
        return "None"
    return query

                                         
                                         
engine=pyttsx3.init('sapi5')            #SAPI5 is a MICROSOFT SPEECH  RECOGNITION API 
voices=engine.getProperty('voices')

engine.setProperty('voice',voices[1].id)



def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour=int(datetime.datetime.now().hour)
    speak("Hello Sir I am Friday")
    if hour>=0 and hour<12:
        speak("Good Morning Shaheel. Have a nice workout and a good cup of tea with nice pack of toast!")
        
    elif hour>=12 and hour<16:
        speak("Good afternoon Shaheel. Just wind up all your work and have a healthy lunch consisting of chicken")

    else:
        speak("Good Evening Shaheel. Have a little workout and go out for a evening walk") 

    speak("And what work for today me sir?. I have just fixed all your schedules and all apointments resolved sir")  



if __name__ == '__main__':
    wishMe()
    while True:
        query = takecommand().lower()

        if 'wikipedia' in query:
            speak("Searching in Wikipedia..")
            query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=4)
            speak(results)
            print(results)

        elif 'open youtube' in query:
            webbrowser.open('youtube.com') 

        elif 'open google' in query:
            webbrowser.open('google.com')   

        elif 'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')

        elif 'open school' in query:
            webbrowser.open('w3schools.com')

        elif 'open facebook' in query:
            webbrowser.open('facebook.com')

        elif 'The time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir , the time is . {strTime}")

        elif 'play music' in query:
            music_dir = "C:\\songs"
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir , songs[2]))

        elif 'open vs code' in query:
            codepath = "C:\\Users\\Shaheel Sahoo\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)

        elif 'open spyder' in query:
            codepath = "C:\\Users\\Shaheel Sahoo\\anaconda3\\pythonw.exe" "C:\\Users\\Shaheel Sahoo\\anaconda3\\cwp.py" "C:\\Users\\Shaheel Sahoo\\anaconda3" "C:\\Users\\Shaheel Sahoo\\anaconda3\\pythonw.exe" "C:\\Users\\Shaheel Sahoo\\anaconda3\\Scripts\\spyder-script.py"  
            os.startfile(codepath)

        elif 'open chrome' in query:
            codepath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"

        elif 'open my games' in query:
            codepath = "C:\\Games\\INSIDE\\INSIDE.exe"

        elif 'open skype' in query:
            codepath = 'C:\\Program Files (x86)\\Microsoft\\Skype for Desktop\\Skype.exe'  