# -*- coding: utf-8 -*-

import unittest
from machine import Machine, Rack, Coin

class MachineTest(unittest.TestCase):
    def test_can_refill_biscuits(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks)
        machine.refill("A", 3)
        self.assertEqual(machine.racks["A"].quantity, 3)

    def test_user_can_buy_item_a(self):
        racks = [ Rack("A", "", 100) ]
        machine = Machine(racks, 0)
        machine.refill("A", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("A")
        self.assertTrue(outcome)
        self.assertEqual(machine.racks["A"].quantity, 0)
        self.assertEqual(machine.amount, 0)
        self.assertEqual(machine.coins[Coin.DOLLAR], 1)

    def test_user_get_its_change_back(self):
        racks = [ Rack("C", "", 85) ]
        machine = Machine(racks, 10) # Ten coins each
        machine.refill("C", 1)
        machine.insert(Coin.DOLLAR)
        outcome = machine.press("C")
        self.assertTrue(outcome)
        self.assertEqual(machine.coins[Coin.DIME], 9)
        self.assertEqual(machine.coins[Coin.NICKEL], 9)