import os
import requests
from clarifai.client.model import Model

def get_food_calorie_count(image_url):
    # # Set up the Clarifai API client
    # os.environ['CLARIFAI_PAT'] = 'your_personal_access_token_here'
    model = Model(user_id="user_id", app_id="app_id", model_id="model_id")  # Replace with your user_id, app_id, and model_id

    # Use Clarifai API to identify food item in image
    model_prediction = model.predict_by_url(url=image_url, input_type="image")

    # Get name of identified food item
    # Assuming the result is in a structure where 'name' gives the identified food item
    food_item = model_prediction['outputs'][0]['data']['concepts'][0]['name']

    # Set up Nutritionix API client
    APP_ID = 'YOUR_APP_ID'
    APP_KEY = 'YOUR_APP_KEY'
    nutritionix_endpoint = f"https://trackapi.nutritionix.com/v2/natural/nutrients"
    headers = {
        "x-app-id": APP_ID,
        "x-app-key": APP_KEY,
        "Content-Type": "application/json"
    }
    data = {
        "query": food_item
    }
    response = requests.post(nutritionix_endpoint, headers=headers, json=data)
    nutrition_data = response.json()

    # Get calorie count for food item
    calorie_count = nutrition_data['foods'][0]['nf_calories']

    return food_item, calorie_count

if __name__ == "__main__":
    # Get image URL from user input
    image_url = input("Enter the URL of the image: ")
    food_item, calorie_count = get_food_calorie_count(image_url)
    print(f"The calorie count for {food_item} is {calorie_count} calories.")





# import requests
# import clarifai

# # Set up Clarifai API client
# from clarifai.rest import ClarifaiApp
# app = ClarifaiApp(api_key='')

# # Set up Nutritionix API client
# APP_ID = 'YOUR_APP_ID'
# APP_KEY = 'YOUR_APP_KEY'

# # Get image URL from user input
# image_url = input("Enter image URL: ")

# # Use Clarifai API to identify food item in image
# model = app.models.get('food-items-v1.0')
# response = model.predict_by_url(image_url)

# # Get name of identified food item
# food_name = response['outputs'][0]['data']['concepts'][0]['name']

# # Use Nutritionix API to look up calorie count for food item
# url = 'https://api.nutritionix.com/v1_1/search/{}?results=0:1&fields=item_name,brand_name,item_id,nf_calories&appId={}&appKey={}'.format(food_name, APP_ID, APP_KEY)
# response = requests.get(url).json()

# # Get calorie count for food item
# calories = response['hits'][0]['fields']['nf_calories']

# # Print calorie count for food item
# print("Calories for {}: {}".format(food_name, calories))