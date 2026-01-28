def garden_operations(error_type) -> None:
    if error_type == "value":
        int("abc")
    
    elif error_type == "zero":
        1/0
    
    elif error_type == "file":
        f = open("missing.txt")
    
    elif error_type == "key":
        garden = {"Tree":"Oak", "Flower":"Rose"}
        print(garden["missing plant"])   


def test_error_types():
    print(" === Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        garden_operations("value")
    except ValueError:
        print("Caught ValueError: invalid literal for int()")

    print("\nTesting ZeroDivisionError...")
    try:
        garden_operations("zero")
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero")

    print("\nTesting FileNotFoundError...")
    try:
        garden_operations("file")
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: No such file '{e.filename}'")
    
    print("\nTesting KeyError...")
    try:
        garden_operations("key")
    except KeyError as e:
        print(f"Caught KeyError: {e}")
    
    print("\nTesting multiple errors together...")
    try:
        garden_operations("value")
        garden_operations("zero")
        garden_operations("file")
        garden_operations("key")
    except (ValueError, FileNotFoundError, ZeroDivisionError, KeyError):
        print("Caught an error, but program continues!")
    
    print("\nAll error types tested sucessfully!")
    


if __name__ == "__main__":
    test_error_types()