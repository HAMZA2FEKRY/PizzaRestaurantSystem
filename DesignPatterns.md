# Design Patterns in the Pizza Restaurant Ordering System

This document explains the design patterns used in the pizza restaurant ordering system and provides an understanding of how they improve the system's architecture. It also explores the concept of overengineering, where design patterns might be applied unnecessarily in simple systems.

1. Singleton Pattern (InventoryManager)

Pattern Description
The Singleton  pattern ensures that a class has only one instance and provides a global point of access to it. In the pizza restaurant system, the `InventoryManager` class manages the stock of pizzas and toppings, and we ensure that only one instance of it exists throughout the application.

Why Singleton?
Centralized Control
It ensures that all parts of the system interact with a single inventory instance, preventing data inconsistency.
Resource Management Since managing inventory is a system-wide concern, having a single instance prevents the unnecessary creation of multiple inventory managers.

Code Example
```python
class InventoryManager:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if not hasattr(self, 'initialized'):
            self._inventory = {
                "Margherita": 10,
                "Pepperoni": 10,
                "Cheese": 15,
                "Olives": 10,
                "Mushrooms": 12,
            }
            self.initialized = True

    def check_and_decrement(self, item: str) -> bool:
        if self._inventory.get(item, 0) > 0:
            self._inventory[item] -= 1
            return True
        return False

    def get_inventory(self):
        return self._inventory

