__author__ = 'Ryan'
from base_item import Item

class Wallet(Item):
    def __init__(self):
        self._name = 'wallet'
        self._description = 'my dirty old wallet'
        self.carryable = True
        self.action = None
