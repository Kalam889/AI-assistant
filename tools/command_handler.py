from tools.applications import open_notepad, open_calculator

from tools.system_info import tell_date, tell_time
from tools.speech import speak   

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
        open_notepad()
    elif "open calculator" in command:
        open_calculator()
    elif "exit" in command:
        print("JARVIS: Shutting down. Goodbye!")
        return "exit"
    else:
        print("JARVIS: I don't understand that command yet.")
    return None