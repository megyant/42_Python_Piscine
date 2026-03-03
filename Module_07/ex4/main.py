from .Rankable import Rankable
from .TournamentCard import TournamentCard
from .TournamentPlatform import TournamentPlatform


def main() -> None:
    print("\n===  DataDeck Tournament Platform ===\n")

    print("Registering Tournament Cards...\n")

    tournament = TournamentPlatform()

    tournament.register_card()


if __name__ == "__main__":
    main
