class Coffee:
    def cost(self):
        return 5

    def description(self):
        return 'Simple coffee'

class CoffeeDecorator:
    def __init__(self, coffee):
        self._coffee = coffee

    def cost(self):
        return self._coffee.cost()

    def description(self):
        return self._coffee.description()


class SugarDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 1

    def description(self):
        return self._coffee.description() + " + sugar"


class MilkDecorator(CoffeeDecorator):
    def cost(self):
        return self._coffee.cost() + 2

    def description(self):
        return self._coffee.description() + ' + milk'


coffee = Coffee()
print(coffee.description(), "-", coffee.cost(), "sums")

coffee_with_milk = MilkDecorator(coffee)
print(coffee_with_milk.description(), "-", coffee_with_milk.cost(), "sums")

coffee_with_milk_sugar = SugarDecorator(coffee_with_milk)
print(coffee_with_milk_sugar.description(), "-", coffee_with_milk_sugar.cost(), "sums")