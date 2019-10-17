# -*- coding: utf-8 -*-
import xlwings as xw

# importing request package
import requests
import pandas as pd
def hello_xlwings():
    wb = xw.Book.caller() # connecting to the book
    # base url of server
    BASE_URL = 'https://www.metaweather.com'
    sheet = wb.sheets[0]
    # getting input from the user
    # comes from cell A1 of my sheet
    city = sheet.range("A1").value
    
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
    # create a dictionary to store all the api data
    weather_dict = {
            'date': [],
            'weather': [],
            'temp': []
    }
    # looping through my data to get all the weather info for the next 6 days
    for day in weather_data:
        date = day['applicable_date']
        weather_condition = day['weather_state_name']
        crt_temp = day['the_temp']
        weather_dict['date'].append(date)
        weather_dict['weather'].append(weather_condition)
        weather_dict['temp'].append(crt_temp)
    # creating a dataframe out of the dictionary
    weather_df = pd.DataFrame(weather_dict)
    # writing the dataframe inside excel
    sheet.range('A2').value = weather_df

#hello_xlwings()