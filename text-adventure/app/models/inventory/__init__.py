__author__ = 'Ryan'
from app.models.item_models.cellphone import Cellphone
from app.models.item_models.wallet import Wallet

#after the first time a module is imported, python does not re-execute the code.


def insert_starting_items():
    cellphone = Cellphone()
    wallet = Wallet()
    inventory_items[cellphone.name] = cellphone
    inventory_items[wallet.name] = wallet
    
inventory_items = {}
insert_starting_items()

