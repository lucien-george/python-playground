# -*- coding: utf-8 -*-

# Dictionaries
grades = {
    'john': 95,
    'paul': 80
}

print(type(grades)) # => dict

# Reading a value
print(grades['john'])
print(grades.get('jonny', None))

# Creating a key/value pair
grades['lucien'] = 86
print(grades)

# Checking if key is in the dictionary
if 'john' in grades:
    print('yes')
else:
    print('no')
    
# Updating a key/value pair
grades['john'] = 98
print(grades)


# Deleting key/value pair
del(grades['john'])
print(grades)

# CRUD
# Create
# => dict['new_key'] = new_value
#
# Read
# => dict['key']
#
# Update
# => dict['existing_key'] = new_value
#
# Delete
# => del(dict['key'])

# Looping over a dictionary with two variables. One for the key and one for its value
for name, grade in grades.items():
    print(f'{name} got {grade}')