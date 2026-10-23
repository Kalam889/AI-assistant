
import pyttsx3

def speak(text):
    print("JARVIS:", text)

    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine = None