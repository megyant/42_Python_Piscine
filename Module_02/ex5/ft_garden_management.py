class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self):
        self.plant_list = {}

    def add_plants(self, plant, water, sun):
        try:
            if not plant:
                raise PlantError("Error adding plant: Plant name "
                                 "cannot be empty!")
            else:
                self.plant_list[plant] = {"water": water, "sun": sun}
                print(f"Added {plant} sucessfully")
        except PlantError as e:
            print(e)

    def water_plants(self):
        try:
            print("\nOpening watering system...")
            if not self.plant_list:
                raise WaterError("The garden is empty!")
            else:
                for plant in self.plant_list:
                    print(f"Watering {plant} - sucess")
        except WaterError as e:
            print(e)
        finally:
            print("Closing watering system (cleanup)")

    def check_plant_health(self):
        try:
            print("\nChecking plant heath...")
            if not self.plant_list:
                raise GardenError("The garden is empty!")
            for plant, stats in self.plant_list.items():
                water_level = stats["water"]
                sun_level = stats["sun"]
                if (0 < water_level < 11) and (1 < sun_level < 13):
                    print(f"{plant}: healthy (water: {water_level}, "
                          f"sun: {sun_level})")
                elif water_level > 10:
                    raise GardenError(f"Error checking {plant}: "
                                      f"Water level {water_level} is too "
                                      "high (max 10)")
                elif sun_level > 12:
                    raise GardenError(f"Error checking {plant}: "
                                      f"Sun level {sun_level} is too "
                                      "high (max 12)")
                elif water_level < 1:
                    raise GardenError(f"Error checking {plant}: "
                                      f"Water level {water_level} is "
                                      "too low (min 1)")
                else:
                    raise GardenError(f"Error checking {plant}: "
                                      f"Sun level {sun_level} is "
                                      "too low (min 2)")
        except GardenError as e:
            print(e)


def test_garden_management():
    print("=== Garden Management System ===")

    plant_list = GardenManager()

    print("\nAdding plants to garden...")
    plant_list.add_plants("tomato", 5, 8)
    plant_list.add_plants("lettuce", 15, 10)
    plant_list.add_plants(None, None, None)

    print("\nWatering plants...")
    plant_list.water_plants()

    plant_list.check_plant_health()

    print("\nTesting error recovery...")
    try:
        raise WaterError("Not enough water in tank")
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...\n")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
