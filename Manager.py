from abc import ABC, abstractmethod

'''
only one instance of the Manager 
exists in the system.
this is helpful to manage  globally and ensure 
that there are no errors between multiple instances.
'''
class Manager: 

    _inventory = { 
        "Margherita": 10,
        "Pepperoni": 10,
        "Cheese": 15,
        "Olives": 10,
        "Mushrooms": 12,

    }

    _instance = None

    def __new__(obj):
        if obj._instance is None:
            obj._instance = super().__new__(obj)
        return obj._instance
    
    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

# factory method


