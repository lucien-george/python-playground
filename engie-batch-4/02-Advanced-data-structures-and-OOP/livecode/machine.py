# -*- coding: utf-8 -*-
from enum import Enum

class Coin(Enum): # inheritance from Enum class
    DOLLAR = 100
    QUARTER = 25
    DIME = 10
    NICKEL = 5
    
class Rack:
    pass

class Machine:
    pass

## TESTING MY CODE
## Creating a list of racks with only one rack inside
#racks = [ Rack("A", "Chocolate Biscuits", 100) ]
#
## creating an instance of machine
#machine = Machine(racks)
#
## calling refill function
#machine.refill("A", 3)
#
## Inserting coins
#machine.insert(Coin.DOLLAR)
#
## Buying an item
#outcome = machine.press("A")