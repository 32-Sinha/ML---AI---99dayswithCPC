import requests

def get_weather(city, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city,
        'appid': api_key,
        'units': 'metric'
    }
    response = requests.get(base_url, params=params)
    return response.json()

def display_weather(data):
    if data['cod'] == 200:
        city = data['name']
        country = data['sys']['country']
        temp = data['main']['temp']
        weather = data['weather'][0]['description']
        print(f"Weather in {city}, {country}:")
        print(f"Temperature: {temp}°C")
        print(f"Condition: {weather.capitalize()}")
    else:
        print("City not found!")

def main():
    api_key = "your_api_key_here"
    city = input("Enter city name: ")
    weather_data = get_weather(city, api_key)
    display_weather(weather_data)

if __name__ == "__main__":
    main()
