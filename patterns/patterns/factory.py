from abc import abstractmethod, ABC


class Pizza(ABC):
    "Simple pizza class"

    @abstractmethod
    def prepare(self):
        pass

    @abstractmethod
    def bake(self):
        pass

    @abstractmethod
    def cut(self):
        pass

    @abstractmethod
    def box(self):
        pass


class CheesePizza(Pizza):
    def prepare(self):
        print("preparing cheese pizza")

    def bake(self):
        print("baking cheese pizza")

    def cut(self):
        print("cutting cheese pizza")

    def box(self):
        print("boxing cheese pizza")


class GreekPizza(Pizza):
    def prepare(self):
        print("preparing greek pizza")

    def bake(self):
        print("baking greek pizza")

    def cut(self):
        print("cutting greek pizza")

    def box(self):
        print("boxing greek pizza")


class PizzaFactory:
    "Class used to exclusively deal with the object creation process"

    def create(self, pizza_type: str) -> Pizza:
        if pizza_type == 'Greek':
            return GreekPizza()
        elif pizza_type == 'Cheese':
            return CheesePizza()
        else:
            print("No matching pizza found..")

class PizzaStore(PizzaFactory):
    def __init__(self, factory: PizzaFactory):
        self.factory = factory

    def order_pizza(self, pizza_type: str):
        pizza = self.factory.create(pizza_type)
        pizza.prepare()
        pizza.bake()
        pizza.cut()
        pizza.box()

store = PizzaStore(PizzaFactory())
store.order_pizza('Greek')
