class Plant:
    """ A plant that grows and ages over time """
    def __init__(self, name: str, height: int, age: int) -> None:
        """ Initializing plant attributes """
        self.name: str = name
        self.height: int = height
        self.age: int = age


class Flower(Plant):
    """ A flower(plant) that has different colours and blooms """
    def __init__(self, name: str, height: int, age: int, color: str):
        """ Initializing flower atributes """
        super().__init__(name, height, age)
        self.color = color
        print(f'{self.name} (Flower): {self.height}cm, {self.age} days, '
              f'{self.color} color')
        self.bloom()

    def bloom(self) -> None:
        """ Allowing flower to bloom """
        print(f'{self.name} is blooming beautifully!')


class Tree(Plant):
    """ A tree(plant) that has a trunk and produces shade"""
    def __init__(self, name: str, height: int, age: int,
                 trunk_diameter: int) -> None:
        """ Initializing tree attributes """
        super().__init__(name, height, age)
        self.trunk_diameter = trunk_diameter
        print(f'{self.name} (Tree): {self.height}cm, {self.age} days, '
              f'{self.trunk_diameter}cm diameter')
        self.produce_shade()

    def produce_shade(self) -> None:
        """ Calculating shade area for tree """
        shade_area = (self.height * self.trunk_diameter * 3.14) / 1000
        print(f'{self.name} provides {shade_area:.0f} square meters of shade')


class Vegetable(Plant):
    """ A vegetable(plant) that can be harvested and has
        a nutritional value """
    def __init__(self, name: str, height: int, age: int,
                 harvest_season: str, nutritional_value: str) -> None:
        """ Initializing vegetable attributes """
        super().__init__(name, height, age)
        self.harvest_season = harvest_season
        self.nutritional_value = nutritional_value
        print(f'{self.name} (Vegetable): {self.height}cm, {self.age} days, '
              f'{self.harvest_season} harvest')
        self.nutri_value()

    def nutri_value(self) -> None:
        """ Nutritional value of vegetable """
        print(f'{self.name} is rich in {self.nutritional_value}')


def plants() -> None:
    """ Defining plants and plants' subclasses """
    Flower("Rose", 25, 30, "red")
    print()
    Flower("Daisy", 57, 45, "white")
    print()
    Tree("Oak", 500, 1825, 50)
    print()
    Tree("Magnolia", 250, 400, 67)
    print()
    Vegetable("Tomato", 80, 90, "summer", "vitamin C")
    print()
    Vegetable("Cauliflower", 150, 200, "winter", "iron")


if __name__ == "__main__":
    print("=== Garden Plant Types ===")
    print()
    plants()
