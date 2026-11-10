import os
from groq import Groq
from tools.memory import save_memory, load_memory
client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)

messages = load_memory()
def ask_ai(question):
    messages.append(
        {
                            "role": "user",
                            "content": question
                        }
                    
    )
    
    try:
        response = client.chat.completions.create(
            
            model="openai/gpt-oss-120b",
            messages = messages
        )
        
        answer = response.choices[0].message.content
        messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )
        save_memory(messages)
        return answer
    except Exception as error:
        print("JARVIS: AI request failed", error)
        return "Sorry, I can not connect to my AI service right now."


# import os
# from groq import Groq
# from memory import save_memory, load_memory
# client = Groq(
#     api_key=os.getenv("GROQ_API_KEY")
# )

# messages= [
#                 {
#                 "role": "system",
#                 "content": (
#                     "You are JARVIS, a helpful personal AI assistant."
#                     "Give clear, concise answers using simple language."
#                 )
#                 }
                
                
                
#             ]
    
    
# def ask_ai(question):
#     messages.append(
#         {
#                     "role": "user",
#                     "content": question
#                 }
#     )
    
#     try:
#         response = client.chat.completions.create(
            
#             model="openai/gpt-oss-120b",
           
#             messages=messages
            
            
        
#         )
        
#         answer = response.choices[0].message.content
       
#         messages.append(
#             {
#                 "role":"assistant",
#                 "content":"answer"
#             }
            
#         )
#         save_memory(messages)
#         load_memory()
#         return answer
        
#     except Exception as error:
#         print("JARVIS: AI request failed", error)
#         return "Sorry, I can not connect to my AI service right now."