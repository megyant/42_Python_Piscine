import functools
import time


def spell_timer(func: callable) -> callable:
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Casting {func.__name__}...")
        start_time = time.time()
        result = func(*args, **kwargs)
        total_time = time.time() - start_time
        print(f"Spell completed in {total_time:.3f} seconds")
        return result
    return wrapper


def power_validator(min_power: int) -> callable:
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if args and not isinstance(args[0], int):
                current_power = args[1] if len(args) > 1 else 0
            else:
                current_power = args[0] if args else 0

            if current_power >= min_power:
                return func(*args, **kwargs)
            else:
                return "Insufficient power for this spell"
        return wrapper
    return decorator


def retry_spell(max_attempts: int) -> callable:
    def decorator(func: callable):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, max_attempts + 1):
                try:
                    return func(*args, **kwargs)
                except Exception:
                    if attempt < max_attempts:
                        print("Spell failed, retrying..."
                              f"{max_attempts - attempt} attempts left")
                    else:
                        print("Spell failed. No more attempts left")
            return f"Spell casting failed after {max_attempts} attempts"

        return wrapper
    return decorator


class MageGuild:

    @staticmethod
    def validate_mage_name(name: str) -> bool:
        if len(name) < 3:
            return False

        return all(char.isalpha() or char.isspace() for char in name)

    @power_validator(min_power=10)
    def cast_spell(self, spell_name: str, power: int) -> str:
        return f"Successfully cast {spell_name} with {power} power"


def main() -> None:
    print("\nTesting spell timer...")

    @spell_timer
    def fireball():
        return "Fireball cast!"

    result = fireball()

    print(f"Result: {result}")

    print("\nTesting power validator...")

    @power_validator(10)
    def fireball2(power: int):
        return f"Fireball cast with {power} power!"

    print(fireball2(12))

    print("\nTesting retry spell...")

    @retry_spell(max_attempts=3)
    def fireball3(count):
        if count == 1:
            raise Exception("Spell failed!")
        return "Fireball cast!"

    result = fireball3(1)
    print(f"Casting spell...{result}")

    print("\nTesting Mage Guild...")
    guild = MageGuild()
    print(guild.validate_mage_name("A"))
    print(guild.validate_mage_name("Dumbledore"))
    print(guild.cast_spell(15, "Fireball"))
    print(guild.cast_spell(1, "Fireball"))


if __name__ == "__main__":
    main()
