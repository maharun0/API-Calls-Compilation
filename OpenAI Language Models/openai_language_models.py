import openai

# Loads .env
import os 
from dotenv import load_dotenv
load_dotenv()

# Authenticate with OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

## List the available models
models = openai.Model.list()

for model in models['data']:
    print(model['id'])

## Prompt the user and generate response
def get_AI_response(user_message):
    if user_message:

        # Generate response based on prompt
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=user_message,
            max_tokens=60,
            n=1,
            stop=None,
            temperature=0.9,
        )
    
    reply = response.choices[0].text

    return reply

# Get response in the terminal
while True:
    message = input('Enter prompt: ')
    reply = get_AI_response(message)
    print(f"ChatGPT: {reply}")