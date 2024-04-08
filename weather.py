import requests

def getweather(apikey, city):
    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={apikey}&units=metric'
    response = requests.get(url)
    data = response.json()

    if data['cod'] == 200:
        weatherinfo = {
            'city': data['name'],
            'temperature': data['main']['temp'],
            'description': data['weather'][0]['description'],
            'humidity': data['main']['humidity'],
            'windspeed': data['wind']['speed']
        }
        return weatherinfo
    else:
        print(f"Error: {data['message']}")
        return None

def main():
    api_key = 'a89dc6cd5b6b6c2b853fc7c521b1b3d4'
    city = input("Enter city name: ")

    weather = getweather(api_key, city)

    if weather:
        print("")
        print(f"Weather in {weather['city']}:")
        print(f"Temperature: {weather['temperature']}°C")
        print(f"Description: {weather['description']}")
        print(f"Humidity: {weather['humidity']}%")
        print(f"Wind Speed: {weather['wind_speed']} m/s")
    else:
        print("Weather data not available for the specified location.")

if __name__ == "__main__":
    main()