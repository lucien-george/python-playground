# -*- coding: utf-8 -*-

# importing request package
import requests

# base url of server
BASE_URL = 'https://www.metaweather.com'

# getting input from the user
city = input('city?\n> ')

# enpoint for first api call
woeid_url = f'{BASE_URL}/api/location/search/?query={city}'

# getting back the data
response = requests.get(woeid_url)

# converting the data to json
data = response.json()

# digging through the data to get the woeid
woeid = data[0]['woeid']

# endpoint for second api call
weather_url = f'{BASE_URL}/api/location/{woeid}'

# getting back the data
response = requests.get(weather_url)

# converting data to json
data = response.json()

# digging through the data to retrieve the data that I need
weather_data = data['consolidated_weather']

# looping through my data to get all the weather info for the next 6 days
for day in weather_data:
    date = day['applicable_date']
    weather_condition = day['weather_state_name']
    crt_temp = day['the_temp']
    print(f'{date}: {weather_condition} ({round(crt_temp, 1)} °C)')