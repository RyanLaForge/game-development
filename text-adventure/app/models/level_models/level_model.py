__author__ = 'Ryan'
from abc import ABCMeta, abstractproperty, abstractmethod

class LevelModel(object):
    __metaclass__ = ABCMeta

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        if value is None:
            value = []
        elif not isinstance(value, list):
            value = [value]
        self._connections = value


    @property
    def name(self):
        return self._name

    @property
    def description(self):
        return self._description

    def has_connection(self, connection):
        return connection in self.connections

    @description.setter
    def description(self, description):
        self._description = description

    @abstractmethod
    def describe_level_string(self):
        raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.describe_level_string.__name__)



