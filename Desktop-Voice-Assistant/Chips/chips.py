import pyttsx3
import pywin32_system32
import datetime
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import speech_recognition as sr
import pyaudio
import wave
import google.generativeai as genai
from api import Gemini_API_KEY as api
genai.configure(api_key=api)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

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
    print("The current date is ",day,"/", month,"/", year)

def wishme():
    print("Welcome back !!")
    speak("Welcome back !!")
    
    hour = datetime.datetime.now().hour
    if hour >= 4 and hour < 12:
        speak("Good Morning !!")
        print("Good Morning !!")
    elif hour >= 12 and hour < 16:
        speak("Good Afternoon !!")
        print("Good Afternoon !!")
    elif hour >= 16 and hour < 24:
        speak("Good Evening Sir!!")
        print("Good Evening Sir!!")
    else:
        speak("Good Night Sir, See You Tommorrow")

    speak("Chips at your service sir, please tell me how may I help you.")
    print("Chips at your service sir, please tell me how may I help you.")

def screenshot():
    img = pyautogui.screenshot()
    img.save("C:\\Users\\lahua\\Desktop\\desktop assistance\\")
def capture_audio():
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 1
    RATE = 44100
    RECORD_SECONDS = 10  # Increased recording duration to 10 seconds

    audio = pyaudio.PyAudio()

    stream = audio.open(format=FORMAT, channels=CHANNELS,
                        rate=RATE, input=True,
                        frames_per_buffer=CHUNK)

    print("Adjusting for ambient noise...")
    stream.start_stream()
    stream.read(CHUNK)  # Consume a chunk of audio to adjust for ambient noise

    print("Recording...")

    frames = []

    for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
        data = stream.read(CHUNK)
        frames.append(data)

    print("Finished recording.")

    stream.stop_stream()
    stream.close()
    audio.terminate()

    return b''.join(frames)
def takecommand():
    audio_data = capture_audio()

    with wave.open("recorded_audio.wav", "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(pyaudio.PyAudio().get_sample_size(pyaudio.paInt16))
        wf.setframerate(44100)
        wf.writeframes(audio_data)

    recognizer = sr.Recognizer()

    try:
        audio = sr.AudioFile("recorded_audio.wav")
        with audio as source:
            audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
        query= text
    except sr.UnknownValueError:
        query="Unable to recognize speech"
    except sr.RequestError as e:
        query="Error: {e}"

    return query

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
            print("I'm Chips created by Team 1 and I'm a desktop voice assistant.")

        elif "how are you" in query:
            speak("I'm fine sir, What about you?")
            print("I'm fine sir, What about you?")

        elif "fine" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "good" in query:
            speak("Glad to hear that sir!!")
            print("Glad to hear that sir!!")

        elif "wikipedia" in query:
            try:
                speak("Ok wait sir, I'm searching...")
                query = query.replace("wikipedia","")
                result = wikipedia.summary(query, sentences=2)
                print(result)
                speak(result)
            except:
                speak("Can't find this page sir, please ask something else")
        
        elif "open youtube" in query:
            wb.open("youtube.com") 

        elif "open google" in query:
            wb.open("google.com") 
   
        elif "open stack overflow" in query:
            wb.open("stackoverflow.com")

        elif "play music" in query:
            print("Plsease allow the access to music  directory functionality!")
            # song_dir = "#"
            # songs = os.listdir(song_dir)
            # print(songs)
            # x = len(songs)
            # y = random.randint(0,x)
            # os.startfile(os.path.join(song_dir, songs[y]))

        elif "open chrome" in query:
            chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" # require path of crome in local
            os.startfile(chromePath)

        elif "search on chrome" in query:
            try:
                speak("What should I search?")
                print("What should I search?")
                chromePath = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe" # like the path add here
                search = takecommand()
                wb.get(chromePath).open_new_tab(search)
                print(search)

            except Exception as e:
                speak("Can't open now, please try again later.")
                print("Can't open now, please try again later.")
            
        
        elif "remember that" in query:
            speak("What should I remember")
            # data = takecommand()
            # speak("You said me to remember that" + data)
            # print("You said me to remember that " + str(data))
            # remember = open("data.txt", "w")
            # remember.write(data)
            # remember.close()

        elif "do you remember anything" in query:
            remember = open("data.txt", "r")
            speak("You told me to remember that"+remember.read())
            # print("You told me to remember that ",(str)remember)

        elif "screenshot" in query:
            screenshot()
            speak("I've taken screenshot, please check it")
        elif "stop" in query:
            break
        else:
            print("Wait we are Generating....")
            response = chat.send_message(query)
            
            print("Chips: ", response.text)
speak("Thank you for Using Chips")
print("Thank you for Using Chips")