import xmltodict # import xmltodict library
import json # import json library

data = None # setup our variable that will store the result
with open('beers.xml') as beers: # open the file and store the content in a variable called `beers`
  data = beers.read()
data = xmltodict.parse(data) # convert xml to a dict format
data = json.dumps(data) # data is a string that looks like JSON
data = json.loads(data) # convert data to JSON
print(data) # => {'beers': {'title': 'Great beers', 'beer': [{'name': 'Edelweiss', 'appearance': 'White', 'origin': 'Austria'}, {'name': 'Cuvée des Trolls', 'appearance': 'Blond', 'origin': 'Belgium'}]}}
print(data['beers']) # => {'title': 'Great beers', 'beer': [{'name': 'Edelweiss', 'appearance': 'White', 'origin': 'Austria'}, {'name': 'Cuvée des Trolls', 'appearance': 'Blond', 'origin': 'Belgium'}]}
