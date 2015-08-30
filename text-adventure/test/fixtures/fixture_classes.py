__author__ = 'Ryan'
from app.models.level_models import LevelModel

class BaseLevelModel(LevelModel):
    def __init__(self):
        self._description = "This is a test class"
        self._connections = []
        self._name = "test level class"

    def describe_level_string(self):
        return "TEST LEVEL DESCRIPTION STRING"
