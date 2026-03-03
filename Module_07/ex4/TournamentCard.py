from ex0.Card import Card
from ex2.Combatable import Combatable
from .Rankable import Rankable


class TournamentCard(Card, Combatable, Rankable):
    def __init__(self, name: str, cost: int, rarity: str, damage: int,
                 defense_damage: int, id, rating) -> None:
        Card.__init__(self, name, cost, rarity)
        Combatable.__init__(self, damage, defense_damage)
        self.id = id
        self.rating = rating
        self.total_wins = 0
        self.total_losses = 0

    def play(self, game_state: dict) -> dict:
        game_state = {"card_played": self.name, "mana_used": self.cost,
                      "effect": "3 Damage"}
        return game_state

    def attack(self, target) -> dict:
        combat_type = "melee"
        return {"attacker": self.name, "target": target,
                "damage": self.damage, "combat_type": combat_type}

    def calculate_rating(self) -> int:
        return self.rating

    def update_wins(self, wins: int) -> None:
        self.total_wins += wins

    def update_losses(self, losses: int) -> None:
        self.total_losses += losses

    def get_rank_info(self) -> dict:
        pass

    def get_tournament_stats(self) -> dict:
        pass
