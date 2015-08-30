from base_item import Item

class Cellphone(Item):
    def __init__(self):
        self._name = 'cellphone'
        self._description = 'A cellphone. The screen is black and the battery is dead.'
        self._usable = (lambda self: self.action != None)
        self._carryable = True
        self.action = None
