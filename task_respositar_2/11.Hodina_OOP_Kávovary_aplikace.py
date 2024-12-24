# Základní třída Device
class Device:
    def __init__(self, brand: str, model: str, power: int):

        self.brand = brand
        self.model = model
        self.power = power

    def show_info(self):

        print(f"Značka: {self.brand}, Model: {self.model}, Výkon: {self.power} W")


class CoffeeMachine(Device):
    def __init__(self, brand: str, model: str, power: int, water_capacity: int):
        super().__init__(brand, model, power)
        self.water_capacity = water_capacity

    def make_coffee(self):

        print(f"{self.brand} {self.model}: Připravuji kávu...")

    def show_info(self):

        super().show_info()
        print(f"Kapacita vody: {self.water_capacity} ml")



class Blender(Device):
    def __init__(self, brand: str, model: str, power: int, speed_levels: int):
        super().__init__(brand, model, power)
        self.speed_levels = speed_levels

    def blend(self):

        print(f"{self.brand} {self.model}: Mixuji...")

    def show_info(self):

        super().show_info()
        print(f"Úrovně rychlosti: {self.speed_levels}")


class MeatGrinder(Device):
    def __init__(self, brand: str, model: str, power: int, grinding_capacity: int):
        super().__init__(brand, model, power)
        self.grinding_capacity = grinding_capacity

    def grind_meat(self):

        print(f"{self.brand} {self.model}: Mletí masa...")

    def show_info(self):

        super().show_info()
        print(f"Kapacita mletí: {self.grinding_capacity} kg/h")

print()
coffee_machine = CoffeeMachine ("Delongi","Super S", 1450 , 2000)
coffee_machine.show_info()
coffee_machine.make_coffee()
print()
blender = Blender("Philips", "HR3652", 1400, 5)
blender.show_info()
blender.blend()
print()
meat_grinder = MeatGrinder("Bosch", "MFW68660", 2200, 3.5)
meat_grinder.show_info()
meat_grinder.grind_meat()