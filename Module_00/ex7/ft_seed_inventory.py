#!/usr/bin/env python3

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    seed = seed_type.capitalize()

    if unit == "area":
        print(f"{seed} seeds: covers {quantity} square meters")
    elif unit == "grams":
        print(f"{seed} seeds: {quantity} grams total")
    elif unit == "packets":
        print(f"{seed} seeds: {quantity} packets available")
    else:
        print("Unkown unit type")
