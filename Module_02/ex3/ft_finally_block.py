class WaterError(Exception):
    pass


def water_plants(plant_list):
    try:
        print("Opening watering system")
        for plant in plant_list:
            if not plant:
                raise WaterError(f"Error: cannot water {plant} "
                                 "- invalid plant!")
            else:
                print(f"Watering {plant}")
    except WaterError as e:
        print(e)
    finally:
        print("Closing watering system (cleanup)")


def test_watering_system():
    print("=== Garden Watering System ===")

    print("\nTesting normal watering...")
    plant_list_good = ["tomato", "lettuce", "carrots"]
    water_plants(plant_list_good)
    print("Watering completed sucessfully!")

    print("\nTesting with error...")
    plant_list_bad = ["tomato", None]
    water_plants(plant_list_bad)

    print("\nCleanup always happens, even with errors!")


if __name__ == "__main__":
    test_watering_system()
