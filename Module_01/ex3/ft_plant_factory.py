class Plant:
    """ Defining a plant """
    count = 0

    def __init__(self, name, height, days) -> None:
        """ Initialize plant variables """
        self.name = name
        self.height = height
        self.days = days
        Plant.count += 1

    def get_info(self) -> None:
        """ Display plant information """
        print(f'Created: {self.name} ({self.height}cm, {self.days} days)')


if __name__ == "__main__":
    plants = [("Rose", 25, 30),
              ("Oak", 200, 365),
              ("Cactus", 5, 90),
              ("Sunflower", 80, 45),
              ("Fern", 15, 120)
              ]
    for name, height, age in plants:
        print_plant = Plant(name, height, age)
        print_plant.get_info()

    print(f'Total plants created: {Plant.count}')
