# from ex0.Card import Card
from .CreatureCard import CreatureCard


def main() -> None:
    print("=== DataDeck Card Foundation ===")

    print("\nTesting Abstract Base Class Design:")

    fire_dragon = CreatureCard("Fire Dragon", 5, "Legendary", 7, 5)

    print("\nCreatureCard Info:")
    info = fire_dragon.get_card_info()
    print(f"{info}\n")

    mana = 6
    print(f"Playing {fire_dragon.name} with {mana} available")

    is_playable = fire_dragon.is_playable(mana)
    print(f"Playable: {is_playable}")

    if is_playable:
        effect = "Creature summoned to battlefield"
        play = {"effect": effect}
        print('Play result: '
              f'{fire_dragon.play(play)}')

        target = "Goblin Warrior"
        print(f"\n{fire_dragon.name} attacks {target}:")
        print(f"Attack result: {fire_dragon.attack_target(target)}")
        mana = mana - fire_dragon.cost

    print(f"\nTesting insuficcient mana ({mana} available): ")

    is_playable = fire_dragon.is_playable(mana)
    print(f"Playable: {is_playable}")

    if is_playable:
        effect = "Creature summoned to battlefield"
        play = {"effect": effect}
        print('Play result: '
              f'{fire_dragon.play(play)}')

        target = "Goblin Warrior"
        print(f"\n{fire_dragon.name} attacks {target}:")
        print(f"Attack result: {fire_dragon.attack_target(target)}")
        mana = mana - fire_dragon.cost

    print("\nAbstract pattern successfully demonstrated!")


if __name__ == "__main__":
    main()
