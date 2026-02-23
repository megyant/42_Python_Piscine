from .Card import Card


class CreatureCard(Card):
    def __init__(self, name: str, cost: int, rarity: str, attack: int, health: int) -> None:
        super().__init__(name, cost, rarity)
        self.attack = attack
        self.health = health
        self.type = "Creature"

    def get_card_info(self):
        info = {"name": self.name, "cost": self.cost, "rarity": self.rarity,
                "type": self.type, "attack": self.attack, "health": self.health}
        return info

    def play(self, game_state: dict) -> dict:
        pass

    # def attack_target(self, target: str) -> dict: