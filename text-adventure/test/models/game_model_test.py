__author__ = 'Ryan'
import unittest

import mock

from app.models.game_models.game_model import GameModel


class GameModelTests(unittest.TestCase):

    def setUp(self):
        self.model = GameModel()

    @mock.patch('models.game_model.Bedroom.has_connection', mock.MagicMock(return_value=True))
    def test_has_connection_returns_true_if_level_connected_to_current_level(self):
        self.assertTrue(self.model.has_connection('fake_level'))

    @mock.patch('models.game_model.Bedroom.has_connection', mock.MagicMock(return_value=False))
    def test_has_connection_returns_true_if_current_level_not_connected(self):
        self.assertFalse(self.model.has_connection('fake_level'))

    @mock.patch('models.game_model.GameModel.has_connection', mock.MagicMock(return_value=False))
    def test_move_to_level_raises_value_error_if_not_connected_to_current_level(self):
        with self.assertRaises(ValueError):
            self.model.move_to_level('fake')

    @mock.patch('models.game_model.GameModel.has_connection', mock.MagicMock(return_value=True))
    @mock.patch('models.game_model.GameModel.get_level_by_name', mock.MagicMock(return_value='fake_level'))
    def test_move_to_level_sets_current_level_if_has_connected_is_true(self):
        self.model.current_level = 'not-set'
        self.model.move_to_level('fake')
        self.assertEqual('fake_level', self.model.current_level)

    def test_get_current_level_returns_current_level(self):
        self.model.current_level = 'current level^^'
        self.assertEqual('current level^^', self.model.current_level)

    def test_get_current_level_name(self):
        level = mock.MagicMock
        level.name = 'name'
        self.model.current_level = level
        self.assertEqual('name', self.model.current_level.name)

    def test_get_level_by_name_returns_correct_level(self):
        levels = []
        for i in xrange(0,5):
            level = mock.MagicMock()
            level.name = 'level%s' % i
            levels.append(level)

        self.model.levels = levels
        expected_level = levels[2]
        actual_level = self.model.get_level_by_name('level2')
        self.assertEqual(expected_level, actual_level)