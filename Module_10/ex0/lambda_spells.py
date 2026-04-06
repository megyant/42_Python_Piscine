
def artifact_storer(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda x: x.get('power'),
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x.get('power') >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    transformed_spells = list(map(lambda spell: '* ' + spell + ' *', spells))
    return transformed_spells


def mage_stats(mages: list[dict]) -> dict:
    max_power: int = max(mages, key=lambda x: x['power'])
    min_power: int = min(mages, key=lambda x: x['power'])
    avg_power: float = sum(map(lambda x: x.get('power'), mages)) / len(mages)

    return {'max_power': max_power, 'min_power': min_power,
            'avg_power': round(avg_power, 2)}


def main() -> None:
    print("\nTesting artifact sorter...")

    artifacts = ([{'name': 'Fire Staff', 'power': 92, 'type': 'staff'},
                  {'name': 'Crystal Orb', 'power': 85, 'type': 'orb'}])

    sorted_artifacts = artifact_storer(artifacts)

    for i in range(len(sorted_artifacts)):
        print(f"{sorted_artifacts[i].get('name')} "
              f"({sorted_artifacts[i].get('power')} power) comes "
              f"before {sorted_artifacts[i+1].get('name')} "
              f"({sorted_artifacts[i+1].get('power')} power)")
        break

    print("\nTesting power filter...")

    mages = ([{'name': 'Christopher', 'power': 9, 'element': 'fire'},
             {'name': 'Olaf', 'power': 11, 'element': 'water'},
             {'name': 'Elsa', 'power': 10, 'element': 'ice'},
             {'name': 'Anna', 'power': 7, 'element': 'eletric'}])
    min_power = 10

    filtered_mages = power_filter(mages, min_power)

    mages_left = []
    for i in range(len(filtered_mages)):
        mages_left.append(filtered_mages[i].get('name'))

    if len(mages_left) == 1:
        print(f"Only {mages_left} has enough power")
    else:
        print(f"{mages_left} have enough power")

    print("\nTesting spell transformer...")

    spells = ['wingardium leviosa', 'expeliarmus', 'diffindo']

    transformed_spells = spell_transformer(spells)
    formatted_spells = " ".join(transformed_spells)

    print(formatted_spells)

    print("\nTesting mage stats...")

    stats_mages = mage_stats(mages)

    print(f"Max power: {stats_mages.get('max_power').get('power')} "
          f"({stats_mages.get('max_power').get('name')})")
    print(f"Min power: {stats_mages.get('min_power').get('power')} "
          f"({stats_mages.get('min_power').get('name')})")
    print(f"Average: {stats_mages.get('avg_power')}")


if __name__ == "__main__":
    main()
