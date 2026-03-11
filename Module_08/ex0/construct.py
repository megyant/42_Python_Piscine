import sys
import site


def test_environment() -> bool:
    try:
        return (sys.prefix == sys.base_prefix)
    except (ImportError, AttributeError) as e:
        print(f"Error: {e}")


def main() -> None:
    test = test_environment()

    if test is True:
        print("\nMATRIX STATUS: You're still plugged in\n")
    else:
        print("\nMATRIX STATUS: Welcome to the construct\n")

    if test is True:
        print(f"Current Python: {sys.executable}")
        print("Virtual Environment: None detected")

        print("\nWARNING: You're in the global environment!")
        print("The machines can see everything you install.")
        print("To enter the construct, run:\n"
              "python -m venv matrix_env\n"
              "source matrix_env/bin/activate # On Unix\n"
              "matrix_env\n"
              "Scripts\n"
              "activate # On Windows\n")

        print("Then run this program again.")
    else:
        print(f"Current Python: {sys.executable}")
        print(f"Virtual Environment: {sys.prefix}")

        print("\nSUCCESS: You're in an isolated environment!\n"
              "Safe to install packages without affecting\n"
              "the global system.")

        print("\nPackage installation path:")
        print(f"{site.getsitepackages()[0]}")


if __name__ == "__main__":
    main()
