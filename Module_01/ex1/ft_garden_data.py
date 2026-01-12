class Plant:
    """ Create a class for plant with name, heigth and age """
    def __init__(self, name, height, age):
        self.name = name
        self.height = height
        self.age = age


plants = [
    Plant("Rose", 25, 30),
    Plant("Sunflower", 80, 45),
    Plant("Cactus", 15, 120)
    ]

print("=== Garden Plant Registry ===")

for plant in plants:
    print(f'{plant.name}: {plant.height}cm, {plant.age} days old')
