import requests

# Loads .env
import os 
from dotenv import load_dotenv
load_dotenv()

# GIF generation
# set API endpoint and parameters
url = "http://api.giphy.com/v1/gifs/search"
params = {
    "api_key": os.getenv('GIPHY_API_KEY'),
    "q": "funny cat",
    "limit": 1,
    "offset": 0,
    "rating": "g",
    "lang": "en"
}

# send a GET request to the API endpoint
response = requests.get(url, params=params)

# parse the JSON response and extract the GIF URL
data = response.json()
gif_url = data["data"][0]["images"]["original"]["url"]

print(gif_url)