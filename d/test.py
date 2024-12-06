import pyttsx3
import speech_recognition as sr
import datetime
import os
import cv2
import random
from requests import get
import wikipedia
import webbrowser
import pywhatkit 
import sys
import time
import pyjokes
import subprocess
import pyautogui
import requests
import smtplib
import instaloader
import PyPDF2
import pywikihow
from pywikihow import search_wikihow
# import brd


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
    
    
    hour = datetime.datetime.now().hour
    tt = time.strftime("%I:%M %p")
    
    if 0 <= hour < 12:
        speak(f"Good morning sir,its {tt}")
    elif 12 <= hour < 18:
        speak(f"Good afternoon sir,its {tt}")
    else:
        speak(f"Good evening sir,its {tt}")
        
    speak("I am at your service sir,how can I help you.")
    
def sendEmail(to,content):
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.ehlo()
        server.starttls()
        server.login('your email id','your password')
        server.sendmail('your email id',to,content)
        server.close()
        
def news():
    main_url = 'http://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=cb3ee5cb9c2d428fb3222625a922a863'
    main_page = requests.get(main_url).json()
    articles = main_page["articles"]
    
    head = []
    day=["first","second","third","fourth","fifth","sixth","seventh","eighth","ninth","tenth"]
    for ar in articles:
        head.append(ar["title"])
    for i in range(len(day)):
        speak(f"today's {day[i]} news is: {head[i]}")
        
def pdf_reader():
    book = open('read.pdf','rb')
    pdfReader = PyPDF2.PdfFileReader(book)
    pages = pdfReader.numPages
    speak(f"Total number of pages in this book {pages}")
    speak("sir please enter the page number i have to read")
    pg = int(input("Please enter the page number here:"))
    page = pdfReader.getPage(pg)
    text = page.extractText()
    speak(text)
#def Taskexecution():
def get_current_location():
    try:
        # Get your public IP address using ipify.org
        ipAdd = requests.get('https://api.ipify.org').text

        # Use the IP address to fetch geolocation data
        url = f'https://get.geojs.io/v1/ip/geo/{ipAdd}.json'
        geo_data = requests.get(url).json()

        # Extract city and country information from the geo data
        city = geo_data['city']
        country = geo_data['country']

        return f"I think we are in {city} city of {country} country."
    except Exception as e:
        return "Sorry, I couldn't determine our current location due to a network issue."

    query = "where am I"

# Example usage

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
                if k==27:
                    break
            cap.release()
            cv2.destroyAllWindows()
            
        elif "open mobile camera" in query:
            import urllib.request
            import cv2 
            import numpy as np
            import time 
            # URL ="http://192.168.141.131:8080/shot.jpg"
            URL = "http://192.168.52.242:8080/shot.jpg"
            while True:
                img_arr = np.array(bytearray(urllib.request.urlopen(URL).read()), dtype=np.uint8)
                img = cv2.imdecode(img_arr, -1)
                cv2.imshow('IPWebcam', img)
                q = cv2.waitKey(1)
                if q == ord('q'):
                    break
            cv2.destroyAllWindows()
            
            
        elif "play music" in query:
             music_dir = "C:\\Users\\ADITYA\\Music\\ms"
             songs = os.listdir(music_dir)
             rd = random.choice(songs)
             for song in songs:
            #     if song.endwith('.mp3'):
                    os.startfile(os.path.join(music_dir, songs[0]))
                    
        elif "my ip address" in query:
            ip = get('https://api.ipify.org').text
            speak(f"you IP address is {ip}")
            
        elif "wikipedia" in query:
            speak("searching wikipedia")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            speak(results)
            #print(results)
            
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
            
        # elif "play song on youtube" in query:
        #    pywhatkit.playonyt("see you again")
           
        elif "email to adi" in query:
           try: 
            speak("what should i say")
            content = takecommand().lower()
            to = "adityashinde5154@gmail.com"
            sendEmail(to,content)
            speak("Email has been sent to Aadi")
            
           except Exception as e:
               print(e)
               speak("sorry sir, i am not able to send email")
               
        elif"you can sleep" in query:
            speak("Ok sir,have a good day.")
            sys.exit()
                
        elif "set alarm" in query:
            nn = int(datetime.datetime.now().hour)
            if  nn==22:
                music_dir = 'C:\\Users\\ADITYA\\Music\\ms'
                songs = os.listdir(music_dir)
                os.startfile(os.path.join(music_dir, songs[0]))

        elif "tell me a joke" in query:
            joke = pyjokes.get_joke()
            speak(joke)
            
        elif "switch window" in query:
            pyautogui.keyDown("alt")
            pyautogui.press("tab")
            time.sleep(1)
            pyautogui.keyUP("alt")
            
        elif "today news" in query:
            speak("Please wait sir,fetching the news")
            news()
            
        
        elif "where i am" in query or "where we are" in query:
            speak("wait sir, let me check")
            try:
                ipAdd = requests.get('https://api.ipify.org').text
                print(ipAdd)
                url = 'https://get.geojs.io/v1/ip/geo/'+ipAdd+'.json'
                geo_data = requests.get(url).json()  # Corrected variable name and added .json()
        
                city = geo_data['city']
                country = geo_data['country']
        
                speak(f"sir, I am not sure, but I think we are in {city} city of {country} country")
            except Exception as e:
              speak("sorry sir, due to a network issue, I am not able to find where we are.")
              pass
          
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
                pass
            
        elif "take screenshot" in query:
            speak("sir,please tell me name for this screenshot file")
            name = takecommand().lower()
            speak("please hold the screen for few seconds,i am taking screenshot")
            time.sleep(3)
            img = pyautogui.screenshot()
            img.save(f"{name}.png")
            speak("i am done sir, screenshot saved in main folder. now i am ready for next command.")
            

        elif "read pdf" in query:
            pdf_reader()

        elif "activate search mode" in query:
            speak("Mode is activated...")
            while True:
                speak("Please tell me what you want to know")
                how = takecommand()
                try:
                    if "exit" in how or "close" in how:
                        speak("Okay sir,closing the activated mode.")
                        break
                    
                    else:
                        max_results = 1
                        how_to = search_wikihow(how, max_results)
                        assert len(how_to[0].summary)
                        speak(how_to[0].summary)
                except Exception as e:
                   speak("Sorry sir, i am not able to find this.")
                   
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
            
        
        elif "where am I" in query or "where are we" in query:
            result = get_current_location()
            speak(result)  # You should have a function named "speak" to handle this
            
            