import pyttsx3
import datetime
import speech_recognition as sr
import webbrowser as wb
import os
import google.generativeai as genai
from api import Gemini_API_KEY as api
engine = pyttsx3.init()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def time():
    Time = datetime.datetime.now().strftime("%I:%M:%S")
    speak("the current time is")
    speak(Time)
    print("The current time is ", Time)

def date():
    day = int(datetime.datetime.now().day)
    month = int(datetime.datetime.now().month)
    year = int(datetime.datetime.now().year)
    speak("the current date is")
    speak(day)
    speak(month)
    speak(year)
    print("The current date is ", day, "/", month, "/", year)

def wishme():
    print("Welcome back !!")
    speak("Welcome back !!")
    
    hour = datetime.datetime.now().hour
    if 4 <= hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif 12 <= hour < 16:
        speak("Good Afternoon !!")
        print("Good Afternoon !!")
    elif 16 <= hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tomorrow")

    speak("Chips at your service sir, please tell me how may I help you.")
    print("Chips at your service sir, please tell me how may I help you.")

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(query)

    except Exception as e:
        print(e)
        speak("Please say that again")
        return "Try Again"

    return query

def open_application(application_name):
    # Add more application paths as needed
    application_paths = {
        "notepad": "C:\\Windows\\System32\\notepad.exe",
        "calculator": "C:\\Windows\\System32\\calc.exe",
        # Add more applications here
    }

    if application_name in application_paths:
        os.startfile(application_paths[application_name])
        speak(f"Opening {application_name}")
    else:
        speak(f"Sorry, I couldn't find {application_name}")

genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if __name__ == "__main__":
    wishme()
    while True:
        #query = takecommand().lower()
        str= input('Enter Your Command : ')
        query = str.lower()
        if "time" in query:
            time()
        elif "date" in query:
            date()
        elif "who are you" in query:
            speak("I'm Chips created by Team 1 and I'm a desktop voice assistant.")
        elif "open" in query:
            words = query.split()
            open_application(words[-1])  # Assuming the last word is the application name
        elif "stop" in query:
            break
        else:
            response = chat.send_message(query)
            print("AI:", response.text)
    speak("Thank you for Using Chips")
    print("Thank you for Using Chips")
