__author__ = 'Ryan'

help_instructions = """
Here are the commands that you can perform.
go {{levelname}}} -- Go to the level with levelName if that level is listed in the list of instructions.
"""
from models.game_model import GameModel

game_model = GameModel()

print game_model.get_current_level().describe_level_string()


def collect_user_input():
    input = raw_input("Input your command here: ")
    input = input.lower()
    print "You chose the command: " + input
    if input.lower() == 'help' or input.lower() == 'h':
        print help_instructions
        collect_user_input()
    elif input.startswith('go'):
        connection = input[2:]
        connection = connection.strip()
        game_model.move_to_level(connection)
        print game_model.get_current_level().describe_level_string()
    else:
        print "did not understand that command. Please try again."
        collect_user_input()

while True:
    collect_user_input()