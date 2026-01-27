class Plant:
    def __init__(self, name, height):
        self.name = name
        self.height = height

    def grow(self):
        self.height += 1
        print(f"{self.name} grew 1cm")


class FloweringPlant(Plant):
    def __init__(self, name, height, flower_color):
        super().__init__(name, height)
        self.flower_color = flower_color


class PrizeFlower(FloweringPlant):
    def __init__(self, name, height, flower_color, points):
        super().__init__(name, height, flower_color)
        self.points = points




class GardenManager:
    def __init__(self, garden_owner: str):
        self.garden_owner = garden_owner
        self.plants = []
    
    def add_plant(self, plant):
        self.plants.append(plant)
        print(f"Added {plant.name} to {self.garden_owner}'s garden")

   # class GardenStats():




if __name__ == "__main__":
    print ("=== Garden Manager System Demo ===")