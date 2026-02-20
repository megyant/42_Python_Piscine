import alchemy.elements


def sacred_scroll() -> None:
    print("=== Sacred Scroll Mastery ===\n")

    print("Testing direct module access:")
    print(f"alchemy.elements.create_fire(): {alchemy.elements.create_fire()}")
    print(f"alchemy.elements.create_water(): "
          f"{alchemy.elements.create_water()}")
    print(f"alchemy.elements.create_earth(): "
          f"{alchemy.elements.create_earth()}")
    print(f"alchemy.elements.create_air(): {alchemy.elements.create_air()}")

    print("\nTesting package-level access (controlled by __init__.py):")
    try:
        type = "alchemy.create_fire()"
        print(f"{type}: {alchemy.create_fire()}")
    except AttributeError:
        print(f"{type}: AttributeError - not exposed")

    try:
        type = "alchemy.create_water()"
        print(f"{type}: {alchemy.create_water()}")
    except AttributeError:
        print(f"{type}: AttributeError - not exposed")

    try:
        type = "alchemy.create_earth()"
        print(f"{type}: {alchemy.create_earth()}")
    except AttributeError:
        print(f"{type}: AttributeError - not exposed")

    try:
        type = "alchemy.create_air()"
        print(f"{type}: {alchemy.create_air()}")
    except AttributeError:
        print(f"{type}: AttributeError - not exposed")


if __name__ == "__main__":
    sacred_scroll()
