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
        self.visited = 0

    def describe_level_string(self):
        if self.visited <= 1:
            return self.first_description_string()
        else:
            return self.description_string()

    def first_description_string(self):
        string = """Your lungs gasp for breath as you awaken from what must have been a nightmare. You sit up and wipe
        the sweat off your brow and look around. In horror, you realize that you don't recognize the room at all.
        You rest your face in your hands as you try to remember what happened and how you got here. Your memory is faded,
        so much so that you can't even seem to remember your own name.
        You reach down into your pockets and pull out your cell phone. The screen is completely black, and the phone is
        dead. You reach for your wallet, desperate to remember who you are. You open the wallet, but it's completely
        empty, except for a small smily face.\n"""
        string = string + self.description
        string = string + "you see that the bedroom is connected to: "
        for connection in self.connections:
            string = string + connection.name + " "

        return string

    def description_string(self):
        string = self.description
        string = string + "you see that the bedroom is connected to: "
        for connection in self.connections:
            string = string + connection.name + " "

        return string