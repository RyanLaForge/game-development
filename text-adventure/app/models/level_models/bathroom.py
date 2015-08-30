__author__ = 'Ryan'
from level_model import LevelModel

class Bathroom(LevelModel):

    def __init__(self):
        self._connections = []
        self._description = """
                You walk into the bathroom and... A DEMON STARES YOU IN THE FACE. You faint and die from fear. The end.
                """
        self._name = 'bathroom'
        self.visited = 0

    def describe_level_string(self):
        string = self.description
        string = string + " In the dank bathroom you see a few connections: "
        for connection in self.connections:
            string = string + connection.name + " "
        return string