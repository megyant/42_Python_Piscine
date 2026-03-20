from typing import Tuple


def spell_combiner(spell1: callable, spell2: callable) -> callable:
    def combined_spell(*args, **kwargs) -> Tuple[str, str]:
        result1 = spell1(*args, **kwargs)
        result2 = spell2(*args, **kwargs)
        return (result1, result2)
    return combined_spell


def power_amplifier(base_spell: callable, multiplier: int) -> callable:
    def accumulated_power(*args, **kwargs) -> int:
        original_value = base_spell(*args, **kwargs)
        return original_value * multiplier
    return accumulated_power


def conditional_caster(condition: callable, spell: callable) -> callable:
    def check_condition(*args, **kwargs) -> str:
        if condition(*args, **kwargs) is True:
            return spell(*args, **kwargs)
        else:
            return "Spell fizzled"
    return check_condition


def spell_sequence(spells: list[callable]) -> callable:
    def sequence(*args, **kwargs) -> list[callable]:
        all_results = []
        for spell in spells:
            result = spell(*args, **kwargs)
            all_results.append(result)
        return all_results
    return sequence


def main() -> None:

    print("\nTesting spell combiner...")

    def fireball() -> str:
        return "Fireball hits Dragon"

    def heal() -> str:
        return "Heals Dragon"

    combined = spell_combiner(fireball, heal)

    format_combined = ", ".join(combined())

    print(f"Combined spell result: {format_combined}")

    print("\nTesting power amplifier...")

    def original() -> int:
        return 10

    amplifier = 3
    amplified_power = power_amplifier(original, amplifier)
    print(f"Original: {original()}, Amplified: {amplified_power()}")

    print("\nTesting conditional caster...")

    def condition() -> bool:
        return False

    conditioned_spell = conditional_caster(condition, fireball)
    print(conditioned_spell())

    print("\nTesting spell sequence...")

    list_spells = [fireball, heal]
    sequence = spell_sequence(list_spells)
    format_sequence = ", ".join(sequence())
    print(format_sequence)
    print


if __name__ == "__main__":
    main()
