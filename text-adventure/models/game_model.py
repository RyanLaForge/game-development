__author__ = 'Ryan'
from LevelModel.bedroom import Bedroom
from LevelModel.bedroom_hallway import BedroomHallway
from LevelModel.bathroom import Bathroom

class GameModel(object):

    bedroom = Bedroom()
    bedroom_hallway = BedroomHallway()
    bathroom = Bathroom()

    bedroom.connections = [bedroom_hallway]
    bedroom_hallway.connections = [bedroom, bathroom]
    bathroom.connections = [bedroom_hallway]

    levels = {bedroom, bedroom_hallway, bathroom}

    current_level = bedroom

    def has_connection(self, connection_name):
        if self.current_level.has_connection(self.get_level_by_name(connection_name)):
            return True
        else: return False

    def move_to_level(self, connection_name):
        if self.has_connection(connection_name):
            connection = self.get_level_by_name(connection_name)
            self.current_level = connection
        else:
            raise ValueError("The current level %s is not connected to level %s" % (self.current_level.name, connection_name))

    def get_current_level(self):
        return self.current_level

    def get_current_level_name(self):
        return self.get_current_level().name

    def get_level_by_name(self, name):
        for level in self.levels:
            if level.name == name:
                return level