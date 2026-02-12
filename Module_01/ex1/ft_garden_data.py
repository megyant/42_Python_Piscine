class Plant:
    """ Create a class for plant """
    def __init__(self, name: str, height: int, age: int):
        """ Initialize a new Plant instance """
        self.name = name
        self.height = height
        self.age = age


def garden_data(plant_list: list[Plant]) -> None:
    """ Prints details of plants """

    print("=== Garden Plant Registry ===")

    for plant in plant_list:
        print(f'{plant.name}: {plant.height}cm, {plant.age} days old')


if __name__ == "__main__":
    plants = [
                Plant("Rose", 25, 30),
                Plant("Sunflower", 80, 45),
                Plant("Cactus", 15, 120)
             ]
    garden_data(plants)
