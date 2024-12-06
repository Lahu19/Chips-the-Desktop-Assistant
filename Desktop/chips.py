import typing
import pyautogui
import pyttsx3 #converts the entered text into speech.
import speech_recognition as sr
import pyaudio
import datetime
import time
import os
import wikipedia
import cv2
import webbrowser
import random
import sys
import pywhatkit  # pip install pywhatkit. is used for send messages and converting text into handwritten text images.
import pyjokes
# import pyautogui  provides the ability to simulate mouse cursor moves and clicks as well as keyboard button presses.
import requests
import psutil
import instadownloader
import instaloader
from PyQt5 import QtWidgets, QtCore , QtGui
from PyQt5.QtCore import QObject, QTime, QTimer, QDate,Qt
from PyQt5.QtGui import QMovie
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.uic import loadUiType
from desktop import Ui_MainWindow
# Remove one of these lines based on your preference
from translate import Translator
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextBrowser




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices)
engine.setProperty('voices', voices[0].id)


def speak(text):
    engine.say(text)
    engine.runAndWait()



def speak(audio):
    engine.say(audio)
    print(audio)
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
    print("The current date is ",day,"/", month,"/", year)

def wishme():
 
    speak("Welcome back !!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning !!")
       
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon !!")
       
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
       
    else:
        speak("Good Night Sir, See You Tommorrow")
    speak("Chips at your service sir, please tell me how may I help you.")
    
   
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


class MainThread(QThread):
    def __init__(self):
        super(MainThread, self).__init__()
    def run(self):
        self.task()
    

    def takecommand(self):
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            r.pause_threshold = 1
            audio = r.listen(source)

        try:
            print("Recognizing...")
            self.query = r.recognize_google(audio, language='en-in')
            print(f"user said {self.query}")

        except Exception as e:
            speak("Say that again please...")
            return "none"
        return self.query


    def task(self):
        wishme()
        while True:

            self.query = self.takecommand().lower()
    
            if "date" in self.query:
                date()

            elif "who are you" in self.query:
                speak("I'm Chips created by Team 1 and I'm a desktop voice assistant.")
                print("I'm Chips created by Team 1 and I'm a desktop voice assistant.")

            elif "how are you" in self.query:
                speak("I'm fine sir, What about you?")
                print("I'm fine sir, What about you?")

            elif "fine" in self.query:
                speak("Glad to hear that sir!!")
                print("Glad to hear that sir!!")

            elif "good" in self.query:
                speak("Glad to hear that sir!!")
                print("Glad to hear that sir!!")

            if 'wikipedia' in self.query:
                speak('ok wait sir, I am searching...')
                self.query = self.query.replace("wikipedia", "")
                results = wikipedia.summary(self.query, sentences=2)
                speak("According to wikipedia")
                print(results)
                speak(results)

            elif "open vscode" in self.query:
                path = "C:\\Users\\uttam\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
                os.startfile(path)
            elif 'open youtube' in self.query:
                webbrowser.open("www.youtube.com")
            elif 'open google' in self.query:
                webbrowser.open("www.google.com")
            elif 'open stackoverflow' in self.query:
                webbrowser.open("www.stackoverflow.com")
            elif 'play music' in self.query:
                music_dir = 'C:\\Users\\Uttam\\Desktop\\spotify\\songs'
                songs = os.listdir(music_dir)
                print(songs)
                os.startfile(os.path.join(music_dir, songs[0]))
                

            elif 'the time' in self.query:
                strTime = datetime.datetime.now().strftime("%H:%M:%S")
                speak(f"Sir, the time is : {strTime}")
            
            elif "open chrome" in self.query:
                apath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Google Chrome.lnk"
                os.startfile(apath)  
            
            elif "open command prompt" in self.query:
                os.system("start cmd")
            
            elif "open camera" in self.query:
                cap = cv2.VideoCapture(0)
                while True:
                    ret, img = cap.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==15:
                        break
                cap.release()
                cv2.destroyAllWindows()   
            
            elif "close word" in self.query:
                speak("okay sir, closing word application")
                os.system("Taskkill //f //in // WINWORD.EXE")
            elif "tell me a joke" in self.query:
                joke = pyjokes.get_joke()
                speak(joke)

            

            elif "sleep " in self.query:
                os.system("rundll32.exe powrprof.dil,SetSuspendState 0,1,0")

            elif 'switch the window' in self.query:
                pyautogui.keyDown("alt")
                pyautogui.press("tab")
                time.sleep(1)
                pyautogui.keyUp("alt")

            
            elif "instagram profile" in self.query:
                speak("Enter Instagram user name")
                name = input("Enter your Instagram user name:")
                webbrowser.open(f"www.instagra.com/{name}")
                speak(f"Sir here is the profile of the user {name}")
                speak("Sier would you like to download profile picture of this accound.")
                condition = self.takecommand().lower()
                if "yes" in condition:
                    mod = instaloader.Instaloader()
                    mod.download_profile(name, profile_pic_onlu=True)
                    speak("I am done sir, profile pictureis saved in our medial folde. now i am ready to do anothe task")
                else:
                    pass

            elif "take screenshot" in self.query:
                speak("Sir, please tell me the name for this screenshot file")
                name = self.takecommand().lower()
                speak("Please sir hold the screen for few seconds, i am taking screenshot")
                time.sleep(3)
                img = pyautogui.screenshot()
                img.save(f"{name}.png")
                speak("I am done sir, profile pictureis saved in our medial folder. now i am ready to do another task")
            
            elif "you can sleep" in self.query:
                speak("Ok sir,have a good day.")
                sys.exit()
            elif "check charging" in self.query or "battery" in self.query:
                import psutil
                battery = psutil.sensors_battery()
                percentage = battery.percent
                speak(f"Sir, our system has {percentage}% battery.")
                    
            elif "shutdown the system" in self.query:
                subprocess.run(["shutdown", "/s", "/t", "5"])
            
            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")
            
            elif "sleep the system" in self.query:
                os.system("rund1132.exe powrprof.d11,SetSuspendstate 0,1,0")

        
startExecution = MainThread() 

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        
    
    def startTask(self):
        self.ui.movie = QtGui.QMovie("desktop/9uttam.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        
        
app = QApplication(sys.argv)
jarvis = Main()
jarvis.show()
exit(app.exec_())

    
