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
        self.parse_user_input(clean_input)


    def clean_user_input(self, input):
        """Cleans the user input to make it easier to parse
        :return: The cleaned input."""
        input = input.lower()
        input = input.strip()
        return input

    def parse_user_input(self, input):
        """Parse the user input and initiate the command according to the help menu.
        :precon: The input should be cleaned. (lowercase and whitespaces stripped"""
        if 'help' in input:
            self.handle_user_help_options(input)
        elif input.startswith('go'):
            self.handle_go_command(input)
        elif input.startswith('inventory'):
            self.handle_inventory_command(input)
        elif input == 'quit' or input == 'q':
            self.exit_application()
        else:
            self.display_user_error("Did not understand that command. You entered: %s" % input)

    def handle_inventory_command(self, input):
        input = input[10:]
        if input.startswith('-examine'):
            self.examine_item(input[8:])
        elif input.startswith('-use'):
            self.use_item(input[4:])
        elif input.startswith('-list'):
            self.display_inventory_list()
        else:
            self.display_user_error("Invalid inventory command. you entered: %s" % ("inventory %s" % input))
            self.display_inventory_help()

    def handle_go_command(self, input):
        input = input[3:]
        if len(input) == 0:
            self.display_user_error("Invalid go command. You entered: %s" % ("go %s" % input))
            self.display_go_command_help()
        else:
            self.travel_to_level(input)

    def handle_user_help_options(self, input):
        if 'inventory' in input:
            if 'examine' in input:
                self.display_inventory_examine_help()
            elif 'use' in input:
                self.display_inventory_use_help()
            else:
                self.display_inventory_help()
        else:
            if len(input[4:]) != 0:
                self.display_invalid_help_command(input)
            self.display_help_instructions()
        if 'go' in input:
            self.display_go_command_help()

    def display_invalid_help_command(self, input):
        """Explain that the help command was invalid """
        print "You gave an invalid help command. The command you typed was: %s" % input
    def display_go_command_help(self):
        """Explain the go command"""
        print "The \'go\' command moves you to another location. use \'go {{room}}\' to move to a different room."

    def display_inventory_use_help(self):
        """Explain inventory use command"""
        print "Use this command to use an item in your inventory \'inventory -use {{item}}\'"

    def display_inventory_examine_help(self):
        """Explain inventory help"""
        print "The examine command examines the given item. To properly use it type \'inventory -examine {{item}}\'"

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
        item_name = item_name.strip()
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
