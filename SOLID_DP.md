
1. Singleton Pattern: InventoryManager
SOLID Principles:

Single Responsibility Principle (SRP): The Inventory Manager class is dedicated solely to managing the pizza and topping inventory. This specialization makes it simpler to understand and modify when necessary.


Dependency Inversion Principle (DIP)

By utilizing an interface for inventory management, the Inventory Manager separates the rest of the system from the specific methods of inventory handling.

Why Use Singleton? 
The Singleton pattern guarantees that there is only one instance of InventoryManager throughout the system. This centralization of inventory management helps prevent discrepancies and simplifies the process of updating inventory.

What Are the Benefits?
Extensibility: If you wish to introduce additional inventory features (such as automatic reordering), you can implement those changes in one location without impacting the rest of the system.
Maintainability: Having a single source of truth for inventory data streamlines tracking stock and making necessary adjustments.

2. Factory Pattern: PizzaFactory
SOLID Principles:

Open/Closed Principle (OCP): 
The Pizza Factory allows for the easy addition of new pizza types without modifying existing code. Simply extend the factory, and the system will be ready to produce new pizzas.
Liskov Substitution Principle (LSP): Whether you’re making a MargheritaPizza or a PepperoniPizza, the creation process remains consistent, allowing for seamless substitution of any pizza type without issues.
Why Use Factory? The Factory pattern removes the need for complicated if-else statements when creating pizzas. The factory takes care of all the creation logic, freeing the rest of the system from those details.

What Are the Benefits?

Extensibility: Introducing new pizzas is straightforward. Just update the factory, and everything else stays the same.
Maintainability: Centralizing pizza creation in one location simplifies management, especially when it comes to implementing changes or fixing bugs.

3. Decorator Pattern: Topping Decorators
SOLID Principles:

Open/Closed Principle (OCP): You can easily add new toppings (like cheese, olives, etc.) without altering existing code.
