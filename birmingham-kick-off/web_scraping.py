# -*- coding: utf-8 -*-

# importing requests and BeautifulSoup for web scraping
import requests
from bs4 import BeautifulSoup

# importing pandas for data analysis
import pandas as pd

# storing the url of the webpage we want to scrape in the url variable
url = "https://www.lewagon.com/campuses"

# getting the HTML of the webpage using requests
response = requests.get(url)

# get the status of the request => 200 means OK
print(response.status_code)

# get the content of the webpage from the response
print(response.content)

# parsing/analyzing the content of the website using BeautifulSoup
# creating a variable called soup
soup = BeautifulSoup(response.content, 'html.parser')

# finding all the cities on the webpage based on the class their HTML tag has
cities = soup.find_all(class_='city-card')

# creating a dictionary to store the name and language of all the cities
# the dictionary has two keys, "names", and "languages"
# both keys store initially an empty list because we haven't retrieved the information from
# the website yet. And we use list because we have multiple names and multiple languages to store
# lists will allow us to store multiple values
cities_dict = {
    'names': [],
    'languages': []
}

# iterating over all the cities
for city in cities:
    # finding the name of the city which resides inside the <h3> tag that is located inside
    # the <div> element that has the class "city-card-info"
    city_name = city.find(class_='city-card-info').find('h3').string #.string removes the tag names
    # finding the language of the city which resides inside the <p> tag that is located inside
    # the <div> that has the class "city-card-content"
    # doing .string to remove the name of tag, .strip() to remove trailing and leading white spaces,
    # and .strip('Course in ') to remove this part of the text and keep only the language
    city_language = city.find(class_='city-card-content').find('p').string.strip().strip('Course in ')
    # adding the name on each iteration to the empty list stored inside the key 'names' in the dictionary
    cities_dict['names'].append(city_name)
    # adding the language on each iteration to the empty list stored inside the key 'languages' in the dictionary
    cities_dict['languages'].append(city_language)

# once the loop is done we print the dictionary we created to see the data
print(cities_dict)

# creating a dataframe from the dictionary `cities_dict`
cities_df = pd.DataFrame(cities_dict)

# printing the result
print(cities_df)