import requests
import datetime as dt
import os

# **********************************************CONSTANTS**********************************************
API_KEY = os.environ["API_KEY"]
APP_ID = os.environ["APP_ID"]
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]
GENDER = "male"
WEIGHT_KG = 88
HEIGHT_CM = 180
AGE = 19

# **********************************************ENDPOINTS**********************************************
Exercise_Endpoints = " https://trackapi.nutritionix.com/v2/natural/exercise"

Sheety_Endpoint = os.environ["Sheety_Endpoint"]

# **********************************************INPUTS**********************************************
exercise_text = input("Tell me which exercises you did: ")

today = dt.datetime.now().strftime("%d/%m/%Y")

now_time = dt.datetime.now().strftime("%X")

# **********************************************REQUESTS**********************************************
header = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=Exercise_Endpoints, json=exercise_params, headers=header)
result = response.json()

# **********************************************PARAMS**********************************************


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    # Basic Authentication
    sheet_response = requests.post(
        Sheety_Endpoint,
        json=sheet_inputs,
        auth=(
            USERNAME,
            PASSWORD,
        )
    )
    print(sheet_response.text)
