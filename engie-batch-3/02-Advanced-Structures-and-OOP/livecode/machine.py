# -*- coding: utf-8 -*-
from enum import Enum

class Coin(Enum): # inheritance from Enum class
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    
class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0

class Machine:
    # coin_count has a default value of 10 if no value is passed when creating a new instance of Machine
    def __init__(self, racks, coin_count = 10):
        self.racks = dict((rack.code , rack) for rack in racks) # creating a dictionary
        self.coins = dict((coin, coin_count) for coin in Coin) # creating a dictionary
        self.amount = 0
    
    def refill(self, code, quantity):
        self.racks[code].quantity += quantity
    
    def insert(self, coin):
        self.coins[coin] += 1
        self.amount += coin.value
        
    def press(self, code):
        if code in self.racks and self.racks[code].quantity > 0 \
        and self.amount >= self.racks[code].price :
            self.racks[code].quantity -= 1
            self.amount -= self.racks[code].price
            self.give_change(self.amount)
            return True
        else:
            return False
            
    def give_change(self, amount):
        if amount==0:
            return 0
        else:
            for coin in Coin:
                self.coins[coin] -= amount//coin.value
                amount = amount % coin.value


# TESTING MY CODE
# Creating a list of racks with only one rack inside
racks = [ Rack("A", "Chocolate Biscuits", 100) ]

# creating an instance of machine
machine = Machine(racks)

# calling refill function
machine.refill("A", 3)

# Inserting coins
machine.insert(Coin.DOLLAR)

# Buying an item
outcome = machine.press("A")

# Since the class Coin inherits from Enum then we can iterate over it like so:
for coin in Coin:
    print(coin) # prints the whole coin
    print(coin.value) # prints the value of the coin