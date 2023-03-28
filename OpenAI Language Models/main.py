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
while True:
    prompt = input('Enter prompt: ')

    # Generate response based on prompts
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=60,
        n=1,
        stop=None,
        temperature=0.9,
    )

    reply = response.choices[0].text

    print(reply)