__author__ = 'Ryan'
from level_model import LevelModel

class Bathroom(LevelModel):

    def __init__(self):
        self._connections = []
        self._description = """
                You walk into the bathroom and... A DEMON STARES YOU IN THE FACE. You faint and die from fear. The end.
                """
        self._name = 'bathroom'

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

    def describe_level_string(self):
        string = self.description
        string = string + " In the dank bathroom you see a few connections: "
        for connection in self.connections:
            string = string + connection.name + " "
        return string

    def has_connection(self, connection):
        return connection in self.connections