from alchemy import create_fire, create_water
from .elements import create_earth, create_air


def healing_potion():
    return (f"Healing potion brewed with {create_fire()} and "
            f"{create_water()}")


def strength_potion():
    return (f"Strength potion brewed with {create_earth()} and "
            f"{create_fire()}")


def invisibility_potion():
    return (f"Strength potion brewed with {create_air()} and "
            f"{create_water()}")


def wisdom_potion():
    return (f"Strength potion brewed with {create_air()},  "
            f"{create_water()}, {create_fire} and {create_earth}")
