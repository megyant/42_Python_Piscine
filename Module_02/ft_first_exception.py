def check_temperature(temp_str):
    print(f"Testing temperature: {temp_str}")
    try:
        temp = int(temp_str)
        if temp > 40:
            print(f"Error: {temp}ºC is too hot for plants (max 40ºC)")
        elif temp < 0:
            print(f"Error: {temp}ºC is too cold for plants (min 0ºC)")
        else:
            print(f"Temperature {temp}ºC is perfect for plants!")

    except ValueError:
        print(f"Error: '{temp_str}' is not a valid number")


if __name__ == "__main__":
    print("=== Garden Temperature Checker ===")
    print()

    check_temperature("25")
    print()
    check_temperature("abc")
    print()
    check_temperature("100")
    print()
    check_temperature("-50")
    print()

    print("All tests completed - program didn't crash!")
