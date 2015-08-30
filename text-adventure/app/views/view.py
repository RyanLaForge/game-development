__author__ = 'Ryan'

from app.models.game_models.game_model import GameModel
from app.models.inventory import inventory_items

class GameView():
    def __init__(self, game_model):
        self.help_instructions = """
            Here are the commands that you can perform.
            go {{levelname}}} -- Go to the level with levelName if that level is listed in the list of instructions.
            inventory {{command}} {{item}} -- Execute the command on the inventory item. For more information, type help -inventory
            quit              -- Quit the game.
            """
        self.inventory_help_text = """
        Inventory help menu:\n
        type inventory -list to list all of the items in your inventory.
        command structure: inventory {{command}} {{itemname}}
        command types:\n
        --examine - examine the item.
        --use - use the item, if it is useable.
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
        elif input.startswith('help'):
            if input[4:].strip() == '-inventory':
                self.display_inventory_help()
        elif input.startswith('go '):
            self.travel_to_level(input[3:])
        elif input.startswith('inventory'):
            input = input[10:]
            if input.startswith('examine'):
                self.examine_item(input[8:])
            elif input.startswith('use'):
                self.use_item(input[4:])
            elif input.startswith('list'):
                self.display_inventory_list()
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

    def display_inventory_help(self):
        print self.inventory_help_text

    def examine_item(self, item_name):
        item = inventory_items.get(item_name)
        if not item:
            self.display_user_error('There is no such item %s in the inventory.' % item_name)
        else:
            print item.description

    def use_item(self, item_name):
        item = inventory_items.get(item_name)
        if not item:
            self.display_user_error('There is no such item %s in the inventory.' % item_name)
        elif not item.usable:
            self.display_user_error("That item is not usable.")
        else:
            item.use()

    def display_inventory_list(self):
        print "Current items in your inventory:"
        for item in inventory_items.keys():
            print item