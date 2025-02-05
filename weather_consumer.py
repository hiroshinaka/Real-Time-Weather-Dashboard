from kafka import KafkaConsumer
import psycopg2
import json
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()
POSTGRES_HOST = os.getenv("POSTGRES_HOST")
POSTGRES_DATABASE = os.getenv("POSTGRES_DATABASE")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")


# PostgreSQL Connection
conn = psycopg2.connect(
    host=POSTGRES_HOST,
    database=POSTGRES_DATABASE,
    user=POSTGRES_USER,
    password=POSTGRES_PASSWORD
)
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
    CREATE TABLE IF NOT EXISTS weather (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
        city VARCHAR(100),
        temperature FLOAT,
        humidity FLOAT,
        description VARCHAR(100)
    )
""")
conn.commit()

# Kafka Consumer
consumer = KafkaConsumer(
    'weather',
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest'
)

for message in consumer:
    weather_data = json.loads(message.value.decode('utf-8'))
    city = weather_data['name']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    description = weather_data['weather'][0]['description']

    # Insert into PostgreSQL
    cursor.execute(
        "INSERT INTO weather (city, temperature, humidity, description) VALUES (%s, %s, %s, %s)",
        (city, temperature, humidity, description)
    )
    conn.commit()
    print(f"Stored weather data: {city}, {temperature}°C, {humidity}%, {description}")