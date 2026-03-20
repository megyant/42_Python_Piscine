from typing import Any


def mage_counter() -> callable:
    count = 0

    def increment() -> int:
        nonlocal count
        count += 1
        return count

    return increment


def spell_accumulator(initial_power: int) -> callable:

    def increment() -> int:
        nonlocal initial_power
        initial_power += 5
        return initial_power

    return increment


def enchantment_factory(enchantment_type: str) -> callable:
    def apply_enchantment(item_name: str) -> str:
        return f"{enchantment_type} {item_name}"
    return apply_enchantment


def memory_vault() -> dict[str, callable]:
    dict_vault = {}

    def store(key: str, value: Any):
        dict_vault[key] = value

    def recall(key: str):
        return dict_vault.get(key, "Memory not found")

    return {"store": store, "recall": recall}


def main() -> None:

    print("\nTesting mage counter...")
    counter = mage_counter()
    print(f"Call 1: {counter()}")
    print(f"Call 2: {counter()}")
    print(f"Call 3: {counter()}")

    print("\nTesting spell accumulator...")
    initial_power = 0
    power = spell_accumulator(initial_power)
    print(f"Incrementing from {power()} to {power()} in power")

    print("\nTesting enchantment factory...")
    flaming = enchantment_factory("Flaming")
    frozen = enchantment_factory("Frozen")
    print(flaming("Sword"))
    print(frozen("Shield"))

    print("\nTesting memory vault...")

    vault = memory_vault()
    vault["store"]("Spell", "Fire Dragon")

    print(f"Recovering vault: {vault["recall"]("Spell")}")


if __name__ == "__main__":
    main()
