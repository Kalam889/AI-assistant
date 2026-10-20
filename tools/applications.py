import subprocess

def open_notepad():
    subprocess.Popen(["notepad.exe"])
    print("Notepad is opening.")

def open_calculator():
    subprocess.Popen(["calc.exe"])
    print("Calculator is opening.")