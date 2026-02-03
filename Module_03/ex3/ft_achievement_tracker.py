def achievement_tracker():
    print("=== Achievement Tracker System ===\n")

    players = {
        'alice': ['first_kill', 'level_10', 'treasure_hunter', 'speed_demon'],
        'bob': ['first_kill', 'level_10', 'boss_slayer', 'collector'],
        'charlie': ['level_10', 'treasure_hunter', 'boss_slayer',
                    'speed_demon', 'perfectionist']
               }

    alice = set(players['alice'])
    bob = set(players['bob'])
    charlie = set(players['charlie'])
    print(f"Player alice achievements: {players['alice']}")
    print(f"Player bob achievements: {players['bob']}")
    print(f"Player charlie achievements: {players['charlie']}")

    print("\n=== Achievement Analytics ===")

    union = alice.union(bob).union(charlie)
    print(f"All unique achievements: {union}")
    print(f"Total unique achievements: {len(union)}")

    intersect = alice.intersection(bob).intersection(charlie)
    print(f"\nCommon to all players: {intersect}")

    alice_bob = alice.intersection(bob)
    alice_charlie = alice.intersection(charlie)
    bob_charlie = bob.intersection(charlie)

    all_common = alice_bob.union(alice_charlie).union(bob_charlie)
    rare = union.difference(all_common)
    print(f"Rare achievements (1 player): {rare}")

    print(f"\nAlice vs Bob common: {alice_bob}")
    print(f"Alice unique: {alice.difference(alice_bob)}")
    print(f"Alice unique: {bob.difference(alice_bob)}")


if __name__ == "__main__":
    achievement_tracker()
