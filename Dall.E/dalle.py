## Documentation: https://platform.openai.com/docs/guides/images/

import openai

# Loads .env
import os 
from dotenv import load_dotenv
load_dotenv()

# Authenticate with OpenAI
openai.api_key = os.getenv('OPENAI_API_KEY')

## Generate an image using prompt
prompt = input('Enter image prompt: ')

response = openai.Image.create(
  prompt=prompt,
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

## Edit an image
response = openai.Image.create_edit(
  image=open("sunlit_lounge.png", "rb"),
  mask=open("mask.png", "rb"),
  prompt="A sunlit indoor lounge area with a pool containing a flamingo",
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)

## Image variation
response = openai.Image.create_variation(
  image=open("corgi_and_cat_paw.png", "rb"),
  n=1,
  size="1024x1024"
)
image_url = response['data'][0]['url']
print(image_url)