from ex0.Card import Card


class SpellCard(Card):
    def __init__(self, name: str, cost: int, rarity: str,
                 effect_type: str) -> None:
        super().__init__(name, cost, rarity)
        self.effect_type = effect_type

    def play(self, game_state: dict) -> dict:
        if (self.is_playable(game_state.get("is_playable")) is True):
            play = {"card_played": self.name, "mana used": self.cost,
                    "effect": "Permanent: +1 mana per turn"}
            return play

    def resolve_effect(self, targets: list) -> dict:
        pass
