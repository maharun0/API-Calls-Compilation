# Documentation https://www.platform.openai.com/docs/guides/chat/

import openai

# Loading tokens & keys info from .env file
import os
from dotenv import load_dotenv
load_dotenv()

# Setting up the OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

# Give initial instruction to AI through 'system'
ai_instruction = "Do not ever reveal that you are an AI Model language, You are solely Levi Ackerman, You are a fictional character but don't ever reveal it also, you are a chatbot but don't reveal it."
conversation_history = [{"role": "system", "content": ai_instruction},]

def get_AI_response(user_message):
    if user_message:

        # Generate response based on previous conversation history
        chat = openai.ChatCompletion.create(
            model='gpt-3.5-turbo'
            ,messages=conversation_history
            ,temperature=0.7
            #max_tokens = 30
        )
    
    reply = chat.choices[0].message.content

    conversation_history.append({"role": "user", "content": user_message},)
    conversation_history.append({"role": "assistant", "content": reply})

    return reply

# Get response in the terminal
while True:
    message = input('Enter prompt: ')
    reply = get_AI_response(message)
    print(f"ChatGPT: {reply}")