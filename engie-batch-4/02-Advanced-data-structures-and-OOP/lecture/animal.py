# -*- coding: utf-8 -*-

# Parent class
class Animal():
    def __init__(self, name):
        self.name = name # instance variables
        self.tricks = [] # instance variables
        
    def learn(self, trick):
        self.tricks.append(trick)
    
    def talk(self):
        print('animal talks')

# Dog class inherits all the data and behavior from the Animal class
# child class
class Dog(Animal):
    def talk(self):
        print('bark')
        
# child class
class Cat(Animal):
    def talk(self):
        print('meow')

snoopy = Dog('snoopy') # instance of Dog class
print(snoopy.name)
snoopy.talk()