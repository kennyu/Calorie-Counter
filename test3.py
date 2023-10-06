import cv2
import numpy as np
from tensorflow.keras.models import load_model
import transformers

# Load the model from Hugging Face
model = transformers.AutoModelForSequenceClassification.from_pretrained("Luke537/image_classification_food_model")

# Convert the model to TensorFlow Keras
model_keras = tf.keras.models.Model(model.input, model.output)

# Load pretrained image recognition model
model = load_model('food_model.h5')

# Dictionary mapping food labels to calorie counts
calorie_dict = {
    'apple': 95,
    'banana': 105,
    'pizza': 285,
    'burger': 354,
    'fries': 312,
    'pineapple':100
}

def get_calories(image):
    # Preprocess image for model
    image = cv2.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0)

    # Make prediction
    pred = model.predict(image)[0]
    food = np.argmax(pred)

    # Get calorie count
    if food in calorie_dict:
        calories = calorie_dict[food]
        print(f'Image contains {calories} calories')
    else:
        print('Could not recognize food')

# Usage
img = cv2.imread('food.jpg')
get_calories(img)