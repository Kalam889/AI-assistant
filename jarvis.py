from tools.applications import open_notepad, open_calculator

from tools.system_info import tell_date, tell_time

print("JARVIS: System online.")
while True:
    
    command = input("You: ")
    if command == "hello":
        print("JARVIS: Hello! How can I help you?")
    elif command == "status":
        print("JARVIS: All systems are ready.")
    elif command == "time":
        tell_time()
    elif command == "date":
        tell_date()
    elif command == "open notepad":
        open_notepad()
    elif command == "open calculator":
        open_calculator()
    elif command == "exit":
        print("JARVIS: Shutting down. Goodbye!")
        break
    else:
        print("JARVIS: I don't understand that command yet.")




































# import datetime
# import subprocess
# print("JARVIS: Systems online. Type 'exit' to shut down.")

# while True:
#     command = input("You: ")
#     command = command.lower()

#     if command == "hello":
#         print("JARVIS: Hello! How can I help you?")

#     elif command == "status":
#         print("JARVIS: All systems are ready.")
    
#     elif command == "time":
#         current_time = datetime.datetime.now()
#         print("JARVIS: The current time is", current_time.strftime("%I:%M %p"))
        
    
#     elif command == "open notepad":
#         subprocess.Popen(["notepad.exe"])
#         print("JARVIS: Opening Notepad...")


#     elif command == "exit":
#         print("JARVIS: Shutting down. Goodbye!")
#         break

#     else:
#         print("JARVIS: I don't understand that command yet.")

# from tools.applications import open_notepad, open_calculator
# from tools.system_info import tell_time, tell_date

# from tools.applications import open_notepad, open_calculator
# from tools.system_info import tell_time, tell_date



# print("JARVIS: Systems online. Type 'exit' to shut down.")

# while True:
#     command = input("You: ").lower().strip()

#     if command == "hello":
#         print("JARVIS: Hello! How can I help you?")

#     elif command == "status":
#         print("JARVIS: All systems are ready.")

#     elif command == "time":
#         tell_time()

#     elif command == "date":
#         tell_date()

#     elif command == "open notepad":
#         open_notepad()

#     elif command == "open calculator":
#         open_calculator()

#     elif command == "exit":
#         print("JARVIS: Shutting down. Goodbye!")
#         break

#     else:
#         print("JARVIS: I don't understand that command yet.")
# ---------
# import speech_recognition as sr

# from tools.applications import open_notepad, open_calculator
# from tools.system_info import tell_time, tell_date
# from tools.speech import speak



# recognizer = sr.Recognizer()


# def listen_for_command():
#     with sr.Microphone() as source:
#         print("JARVIS: Listening...")

#         recognizer.adjust_for_ambient_noise(
#             source, duration=1
#         )

#         audio = recognizer.listen(
#             source,
#             timeout=5,
#             phrase_time_limit=5
#         )

#     command = recognizer.recognize_google(audio)
#     return command.lower().strip()


# print("JARVIS: Voice systems online.")
# print("Say 'exit' to shut down.")

# while True:
#     try:
#         command = listen_for_command()
#         print("You:", command)

#         if command == "hello":
#             speak("Hello! How can I help you?")
#         elif command == "status":
#             print("JARVIS: All systems are ready.")

#         elif command == "time":
#             tell_time()

#         elif command == "date":
#             tell_date()

#         elif command == "open notepad":
#             open_notepad()

#         elif command == "open calculator":
#             open_calculator()

#         elif command == "exit":
#             print("JARVIS: Shutting down. Goodbye!")
#             break

#         else:
#             print("JARVIS: I don't recognize that command.")

#     except sr.WaitTimeoutError:
#         print("JARVIS: I didn't hear a command.")

#     except sr.UnknownValueError:
#         print("JARVIS: Sorry, I couldn't understand.")

#     except sr.RequestError as error:
#         print("JARVIS: Recognition service error:", error)
#         break

#     except OSError as error:
#         print("JARVIS: Microphone error:", error)
#         break


