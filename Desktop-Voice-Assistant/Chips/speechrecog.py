import speech_recognition as sr
import pyaudio
import wave

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

if __name__== "__main__":
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
        print("You said:", text)
    except sr.UnknownValueError:
        print("Unable to recognize speech")
    except sr.RequestError as e:
        print(f"Error: {e}")