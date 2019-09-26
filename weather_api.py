import requests

BASE_URL = "https://www.metaweather.com"
query = input("City?\n> ")
location_url = f"{BASE_URL}/api/location/search/?query={query}"
response = requests.get(location_url)
data = response.json()

location = data[0]['woeid']

weather_url = f"{BASE_URL}/api/location/{location}/"
response = requests.get(weather_url)
data = response.json()

weather = data['consolidated_weather']

for day in weather:
    desc = day['weather_state_name']
    date = day['applicable_date']
    temp = round(day['the_temp'], 1)
    print(f"{date}: {desc} ({temp} °C)")