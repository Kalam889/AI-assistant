import subprocess
import webbrowser
from tools.speech import speak

def open_notepad():
    speak("Notepad is opening.")
    subprocess.Popen(["notepad.exe"])
    

def open_calculator():
    speak("Calculator is opening.") 
    subprocess.Popen(["calc.exe"])

def open_website(url):
    
    webbrowser.open(url)