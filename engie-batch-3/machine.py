# -*- coding: utf-8 -*-
from enum import Enum

class Coin(Enum):
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    
class Rack:
    def __init__(self,code,name,price):
        self.code=code
        self.name=name
        self.price=price
        self.quantity = 0

class Machine:
    def __init__(self,racks, coin_count = 10):
        self.racks = dict((rack.code , rack) for rack in racks)
        self.coins = dict((coin, coin_count) for coin in Coin)
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
            self.amount = self.amount - self.racks[code].price
            self.give_change(self.amount)
            return True
        else:
            return False
            
    def give_change(self, amount):
        if amount==0:
            return 0
        else:
            remaining_amount = amount
            for coin in Coin:
                self.coins[coin] -= remaining_amount//coin.value
                remaining_amount =remaining_amount%coin.value
                
                
    
            
            
            
                
                
racks = [ Rack("A", "Chocolate Biscuits", 100) ]
machine = Machine(racks)
machine.refill("A", 3)
print(machine.coins)
# User can buy item
machine.insert(Coin.DOLLAR)
print(machine.coins)
outcome = machine.press("A")
    
#for coin in Coin:
#    print(coin.value)
