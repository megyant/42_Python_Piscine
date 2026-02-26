from ex0.Card import Card
from .Combatable import Combatable
from . Magical import Magical


class EliteCard(Card, Combatable, Magical):
    def play(self, game_state: dict) -> dict:
        game_state = {"card_played": self.name, "mana_used": self.cost,
                      "effect": "3 Damage"}
        return game_state

    def attack(self, target) -> dict:
        combat_type = "melee"
        return {"attacker": self.name, "target": target,
                "damage": self.cost, "combat_type": combat_type}

    def defend(self, incoming_damage: int) -> dict:
        damage_taken = round((incoming_damage / 3))
        damage_defended = incoming_damage - damage_taken

        still_alive = False

        if damage_taken < self.cost:
            still_alive = True

        return {"defender": self.name, "damage_taken": damage_taken,
                "damage_defended": damage_defended,
                "still_alive": still_alive}

    def get_combat_stats(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}

    def cast_spell(self, spell_name: str, targets: list) -> dict:
        total_mana = 11

        mana_used = 4
        total_mana -= mana_used
        return {"cater": self.name, "spell": spell_name,
                "targets": targets, "mana_used": mana_used}, total_mana

    def channel_mana(self, amount: int) -> dict:
        chanelled = round(amount / 3)

        return {"channeled": chanelled, "total_mana": amount}

    def get_magic_stats(self) -> dict:
        return {"name": self.name, "cost": self.cost, "rarity": self.rarity}
