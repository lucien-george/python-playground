# Importing libraries
import requests
import pandas as pd
import numpy as np
from bs4 import BeautifulSoup

# Base url or website
BASE_URL = "https://www.ancestry.com/search/collections/numident/"

# url of first page
url = f"{BASE_URL}?birth=_mexico&birth_x=_1-0&count=50&race=hispanic&fh=43550&fsk=MDs0MzU1MDs1MA-61--61-"

# creating a dictionary to store all the names
names_dict = {
    'names': []
}
response = requests.get(url)
# Creating soup
soup = BeautifulSoup(response.content, 'html.parser')
# Getting HTML of all names by targetting the class `srchHit`
names = soup.find_all(class_='srchHit')

# iterating over all the names to add them to the empty list in the dictionary
for name in names:
    # adding the names to the list
    names_dict['names'].append(name.text.strip())

# finding the button that redirects to next page
next_page_link = soup.find(class_='iconArrowRight')
# while this link is there (meaning we are not on the last page yet), iterate and get the link of the next page
while next_page_link:
    print(len(names_dict['names']))
    # link of next page
    url = f"{BASE_URL}{next_page_link['href']}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    names = soup.find_all(class_='srchHit')
    for name in names:
        # adding the names to the list
        names_dict['names'].append(name.text.strip())
    # finding the next page if there is one
    next_page_link = soup.find(class_='iconArrowRight')
names_df = pd.DataFrame.from_dict(names_dict)
names_df.to_excel("names2.xlsx")