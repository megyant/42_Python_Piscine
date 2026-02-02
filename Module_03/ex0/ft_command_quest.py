def command_interpreter():
    import sys
    number = 1
    try:
        if (len(sys.argv) < 2):
            raise ValueError("No arguments provided!")
    except ValueError as e:
        print(e)
    print(f"Program name: {sys.argv[0]}")
    for argument in sys.argv[1:]:
        print(f"Argument {number}: {argument}")
        number += 1
    print(f"Total arguments: {len(sys.argv)}")


if __name__ == "__main__":
    command_interpreter()
