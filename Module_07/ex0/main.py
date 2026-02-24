# from ex0.Card import Card
from .CreatureCard import CreatureCard


def main():
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    info = fire_dragon.get_card_info()
    print(f"{info}\n")


if __name__ == "__main__":
    main()
