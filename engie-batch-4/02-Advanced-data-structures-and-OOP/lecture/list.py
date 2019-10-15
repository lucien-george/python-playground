# -*- coding: utf-8 -*-

# List
beatles = [ 'paul', 'john', 'ringo' ]
print(type(beatles)) # => list

# Read an element from a list
print(beatles[0])

# Reading a subset of a list
print(beatles[0:2])

# Create an element and add it at the end of the list
beatles.append('george')
print(beatles)
print(len(beatles))

# => for loop
beatles[0] = beatles[0].upper()
beatles[1] = beatles[1].upper()
beatles[2] = beatles[2].upper()
beatles[3] = beatles[3].upper()
print(beatles)


del(beatles[1])
print(beatles)

# CRUD
# Create
# => list.append(element)

# Read
# One element => list[index]
# Subset of the list => list[start_index:end_index]

# Update
# => list[index] = new_value

# Delete
# => del(list[index])

cities = ['paris', 'madrid', 'london']

# for loop on a list
for city in cities:
    print(city.capitalize())
    
cities.sort() # sorting a list

# for loop with two variables. One for the index and one for the element in the list
for index, city in enumerate(cities):
    print(f'{index + 1}. {city.capitalize()}')