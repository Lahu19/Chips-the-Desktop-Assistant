import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import webbrowser
import sys
import time
import pyjokes
import subprocess
import pyautogui
import instaloader
from pywikihow import search_wikihow

import google.generativeai as genai
from api import Gemini_API_KEY as api

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    print(audio)
    engine.runAndWait()
    
def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.energy_threshold = 400
        r.pause_threshold = 1
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}")
        return query.lower()
    except sr.UnknownValueError:
        speak("Speech recognition could not understand audio")
        return "none"
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")
        return "none"

def wish():
    
    speak("Welcome back !!")
    hour = datetime.datetime.now().hour
    tt = time.strftime("%I:%M %p")
    
    if 0 <= hour < 12:
        speak(f"Good morning sir!!")
    elif 12 <= hour < 18:
        speak(f"Good afternoon sir !!")
    else:
        speak(f"Good evening sir !!")
        
    speak("Chips at your service sir, please tell me how may I help you.")
    
    



# Example usage
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])
if __name__ == "__main__":
        wish()
    
while True:
        query = takecommand()
        #s=input("Enter the command: ")
        #query=s.lower()
        if "exit" in query:
            speak("OK sir have a good day.")
            break
        
        # Logic building tasks
        if "open notepad" in query:
            npath = "C:\\Windows\\notepad.exe"
            os.startfile(npath)
            
        elif "open chrome" in query:
            apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
            os.startfile(apath)
            
        elif "open command prompt" in query:
            os.system("start cmd")

        elif "open camera" in query:
            cap = cv2.VideoCapture(0)
            while True:
                ret, img = cap.read()
                cv2.imshow('webcam',img)
                k = cv2.waitKey(50)
                if k==15:
                    break
            cap.release()
            cv2.destroyAllWindows()
                    
        # elif "play music" in query:
        #      music_dir = "../music_dir"
        #      songs = os.listdir(music_dir)
        #      rd = random.choice(songs)
        #      for song in songs:
        #         if song.endwith('.mp3'):
        #             os.startfile(os.path.join(music_dir, songs[0]))
                    
        elif "my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"you IP address is {ip}")
            
            
        elif "open youtube" in query:
            webbrowser.open("www.youtube.com")
            
        elif "open facebook" in query:
            webbrowser.open("www.facebook.com")
            
        elif "open stack overflow" in query:
            webbrowser.open("www.stackoverflow.com")
            
        elif "open google" in query:
            speak("Sir,What should i search on google")
            cm = takecommand().lower()
            webbrowser.open(f"{cm}")
             
        elif "you can sleep" in query or "stop" in query:
            speak("Ok sir,have a good day.")
            sys.exit()
                

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUP("alt")

        elif "open instagram" in query or "profile on instagram" in query:
            speak("sir please enter the user name correctly")
            name = input("Enter user name here:")
            webbrowser.open(f"www.instagram.com/{name}")
            speak(f"sir here is the profile of the user {name}")
            time.sleep(5)
            speak("sir would you like to download profile picture of this account.")
            condition = takecommand().lower()
            if "yes" in condition:
                mod = instaloader.Instaloader()
                mod.download_profile(name, profile_pic_only=True)
                speak("i am done sir,profile picture is saved in our main folder.now i am read to next command")
            else:
                speak("Enter the valid id")
            
        elif "take screenshot" in query:
            speak("sir,please tell me name for this screenshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds,i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, screenshot saved in main folder. now i am ready for next command.")
 
        elif "check charging" in query or "battery" in query:
            import psutil
            battery = psutil.sensors_battery()
            percentage = battery.percent
            speak(f"Sir, our system has {percentage}% battery.")
                
        elif "shutdown the system" in query:
            subprocess.run(["shutdown", "/s", "/t", "5"])
            
        elif "restart the system" in query:
            os.system("shutdown /r /t 5")
            
        elif "sleep the system" in query:
            os.system("rund1132.exe powrprof.d11,SetSuspendstate 0,1,0")
        else:
            
            speak("Please wait sir, i am thinking")
            response = chat.send_message("Explain in 10 words"+query)
            print("Chips AI:", response.text)
        
            
            