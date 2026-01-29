class WaterError(Exception):
    def __init__(self, message):
        super().__init__(message)


def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if plant != "None":
                print(f"Watering {plant}")
            else:
                raise WaterError(f"Error: cannot water {plant}"
                                 "- invalid plant!")
    except WaterError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plant_list = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list)
    print("Watering completed sucessfully!")

    print("\nTesting with error...")
    plant_list = ["tomato", "None"]
    water_plants(plant_list)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
