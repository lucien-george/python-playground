# -*- coding: utf-8 -*-

class Dog():
    def __init__(self, name):
        self.name = name # instance variables
        self.tricks = [] # instance variables
        
    def learn(self, trick_name):
        self.tricks.append(trick_name)

snoopy = Dog('snoopy')
pongo = Dog('pongo')
print("Snoopy what can you do?")
print(snoopy.tricks)
snoopy.learn('sit')
print("Snoopy what can you do?")
print(snoopy.tricks)
print("Pongo what can you do?")
print(pongo.tricks)


# => DATA (nouns)
# tail
# size
# color
# gender
# name
# breed
# price

# => BEHAVIOR (verbs)
# bite
# bark
# learn
# run
# eat
# sleep