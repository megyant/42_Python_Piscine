import sys
import pandas
import importlib


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")

    print("Checking dependencies:")

    modules = ["pandas", "requests", "matplotlib"]

    for module in modules:
        lib = importlib.import_module(module)

        name = lib.__name__
        version = importlib.metadata.version(module)
        print(name, version)


if __name__ == "__main__":
    main()


