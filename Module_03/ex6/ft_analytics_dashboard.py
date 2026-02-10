
def analytics_dashboard():
    print("=== Game Analytics Dashboard ===\n")

    data = [
        {
            'name': 'alice',
            'score': 2300,
            'status': 'active',
            'score_status': 'high',
            'region': 'north',
            'achievements': ['first_kill',
                             'level_10',
                             'treasure_hunter',
                             'speed_demon']
        },
        {
            'name': 'bob',
            'score': 1800,
            'status': 'active',
            'score_status': 'medium',
            'region': 'east',
            'achievements': ['first_kill',
                             'level_10',
                             'boss_slayer']
        },
        {
            'name': 'charlie',
            'score': 2150,
            'status': 'active',
            'score_status': 'medium',
            'region': 'central',
            'achievements': ['first_kill',
                             'level_10',
                             'boss_slayer',
                             'collector',
                             'speed_demon',
                             'perfectionist',
                             'region_conquerer']
        },
        {
            'name': 'diana',
            'score': 2150,
            'status': 'inactive',
            'score_status': 'high',
            'region': 'central',
            'achievements': ['first_kill',
                             'level_10',
                             'collector']
        },
        {
            'name': 'frank',
            'score': 1350,
            'status': 'inactive',
            'score_status': 'low',
            'region': 'east',
            'achievements': ['first_kill',
                             'level_10']
        }
    ]

    print("=== List Comprehension Examples ===")

    high_scorers = (player['name'] for player in data if
                    player['score'] > 2000)
    print(f"High scorers (>2000): {list(high_scorers)}")

    scores_doubled = (player['score'] * 2 for player in data if
                      player['status'] == 'active')
    print(f"Scores doubled: {list(scores_doubled)}")

    active_players = (player['name'] for player in data if
                      player['status'] == 'active')
    print(f"Active players: {list(active_players)}")

    print("\n=== Dict comprehension Examples ===")

    player_scores = {player['name']: player['score'] for player in data}
    print(f"Player scores: {player_scores}")

    categories = {}
    for player in data:
        status = player['score_status']
        categories[status] = categories.get(status, 0) + 1
    print(f"Score categories: {categories}")

    achievement_counts = {player['name']: len(player['achievements'])
                          for player in data}
    print(f"Achievement counts: {achievement_counts}")

    print("\n=== Set comprehension Examples ===")

    unique_players = {player['name'] for player in data}
    print(f"Unique players: {unique_players}")

    unique_achievements = {achievement for player in data for achievement
                           in player['achievements']}
    print(f"Unique achievements: {unique_achievements}")

    active_regions = {player['region'] for player in data if
                      player['status'] == 'active'}
    print(f"Active regions: {active_regions}")

    print("\n=== Combined Analysis ===")

    print(f"Total players: {len(data)}")

    print(f"Total unique achievements: {len(unique_achievements)}")

    print("Average score: "
          f"{sum(player_scores.values()) / len(player_scores.values())}")

    top_performer = max(data, key=lambda player: player['score'])
    print(f"Top performer: {top_performer['name']} "
          f"({top_performer['score']} points, "
          f"{len(top_performer['achievements'])} achievements)")


if __name__ == "__main__":
    analytics_dashboard()
