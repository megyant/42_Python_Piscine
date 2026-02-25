from ex0.Card import Card
import random

class Deck:
    def __init__(self):
        self.card_list = []

    def add_card(self, card: Card) -> None:
        self.card_list.append(card)

    def remove_card(self, card_name: str) -> bool:
        for card in self.card_list:
            if card.name == card_name:
                self.card_list.remove(card_name)
                return True
        return False

    def shuffle(self) -> None:
        try:
            random.shuffle(self.card_list)
        except IndexError:
            print("Error: Deck is empty")

    def draw_card(self) -> Card:
        try:
            return random.sample(self.card_list)
        except IndexError:
            print("Error: Deck is empty")
            return None

    def get_deck_stats(self) -> dict:
        info = {"total_cards": len(self.card_list),
                "creatures": }

        return info
