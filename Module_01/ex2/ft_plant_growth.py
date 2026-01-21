class Plant:
    """ Plant that grows overtime """
    def __init__(self, name, height, days) -> None:
        """ Initialize plant variables """
        self.name = name
        self.height = height
        self.days = days

    def grow(self) -> None:
        """ Increase plant height by 1 """
        self.height += 1

    def age(self) -> None:
        """ Increase plant age by 1 """
        self.days += 1

    def get_info(self) -> None:
        """ Print plant status information"""
        print(f'{self.name}: {self.height}cm, {self.days} days old')


if __name__ == "__main__":
    rose = Plant("Rose", 25, 30)
    initial_height = rose.height

    print("=== Day 1 ===")
    rose.get_info()

    for i in range(6):
        rose.grow()
        rose.age()

    print("=== Day 7 ===")
    rose.get_info()

    growth = rose.height - initial_height

    print(f'Growth this week: +{growth}cm')
