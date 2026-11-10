from tools.applications import open_calculator, open_notepad
from tools.applications import open_applications
from tools.system_info import tell_date, tell_time
from tools.speech import speak   
from tools.ai_brain import ask_ai
def handle_command(command):
    
    if "hello" in command:
        speak("Hello! How can I help you?")
    elif "status" in command:
        speak("All systems are ready.")
    elif "time" in command:
        tell_time()
    elif "date" in command:
        tell_date()
    elif "open notepad" in command:
        # speak("Opening Notepad")
        open_notepad()
        # open_applications("notepad.exe")
    elif "open calculator" in command:
        open_calculator()
    elif "open youtube" in command:
       speak("Opening YouTube")
       open_applications("agimnkijcaahngcdmfeangaknmldooml")
    elif "open gmail" in command:
        speak("Opening Gmail")
        open_applications("fmgjjmmmlfnkbppncabfkddbjimcfncm")
    elif "open chat gpt" in command:
        speak("Opening chatGPT")
        open_applications("cadlkienfkclaiaibeoongdcgmdikeeg")
    elif "exit" in command:
        print("JARVIS: Shutting down. Goodbye!")
        return "exit"
    else:
        answer = ask_ai(command)
        speak(answer)
    return None