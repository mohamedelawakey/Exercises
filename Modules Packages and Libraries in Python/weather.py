import os
import requests

API_KEY = os.getenv("WEATHER_API_KEY")  
lat = 30.0444
lon = 31.2357
URL = f"https://api.weatherbit.io/v2.0/current?lat={lat}&lon={lon}&key={API_KEY}&include=minutely"

response = requests.get(URL)

if response.status_code == 200:
    data = response.json()
    temp_c = data["data"][0]["temp"]
    condition = data["data"][0]["weather"]["description"]

    print(f"Temperature: {temp_c}°C")
    print(f"Condition: {condition}")
else:
    print("Failed to fetch weather data:", response.status_code)
