# -*- coding: utf-8 -*-

import requests

# Base url of the api
BASE_URL = 'https://www.metaweather.com'

# Getting the city from user's input
city = input('Find a city\n> ')

# url of first api call
location_url = f'{BASE_URL}/api/location/search/?query={city}'

# response of first api call
response = requests.get(location_url)

# converting the response to JSON
data = response.json()

# Grabbing the woeid of the location to be used in the second api call
woeid = data[0]['woeid']

# url of second api call
weather_url = f'{BASE_URL}/api/location/{woeid}/'

# response of second api call
response = requests.get(weather_url)

# converting the response to JSON
data = response.json()

# grabbing the weather information of the upcoming days
weather = data['consolidated_weather']

# Looping over each day
for day in weather:
    # digging through the response's content to get the relevant data
    date_info = f" {day['applicable_date']}" # getting the date
    weather_info = f"{day['weather_state_name']}" # getting weather information
    temp_info = f"({round(day['the_temp'], 1)} °C)" # getting temperature
    print(f"{date_info}: {weather_info} {temp_info}") #printing the result