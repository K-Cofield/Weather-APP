from dotenv import load_dotenv
load_dotenv()
import requests
import os

def get_weather(api_key, location):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}&units=imperial"  # Changed units to imperial
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        temperature = data['main']['temp']
        humidity = data['main']['humidity']
        description = data['weather'][0]['description']
        return temperature, humidity, description
    else:
        return None, None, None

def main():
    api_key = os.environ.get('OPENWEATHER_API_KEY')
    if not api_key:
        print("API key not found. Please set the OPENWEATHER_API_KEY environment variable.")
        return

    while True:
        location = input("Enter a location (or 'exit' to quit): ")
        if location.lower() == 'exit':
            break
        temperature, humidity, description = get_weather(api_key, location)
        if temperature is not None:
            print(f"Weather in {location}:")
            print(f"Temperature: {temperature} °F, Humidity: {humidity}%, Description: {description}")  # Changed temperature unit to °F
        else:
            print("Error: Location not found or API error.")

if __name__ == '__main__':
    main()
