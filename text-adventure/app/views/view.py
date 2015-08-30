__author__ = 'Ryan'

from app.models.game_models.game_model import GameModel

class GameView():
    def __init__(self, game_model):
        self.help_instructions = """
            Here are the commands that you can perform.
            go {{levelname}}} -- Go to the level with levelName if that level is listed in the list of instructions.
            quit              -- Quit the game.
            """

        self.game_model = game_model
        self.display_welcome()

    def collect_user_input(self):
        """Collects the user input, cleans it, and parses the command to understand it."""
        input = raw_input("Input your command here: ")
        clean_input = self.clean_user_input(input)
        self.parse_user_input(input)


    def clean_user_input(self, input):
        """Cleans the user input to make it easier to parse
        :return: The cleaned input."""
        input = input.lower()
        input = input.strip()
        return input

    def parse_user_input(self, input):
        """Parse the user input and initiate the command according to the help menu.
        :precon: The input should be cleaned. (lowercase and whitespaces stripped"""
        if input == 'help' or input == 'h':
            self.display_help_instructions()
        elif input.startswith('go '):
            self.travel_to_level(input[3:])
        elif input == 'quit' or input == 'q':
            self.exit_application()
        else:
            self.display_user_error("Did not understand that command.")

    def display_help_instructions(self):
        """Display the help instructions to the user"""
        print self.help_instructions

    def travel_to_level(self, level):
        """Set the given level."""
        try:
            self.game_model.move_to_level(level)
            self.describe_level(level)
        except ValueError as e:
            print "Failed to travel to that room. %s" % e

    def describe_level(self, level):
        """Describe the current level"""
        print self.game_model.get_current_level().describe_level_string()

    def exit_application(self):
        print "Goodbye"
        exit()

    def display_user_error(self, error):
        print error
        self.display_help_instructions()

    def display_welcome(self):
        print "Welcome to text-adventure! type help for a list of instructions."
        print self.game_model.get_current_level().describe_level_string()

