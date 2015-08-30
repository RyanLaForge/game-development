__author__ = 'Ryan'
from level_model import LevelModel

class BedroomHallway(LevelModel):
    def __init__(self):
        self._connections = []
        self._description = """
                You look left and see a stairwell leading downstairs. You look right and see a door at the end of the hallway. The
            dripping sound seems to be coming from there.
                """
        self._name = 'bedroom_hallway'
        self.visited = 0

    def describe_level_string(self):
        string = self.description
        string = string + " In the long, dark, bedroom_hallway you manage to make out a few connections: "
        for connection in self.connections:
            string = string + connection.name + " "
        return string

