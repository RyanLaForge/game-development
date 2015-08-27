__author__ = 'Ryan'
import mock
import unittest

class GameModelTests(unittest.TestCase):
    def setUp(self):
        self.mocked_call = mock.patch('models.LevelModel.LevelModel')

    def test_py(self):
        self.fail(None)