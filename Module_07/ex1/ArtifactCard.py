from ex0.Card import Card


class ArtifactCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, durability: int,
                 effect: str) -> None:
        super().__init__(name, cost, rarity)
        self.durability = durability
        self.effect = effect

    def play(self, game_state: dict) -> dict:
        if (self.is_playable(game_state.get("is_playable")) is True):
            play = {"card_played": self.name, "mana used": self.cost,
                    "effect": "Permanent: +1 mana per turn"}
            return play

    def activate_ability(self) -> dict:
        pass
