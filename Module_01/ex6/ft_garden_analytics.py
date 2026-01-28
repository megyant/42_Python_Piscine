class Plant:
    def __init__(self, name, initial_height):
        self.name = name
        self.set_height(initial_height)

    def set_height(self, new_height) -> int:
        if (new_height < 0):
            self.height = 0
        else:
            self.height = new_height

    def get_height(self):
        return self.height

    def details(self):
        return f"{self.name}: {self.height}cm"

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")

    def get_category(self):
        return "regular"


class FloweringPlant(Plant):
    def __init__(self, name, initial_height, color):
        super().__init__(name, initial_height)
        self.color = color

    def details(self):
        base_details = super().details()
        return f"{base_details}, {self.color} flowers (blooming)"

    def get_category(self):
        return "flowering"


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, color, points):
        super().__init__(name, height, color)
        self.points = points

    def details(self):
        base_details = super().details()
        return (f"{base_details}, Prize points: {self.points}")

    def get_category(self):
        return "prize"


class Garden:
    def __init__(self, owner: str):
        self.owner = owner.title()
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant):
        self.plants.append(plant)
        plant.name = plant.name.title()
        print(f"Added {plant.name} to {self.owner}'s garden")

    def help_grow(self):
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow()
            self.total_growth += 1

    def get_stats(self):
        return len(self.plants), self.total_growth

    def report(self):
        print(f"=== {self.owner}'s Garden Report ===\n")
        print("Plants in garden:")
        for plant in self.plants:
            print(f"- {plant.details()}")


class GardenManager:
    total_gardens = 0

    def add_garden(self, garden):
        self.gardens.append(garden)
        GardenManager.total_gardens += 1

    class GardenStats:
        def calculate_score(self, plants):
            total_score = 0
            total_regular = 0
            total_flowering = 0
            total_prize = 0

            for plant in plants:
                total_score += plant.get_height()

                category = plant.get_category()

                if category == "prize":
                    total_prize += 1
                elif category == "flowering":
                    total_flowering += 1
                else:
                    total_regular += 1

            return total_score, total_regular, total_flowering, total_prize

    def __init__(self):
        self.gardens = []
        self.stats = self.GardenStats()

    @staticmethod
    def height_validation(value):
        if value >= 0:
            return True
        return False

    @classmethod
    def create_system(cls):
        print("=== Garden Manager System Demo ===\n")
        return cls()


if __name__ == "__main__":
    manager = GardenManager.create_system()

    alice_garden = Garden("Alice")
    manager.add_garden(alice_garden)

    p1 = Plant("oak Tree", 100)
    p2 = FloweringPlant("Rose", 25, "red")
    p3 = PrizeFlower("Sunflower", 50, "yellow", 10)
    alice_garden.add_plant(p1)
    alice_garden.add_plant(p2)
    alice_garden.add_plant(p3)

    print()
    alice_garden.help_grow()

    print()
    alice_garden.report()

    plants_count, growth = alice_garden.get_stats()
    a_score, regular, flowering, prize = manager.stats.calculate_score(
        alice_garden.plants)
    print(f"Plants added: {plants_count}, Total growth: {growth}cm")
    print(f"Plant types: {regular} regular, {flowering} flowering, "
          f"{prize} prize flowers\n")

    is_valid = GardenManager.height_validation(p1.get_height())
    print(f"Height validation test: {is_valid}")

    bob_garden = Garden("Bob")
    manager.add_garden(bob_garden)
    b_score, _, _, _ = manager.stats.calculate_score(
        bob_garden.plants)
    print(f"Garden scores - Alice: {a_score}, Bob: {b_score}")
    print(f"Total gardens managed: {GardenManager.total_gardens}")
