# -*- coding: utf-8 -*-

class Animal():
    def __init__(self, name, tricks):
        self.name = name
        self.tricks = tricks

    def learn(self, trick_name):
        self.tricks.append(trick_name)
        
class Dog(Animal):
    pass

class Cat(Animal):
    pass

snoopy = Dog('snoopy', [])
print(snoopy.name)
print(snoopy.tricks)
snoopy.learn('sit')
print(snoopy.tricks)