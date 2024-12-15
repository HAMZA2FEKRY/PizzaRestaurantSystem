from abc import ABC, abstractmethod


class Pizza(ABC):
    @abstractmethod
    def Description(self):
        pass

    @abstractmethod
    def Cost(self):
        pass

class MargheritaPizza(Pizza):
    def Description(self):
        return "Margherita Pizza"

    def Cost(self):
        return 5.0

class PepperoniPizza(Pizza):
    def Description(self):
        return "Pepperoni Pizza"

    def Cost(self):
        return 6.0

class PizzaFactory:
    def create_pizza(self, pizza_type: str) -> Pizza:
        if pizza_type == "Margherita":
            return MargheritaPizza()
        elif pizza_type == "Pepperoni":
            return PepperoniPizza()
        else:
            raise ValueError("Unknown pizza type")
