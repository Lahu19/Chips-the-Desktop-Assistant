import tkinter as tk
from tkinter import ttk, scrolledtext
import threading
import pyttsx3
import datetime
import wikipedia
import webbrowser as wb
import os
import random
import pyautogui
import speech_recognition as sr
import speech_recognition as sr
import pyaudio
import wave
class DesktopAssistantUI:
    def __init__(self, master):
        self.master = master
        master.title("Desktop Assistant")

        self.style = ttk.Style()
        self.style.configure('TFrame', background='#e1d8b9')
        self.style.configure('TButton', background='#e1d8b9')
        self.style.configure('TLabel', background='#e1d8b9')

        self.output_text = scrolledtext.ScrolledText(master, width=60, height=20, wrap=tk.WORD, font=("Helvetica", 12))
        self.output_text.grid(row=0, column=0, columnspan=2, padx=10, pady=10)

        self.input_label = ttk.Label(master, text="Your command:")
        self.input_label.grid(row=1, column=0, padx=10, pady=5, sticky=tk.W)

        self.input_entry = ttk.Entry(master, width=50)
        self.input_entry.grid(row=1, column=1, padx=10, pady=5, sticky=tk.W)

        self.voice_button = ttk.Button(master, text="Voice Command", command=self.takecommand)
        self.voice_button.grid(row=2, column=0, padx=10, pady=5, sticky=tk.W)

        self.submit_button = ttk.Button(master, text="Submit", command=self.submit_command)
        self.submit_button.grid(row=2, column=1, padx=10, pady=5, sticky=tk.W)

        self.recognizer = sr.Recognizer()

    def submit_command(self):
        command = self.input_entry.get()
        self.output_text.insert(tk.END, 'You: ' + command + '\n')
        self.input_entry.delete(0, tk.END)
        threading.Thread(target=self.process_command, args=(command,)).start()

    def process_command(self, command):
        if "time" in command:
            self.time()
        elif "date" in command:
            self.date()
        elif "who are you" in command:
            self.speak("I'm Chips created by Team 1 and I'm a desktop voice assistant.")
        elif "how are you" in command:
            self.speak("I'm fine sir, What about you?")
        elif any(word in command for word in ["fine", "good"]):
            self.speak("Glad to hear that sir!!")
        elif "wikipedia" in command:
            self.search_wikipedia(command)
        elif "open youtube" in command:
            self.open_website("https://www.youtube.com")
        elif "open google" in command:
            self.open_website("https://www.google.com")
        elif "open stack overflow" in command:
            self.open_website("https://stackoverflow.com")
        elif "play music" in command:
            self.play_music()
        elif "open chrome" in command:
            self.open_chrome()
        elif "search on chrome" in command:
            self.search_on_chrome()
        elif "remember that" in command:
            self.remember(command)
        elif "do you remember anything" in command:
            self.recall_memory()
        elif "screenshot" in command:
            self.take_screenshot()
        elif "stop" in command:
            self.speak("Goodbye!")
            self.master.quit()
        else:
            self.speak("Please say the command again.")

    def capture_audio(self):
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
    def takecommand(self):
        self.speak("Listening...")
        audio_data = self.capture_audio()

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
            self.input_entry.insert(tk.END, text)
        except sr.UnknownValueError:
            self.speak("Unable to recognize speech")
        except sr.RequestError as e:
            self.speak("Error")

    def speak(self, audio):
        engine = pyttsx3.init()
        engine.say(audio)
        engine.runAndWait()

    def time(self):
        current_time = datetime.datetime.now().strftime("%I:%M:%S")
        self.speak("the current time is " + current_time)
        self.output_text.insert(tk.END, 'Chips: the current time is ' + current_time + '\n')

    def date(self):
        current_date = datetime.datetime.now().strftime("%d/%m/%Y")
        self.speak("the current date is " + current_date)
        self.output_text.insert(tk.END, 'Chips: the current date is ' + current_date + '\n')

    def search_wikipedia(self, command):
        try:
            self.speak("Ok wait sir, I'm searching...")
            query = command.replace("wikipedia", "")
            result = wikipedia.summary(query, sentences=2)
            self.speak(result)
            self.output_text.insert(tk.END, 'Chips: ' + result + '\n')
        except Exception as e:
            self.speak("Can't find this page sir, please ask something else")

    def open_website(self, url):
        wb.open(url)

    def play_music(self):
        print("Please allow the access to music directory functionality!")
        # Add your music playing logic here
    def open_chrome(self):
        chrome_path = "C:\\Program Files (x86)\\Google\\Chrome\\Application\\chrome.exe"
        os.startfile(chrome_path)
    
    def search_on_chrome(self):
        try:
            self.speak("What should I search?")
            search_query = self.input_entry.get()
            wb.get('www.chrome.com').open_new_tab(search_query)
            self.output_text.insert(tk.END, 'Chips: ' + search_query + '\n')
        except Exception as e:
            self.speak("Can't open now, please try again later.")

    def remember(self, command):
        self.speak("What should I remember?")
        memory = self.input_entry.get()
        # Save memory to file or database

    def recall_memory(self):
        # Retrieve memory from file or database
        memory = "Example memory"
        self.speak("You told me to remember that " + memory)
        self.output_text.insert(tk.END, 'Chips: You told me to remember that ' + memory + '\n')

    def take_screenshot(self):
        img = pyautogui.screenshot()
        img.save("screenshot.png")
        self.speak("I've taken screenshot, please check it")

def main():
    root = tk.Tk()
    app = DesktopAssistantUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
