class Tea:
    def serve(self):
        return "Подан чай"


class Coffee:
    def serve(self):
        return "Подан кофе"

class DrinkFactory:
    def create_drink(self, drink_type):
        if drink_type == "coffee":
            return Coffee()
        elif drink_type == "tea":
            return Tea()
        else:
            raise ValueError("Такого напитка не существует")


factory = DrinkFactory()

drink1 = factory.create_drink("coffee")

print(drink1.serve())

drink2 = factory.create_drink("tea")

print(drink2.serve())

drink3 = factory.create_drink("juice")

print(drink3.serve())