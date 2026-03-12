import sys
import importlib


def check_dependencies(packages: list):
    for package in packages:
        try:
            module = importlib.import_module(package)

            if module is not None:
                name = module.__name__
                v = module.__version__
                if name == "pandas":
                    msg = "Data manipulation ready"
                elif name == "requests":
                    msg = "Network acess ready"
                elif name == "matplotlib":
                    msg = "Visualization ready"
                else:
                    msg = "ready"
                print(f"[OK] {name} ({v}) - {msg}")

            else:
                print(f"[MISSING] {package} - not ready")

                print("\nTry:")
                print("python3 -m venv matrix_env\n"
                      "source matrix_env/bin/activate")

                print("and")

                print("python3 -m pip install -r requirements.txt")
                print("python3 loading.py")

                print("or")

                print("python3 -m pip install poetry")
                print("poetry install")
                print("poetry run python loading.py")

                print("\nRun this program again.")
                sys.exit()
        except ImportError as e:
            print(f"Error: {e}")


def main() -> None:
    print("\nLOADING STATUS: Loading programs...\n")
    print("Checking dependencies:")

    try:
        dependencies = ["pandas", "requests", "matplotlib"]

        check_dependencies(dependencies)

        pd = importlib.import_module("pandas")
        plt = importlib.import_module("matplotlib.pyplot")
        np = importlib.import_module("numpy")

        print("\nAnalysing Matrix data...")

        data = pd.read_csv('Data.csv', delimiter=',')

        row_count = len(data)

        print(f"Processing {row_count} data points...")

        x = data['n_leaves']
        y = data['height']

        m, b = np.polyfit(x, y, 1)

        data.plot(x="n_leaves", y="height", kind='scatter', color='red')

        plt.plot(x, m*x + b, color='blue')

        plt.xlabel('Number of Leaves')
        plt.ylabel('Plant Height')

        print("Generating visualization...")
        file = "matrix\\_analysis.png"
        plt.savefig(file)

        print("\nAnalysis complete!")
        print(f"Results saved to: {file}")

        plt.show()
    except ImportError as e:
        print(f"Error: {e}")

        print("\nTry:")
        print("python3 -m venv matrix_env\n"
              "source matrix_env/bin/activate")

        print("and")

        print("python3 -m pip install -r requirements.txt")
        print("python3 loading.py")

        print("or")

        print("python3 -m pip install poetry")
        print("poetry install")
        print("poetry run python loading.py")

        print("\nRun this program again.")


if __name__ == "__main__":
    main()
