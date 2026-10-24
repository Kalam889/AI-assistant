import os
from groq import Groq

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

def ask_ai(question):
    try:
        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages = [
                {
                "role": "system",
                "content": (
                    "You are JARVIS, a helpful personal AI assistant."
                    "Give clear, concise answers using simple language."
                )
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )
        answer = response.choice[0].message.content
        return answer
    except Exception as error:
        print("JARVIS: AI request failed", error)
        return "Sorry, I can not connect to my AI service right now."