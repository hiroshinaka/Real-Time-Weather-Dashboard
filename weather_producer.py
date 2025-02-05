import requests
from kafka import KafkaProducer
import time
import os
import json
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
API_KEY = os.getenv("OPENWEATHER_API_KEY")

#City Coordinates
lat = 49.2827
lon = -123.1207

# Kafka Producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

def fetch_weather():
    print(f"Loaded API Key: {API_KEY}")
    url = f"https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error fetching weather data: {response.status_code}")
        return None

if __name__ == "__main__":
    while True:
        weather_data = fetch_weather()
        if weather_data:
            producer.send("weather", json.dumps(weather_data).encode('utf-8'))
            print(f"Sent weather data: {weather_data}")
        time.sleep(60)  