
# import pyttsx3

# def speak(text):
#     engine = pyttsx3.init()

#     print("JARVIS:", text)
#     engine.say(text)
#     engine.runAndWait()

#     engine.stop()



import pyttsx3

engine = pyttsx3.init()

def speak(text):
    print("JARVIS:", text)
    engine.say(text)
    engine.runAndWait()
