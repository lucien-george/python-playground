# -*- coding: utf-8 -*-

import requests

BASE_URL = 'https://www.metaweather.com'
city = input('Find a city\n> ')

location_url = f'{BASE_URL}/api/location/search/?query={city}'
#print(location_url)

response = requests.get(location_url)
data = response.json()

woeid = data[0]['woeid']

weather_url = f'{BASE_URL}/api/location/{woeid}/'

response = requests.get(weather_url)
data = response.json()

weather = data['consolidated_weather']

for day in weather:
    date_info = f" {day['applicable_date']}"
    weather_info = f"{day['weather_state_name']}"
    temp_info = f"({round(day['the_temp'], 1)} °C)"
    print(f"{date_info}: {weather_info} {temp_info}")