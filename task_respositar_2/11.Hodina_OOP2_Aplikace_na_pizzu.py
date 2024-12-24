def base_pizza():
    return "Těsto na pizzu"


def add_ingredient(ingredient):
    def decorator(pizza_function):
        def wrapper():
            return f"{pizza_function()} s {ingredient}"
        return wrapper
    return decorator


@add_ingredient("rajským protlakem")
@add_ingredient("mozzarellou")
@add_ingredient("bazalkou")
def margarita():
    return base_pizza()

@add_ingredient("smetanovým základem")
@add_ingredient("mozzarellou")
@add_ingredient("gorgonzolou")
@add_ingredient("parmazánem")
@add_ingredient("ementálem")
def quattro_formaggi():
    return base_pizza()


@add_ingredient("rajským protlakem")
@add_ingredient("mozzarellou")
@add_ingredient("šunkou")
@add_ingredient("houbami")
@add_ingredient("olivami")
def capricciosa():
    return base_pizza()


@add_ingredient("rajským protlakem")
@add_ingredient("mozzarellou")
@add_ingredient("šunkou")
@add_ingredient("ananasem")
def hawai():
    return base_pizza()

print()
print("Pizzy vyberte si a zadejte ID:")
print()
print("1 = Margarita")
print("2 = Quattro Formaggi")
print("3 = Capricciosa")
print("4 = Hawai")
print()
num1 = int(input("Zadejte ID Pizzy: "))

if num1 == 1:
    print("\nPříprava pizzy Margarita:")
    print(margarita())

elif num1 == 2:
    print("\nPříprava pizzy Quattro Formaggi:")
    print(quattro_formaggi())

elif num1 == 3:
    print("\nPříprava pizzy Capricciosa:")
    print(capricciosa())

elif num1 == 4:
    print("\nPříprava pizzy Hawai:")
    print(hawai())

else:
    print("\nNeplatný výběr!")
