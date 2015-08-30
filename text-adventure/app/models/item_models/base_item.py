__author__ = 'Ryan'
import abc

class Item():
    __metaclass__ = abc.ABCMeta

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, new_name):
        self._name = new_name

    @property
    def description(self):
        return self._description

    @description.setter
    def description(self, new_description):
        self._description = new_description


    def can_be_picked_up(self):
        return self.carryable

    def use(self, *args, **kwargs):
        if not self.usable:
            raise ValueError("This item is not useable.")
        self.action()

    @property
    def usable(self):
        return self.action != None