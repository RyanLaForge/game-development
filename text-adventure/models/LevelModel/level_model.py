__author__ = 'Ryan'
from abc import ABCMeta, abstractproperty, abstractmethod

class LevelModel(object):
    __metaclass__ = ABCMeta

    @abstractproperty
    def connections(self):
        raise NotImplementedError("The subclass of the level model did not implement the property: %s"
                                  % self.connections.__name__)

    @connections.setter
    def connections(self, value):
        raise NotImplementedError("The subclass of the level model did not implement the get property: %s"
                                  % self.connections.__name__)

    @abstractproperty
    def name(self):
        raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.name.__name__)

    @name.setter
    def name(self):
        raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.name.__name__)

    @abstractproperty
    def description(self):
         raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.description.__name__)

    @description.setter
    def description(self):
         raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.description.__name__)

    @abstractmethod
    def describe_level_string(self):
        raise  NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.describe_level_string.__name__)

    @abstractmethod
    def has_connection(self,connection):
        NotImplementedError("The subclass of the level model did not implement the set property: %s"
                                  % self.has_connection.__name__)


