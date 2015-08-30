__author__ = 'Ryan'
from base_item import Item

class Wallet(Item):
    def __init__(self):
        self._name = 'wallet'
        self._description = 'my dirty old wallet'
        self._usable = (lambda self: self.action != None)
        self._carryable = True
        self.action = None


