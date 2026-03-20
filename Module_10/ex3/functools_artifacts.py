import functools
import operator


def spell_reducer(spells: list[int], operation: str) -> int:
    operations = {
        "add": operator.add,
        "multiply": operator.mul,
        "max": max,
        "min": min
    }

    if operation not in operations:
        raise ValueError("Error: not a known operation")

    return functools.reduce(operations[operation], spells)


def partial_enchanter(base_enchantment: callable) -> dict[str, callable]:
    return {
        "fire_enchant": functools.partial(base_enchantment, power=50,
                                          element="Fire"),
        "ice_enchant": functools.partial(base_enchantment, power=50,
                                         element="Ice"),
        "lightning_enchant": functools.partial(base_enchantment, power=50,
                                               element="Lightning")
    }


@functools.lru_cache(maxsize=None)
def memoized_fibonacci(n: int) -> int:
    if n <= 1:
        return n
    return memoized_fibonacci(n - 1) + memoized_fibonacci(n - 2)


def spell_dispatcher() -> callable:
    @functools.singledispatch
    def cast_spell(spell_data):
        return f"Oops not a known type: {spell_data}"

    @cast_spell.register(int)
    def _(spell_data):
        return f"Damage: {spell_data}"

    @cast_spell.register(str)
    def _(spell_data):
        return f"Effect: {spell_data}"

    @cast_spell.register(list)
    def _(spell_data):
        return f"Launching: {spell_data}"

    return cast_spell


def main() -> None:
    print("\nTesting spell reducer...")
    try:
        spells = [4, 30, 26, 40]

        print(f"Sum: {spell_reducer(spells, "add")}")
        print(f"Product: {spell_reducer(spells, "multiply")}")
        print(f"Max: {spell_reducer(spells, "max")}")

        print("\nTesting partial enchanter...")

        def base_enchantment(power: int, element: str) -> str:
            return f"Using {element} element with {power} power"

        enchanter = partial_enchanter(base_enchantment)

        print(enchanter["fire_enchant"]())

        print("\nTesting memoized fibonacci...")

        print(f"Fib(10): {memoized_fibonacci(10)}")
        print(f"Fib(10): {memoized_fibonacci(15)}")

        print("\nTesting spell dispatcher...")

        dispatcher = spell_dispatcher()

        print(f"int: {dispatcher(10)}")
        print(f"str: {dispatcher("Fire")}")
        print(f"lst: {dispatcher(["Ice", "Fire"])}")

    except (ValueError, Exception) as e:
        print(e)


if __name__ == "__main__":
    main()
