import json
import os
memory_file = "memory.json"

def save_memory(messages):
    try:
        with open(memory_file, "w", encoding="utf-8") as file:
            json.dump(messages, file, indent=4)
    except OSError as error:
        print("JARVIS: Could not save memory", error)



def load_memory():
    if not os.path.exists(memory_file):
        return [
            {
            "role": "system",
            "content": (
                "You are JARVIS, a helpful personal AI assistant. "
                "Give clear, concise answers using simple language."
            )
        }
        ]
    try:
        with open(memory_file,"r",encoding="utf-8") as file:
            messages = json.load(file)
            return messages
    except(json.JSONDecodeError, OSError ) as error:
        print("JARVIS: Could not load memory:", error)
        return[]