__author__ = 'Ryan'
from level_model import LevelModel

class Bedroom(LevelModel):
    def __init__(self):
        self._connections = []
        self._description = """
        You look around. It's a perfectly ordinary bedroom, except for the erie paintings stairing at you. The air smells
         of must. Close by, you can hear a tap dripping. You look out into the hallway to see nothing but darkness. You feel uneasy, but
         are sure you should go into the hallway.
    """
        self._name = 'bedroom'

    @property
    def connections(self):
        return self._connections

    @connections.setter
    def connections(self, value):
        if not isinstance(value, list):
            value = [value]
        else:
            self._connections = value

    @property
    def description(self):
        return self._description

    @property
    def name(self):
        return self._name

    def describe_level_string(self):
        string = self.description
        string = string + "you see that the bedroom is connected to:"
        for connection in self.connections:
            string = string + connection.name + " "

        return string

    def has_connection(self, connection):
        return connection in self.connections
