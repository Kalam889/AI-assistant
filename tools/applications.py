import subprocess
from tools.speech import speak

def open_notepad():
    speak("Notepad is opening.")
    subprocess.Popen(["notepad.exe"])
    

def open_calculator():
    speak("Calculator is opening.") 
    subprocess.Popen(["calc.exe"])
    
def open_applications(app_id):
    subprocess.Popen([r"C:\Program Files\Google\Chrome\Application\chrome_proxy.exe",
        "--profile-directory=Default",
        f"--app-id={app_id}"])