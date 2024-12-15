from abc import ABC, abstractmethod



class Pizza(ABC):
    @abstractmethod
    def Description(self):
        pass

    @abstractmethod
    def Cost(self):
        pass

class TopDecorator(Pizza):
    def __init__(self, pizza: Pizza):
        self._pizza = pizza

    def Description(self):
        return self._pizza.Description()

    def Cost(self):
        return self._pizza.Cost()

class CheeseDecorator(TopDecorator):
    def Description(self):
        return self._pizza.Description() + " + Cheese"

    def Cost(self):
        return self._pizza.Cost() + 1.0

class OlivesDecorator(TopDecorator):
    def Description(self):
        return self._pizza.Description() + " + Olives"

    def Cost(self):
        return self._pizza.Cost() + 0.5

class MushroomsDecorator(TopDecorator):
    def Description(self):
        return self._pizza.Description() + " + Mushrooms"

    def Cost(self):
        return self._pizza.Cost() + 0.7
