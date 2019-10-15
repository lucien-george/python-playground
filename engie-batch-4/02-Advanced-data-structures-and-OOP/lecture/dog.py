# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, name):
        # data
        self.name = name # instance variables
        self.tricks = tricks # instance variables
        
    def learn(self, trick): # => behavior
        self.tricks.append(trick)

# aggresive_dog.py => Class AgressiveDog():
    
snoopy = Dog('Snoopy') # instance of Dog class
pongo = Dog('Pongo') # instance of Dog class

print(type(snoopy))
print(type(pongo))

print(snoopy.name)
print(pongo.name)

print(f'{snoopy.name} what can you do?')
print(snoopy.tricks)

snoopy.learn('sit')
print(f'{snoopy.name} what can you do?')
print(snoopy.tricks)
print(pongo.tricks)

# Data
# weight, age, breed, colar, name, height, ... => adjectives/nouns

# Behavior
# bark, play, run, bite, ... => verbs/actions