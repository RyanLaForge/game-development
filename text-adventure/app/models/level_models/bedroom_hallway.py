__author__ = 'Ryan'
from level_model import LevelModel

class BedroomHallway(LevelModel):
    def __init__(self):
        self._connections = []
        self._description = """As you step out into the hallway, the floorboards creak beneath your feet. The hallway is silent except for the
sound of your breath, but you can hear a tap dripping faintly in a room to the right of you. Every room except that one is boarded up. The hallway is covered with faded paintings
of a boy and girl playing. You look at one closely. The boy is pushing the girl, who is on a swing. The girl's face is one of pure joy, and the boy
has an innocent smile on his face.

\'HAHAHAHA BET YOU CAN\'T CATCH ME!\' you hear a little girl yell from downstairs. Goosebumps cover the back of your neck and arms, you
thought you were alone. The sound came from the left side of you, from down the stairs. You begin to wonder if there are more people in the house.
Perhaps you should try and find the little girl to find out.
                """
        self._name = 'bedroom_hallway'
        self.visited = 0

    def describe_level_string(self):
        string = self.description
        string = string.strip() + " In the long, dark, bedroom_hallway you manage to make out a few connections: "
        for connection in self.connections:
            string = string + connection.name + " "
        return string

