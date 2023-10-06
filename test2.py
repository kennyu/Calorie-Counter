import requests
import os

# API keys
api_key = ''

# Set up the image
with open('food.jpg', 'rb') as f:
    file_data = f.read()
    f.close()

# API endpoint
endpoint = 'https://api.clarifai.com/v2/models/bd367be194cf45149e75f01d59f77ba7/outputs'

# Set up headers and data
headers = {'Authorization': 'Key ' + api_key}
files = {'image': file_data}

# Make request and get response
response = requests.post(endpoint, headers=headers, files=files)

# Check for errors
if response.status_code != 200:
    raise Exception("Error getting prediction from Clarifai")

# Get first prediction concept and print name
concept = response.json()['outputs'][0]['data']['concepts'][0]
print(concept['name'])
