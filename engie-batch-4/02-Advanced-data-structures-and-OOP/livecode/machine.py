# -*- coding: utf-8 -*-
from enum import Enum

# Coin class
class Coin(Enum): # inherits from Enum class
    # basically creates a class with constants.
    # Each constant has a value
    # we can iterate over the class
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5

# Rack class  
## takes three parameters: code (str), name (str), price (int), quantity(int) initialized to 0
class Rack:
    def __init__(self, code, name, price):
        self.code = code
        self.name = name
        self.price = price
        self.quantity = 0
    
# Machine class
## DATA
### take two parameters: racks (list), coin_count (int) => default value, amount(int) initialized to 0
    
## BEHAVIOR
### refill(code, quantity)
### => increase the rack quantity by `quantity`
### insert(coin)
### => to increase the amount in our machine
### => increase the coin count of the appropriate coin
### press(code)
### => check if the code refers to an exisiting rack
### => check if quantity of rack is > 0
### => check if the amount > price of the rack
### => reduce the stock by 1
### => decrease the amount in my machine
### => change to give back to the user

class Machine:
    def __init__(self, racks, coin_count = 10):
        self.amount = 0 # amount is 0 initially
#        self.racks = dict((rack.code, rack) for rack in racks)
        self.racks = {} # creating empty dict to fill with racks
        for rack in racks:
            # keys will be the code of the racks and value will be the rack object
            self.racks[rack.code] = rack
#        self.coins = dict((coin, coin_count) for coin in Coin)
        self.coins = {} # creating empty dict to fill with coins
        for coin in Coin:
            # keys will be coin itself and value will be the number of coin in the machine
            self.coins[coin] = coin_count
    
    def refill(self, code, quantity):
        # increase the quantity of appropriate 
        self.racks[code].quantity += quantity
    
    def insert(self, coin):
        # increase the quantity of the correct coin type by 1
        self.coins[coin] += 1
        # increasing my wallet by the value of the coin I insert
        self.amount += coin.value
    
    def press(self, code):
        # checking if rack exists and amount > rack price and quantity of rack > 0
        if code in self.racks and self.racks[code].quantity > 0 \
        and self.amount >= self.racks[code].price:
            # decreasing the quantity of my rack by one
            self.racks[code].quantity -= 1
            # decreasing the wallet by the price of the rack
            self.amount -= self.racks[code].price
            # calling the function give_change to give back the correct change to the user
            self.give_change(self.amount)
            return True
        else:
            return False
        
    def give_change(self, amount):
        if amount == 0:
            # if there is no change to give back then give back nothing
            return 0
        else:
            # iterating over all the types of coins
            for coin in Coin:
                # calculating the number of coins to give back
                # will be the minimum of either the number of coins that I have in the machine
                # or the actual number of coin I have to give back
                coins_to_give_back = min(self.coins[coin], amount // coin.value)
                # remove the quantity of the correct coin type
                self.coins[coin] -= coins_to_give_back
                # reduce the amount we gave back to the user from the initial change
                amount = amount -  coins_to_give_back * coin.value
                

# TESTING MY CODE
# Creating a list of racks with only one rack inside
racks = [ Rack("A", "Chocolate Biscuits", 100) ]

# creating an instance of machine
machine = Machine(racks)
print(machine.racks)
print(machine.coins)
# calling refill function
machine.refill("A", 3)

# Inserting coins
machine.insert(Coin.DOLLAR)

# Buying an item
outcome = machine.press("A")

# iterating over the class coin that inherits from Enum
for coin in Coin:
    print(coin) # accessing the coin itself
    print(coin.name) # accessing the name of the coin
    print(coin.value) # accessing the value of the coin