import requests

# print("Welcome to the Weather App!")
def get_weather(city_name):
    API_KEY = "c897a095880f40250759cf00fa7468f4"
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={API_KEY}&units=metric"

    print(f"Fetching weather data for {city_name}")
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f" City: {data['name']}")
        print(f" Temperature: {data['main']['temp']}°C")
        print(f" Humidity: {data['main']['humidity']}%")
        print(f" Wind Speed: {data['wind']['speed']} m/s")
        print(f" Weather: {data['weather'][0]['description'].title()}")
    else:
        print(f"Error: Unable to fetch weather data for {city_name}")

# Run
city = input("Enter city name: ")
get_weather(city)

