def command_interpreter():
    import sys
    number = 1
    try:
        print(f"Program name: {sys.argv[0]}")
        for argument in sys.argv[1:]:
            print(f"Argument {number}: {argument}")
            number += number
        print(f"Total arguments: {len(sys.argv)}")
    except ValueError:
        print("No arguments provided!")


if __name__ == "__main__":
    command_interpreter()
