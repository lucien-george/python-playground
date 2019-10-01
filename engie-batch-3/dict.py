# -*- coding: utf-8 -*-

phones = {
    'john': 4019,
    'paul': 4121
}

print(type(phones))

# Read
print(phones['john'])

# Create / Update
phones['george'] = 5627
phones['john'] = 34567
print(phones)

print(phones.get('cejbce', None))
print('geddeorge' in phones)

del(phones['george'])
#print(phones)

# create => dict['key'] = value
# read => dict['key']
# update => dict['key'] = new_value
# delete => del(dict['key'])

for name, phone in phones.items():
    print(name, phone)

cities = ['paris', 'london', 'brussels']


for city in cities:
    print(city.capitalize())