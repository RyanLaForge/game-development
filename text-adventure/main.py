__author__ = 'Ryan'
from app.models.game_models.game_model import GameModel
from app.views.view import GameView

class TextAdventure():
    current_model = GameModel()
    current_view = GameView(game_model=current_model)
    while True:
        current_view.collect_user_input()

TextAdventure()