def check_plant_health(plant_name, water_level, sunlight_hours):
    if not plant_name:
        raise ValueError("Error: Plant name cannot be empty!")
    elif water_level > 10 or water_level < 1:
        if water_level > 10:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too high (max 10)")
        else:
            raise ValueError(f"Error: Water level {water_level} "
                             "is too low (min 1)")
    elif sunlight_hours > 12 or sunlight_hours < 2:
        if sunlight_hours > 12:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too high (max 12)")
        else:
            raise ValueError(f"Error: Sunlight hours {sunlight_hours} "
                             "is too low (min 2)")
    else:
        print(f"Plant '{plant_name}' is healthy!")


def test_plant_checks():
    print("=== Garden Plant Health Checker ===")

    print("\nTesting good values...")
    try:
        check_plant_health("tomato", 5, 5)
    except ValueError as e:
        print(e)

    print("\nTesting empty plant name...")
    try:
        check_plant_health(None, 5, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bad water level...")
    try:
        check_plant_health("tomato", 15, 5)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("tomato", -1, 5)
    except ValueError as e:
        print(e)

    print("\nTesting bad sunlight hours...")
    try:
        check_plant_health("tomato", 5, 0)
    except ValueError as e:
        print(e)
    try:
        check_plant_health("tomato", 5, 13)
    except ValueError as e:
        print(e)

    print("\nAll error raising tests completed!")


if __name__ == "__main__":
    test_plant_checks()
