

class Car:

    def __init__(self, model: str, year: int, manufacturer: str, engine_volume: float, color: str, price: float):
        self.__model = model
        self.__year = year
        self.__manufacturer = manufacturer
        self.__engine_volume = engine_volume
        self.__color = color
        self.__price = price


    def display_info(self):

        print(f"Model: {self.__model}")
        print(f"Rok vydání: {self.__year}")
        print(f"Výrobce: {self.__manufacturer}")
        print(f"Objem motoru: {self.__engine_volume} L")
        print(f"Barva: {self.__color}")
        print(f"Cena: {self.__price} Kč")


    def get_model(self):
        return self.__model

    def set_model(self, model: str):
        self.__model = model


    def get_year(self):
        return self.__year

    def set_year(self, year: int):
        self.__year = year


    def get_manufacturer(self):
        return self.__manufacturer

    def set_manufacturer(self, manufacturer: str):
        self.__manufacturer = manufacturer


    def get_engine_volume(self):
        return self.__engine_volume

    def set_engine_volume(self, engine_volume: float):
        self.__engine_volume = engine_volume


    def get_color(self):
        return self.__color

    def set_color(self, color: str):
        self.__color = color


    def get_price(self):
        return self.__price

    def set_price(self, price: float):
        self.__price = price

car1 = Car(model="Octavia", year=2020, manufacturer="Škoda", engine_volume=1.5, color="Bílá", price=500000)


print("Informace o voze:")
car1.display_info()


car1.set_color("Červená")
car1.set_price(480000)

print()
print("Aktualizované informace o voze:")
car1.display_info()


print("Model vozu je:", car1.get_model())

