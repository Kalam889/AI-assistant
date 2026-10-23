import speech_recognition as sr

recognizer = sr.Recognizer()

def listen_for_command():
    try:
        with sr.Microphone() as source:
            recognizer.adjust_for_ambient_noise(source, duration = 1)
            print("JARVIS: Listening...")
            audio = recognizer.listen(source,
                                      timeout=5,
                                      phrase_time_limit=5)
            print("JARVIS: Audio captured successfully.")
            print("JARVIS: Sending audio to Google...")
        command = recognizer.recognize_google(audio)
        return command.lower().strip()
    except sr.WaitTimeoutError:
        print("JARVIS: Sorry, I couldn't understand you.")
        # print("DEBUG: No speech started within 5 seconds.")
    except sr.UnknownValueError:
        print("JARVIS: I couldn't hear you.")
        # print("DEBUG: Audio recorded, but speech was not recognized.")    
    except sr.RequestError as error:
        print("JARVIS: Recognition service error:", error)
        # print("DEBUG: Recognition service error:", error)
    except OSError as error:
        print("JARVIS: Microphone error:", error)
        # print("DEBUG: Microphone error:", error)
    return None
            