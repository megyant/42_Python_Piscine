
def artifact_storer(artifacts: list[dict]) -> list[dict]:
    sorted_artifacts = sorted(artifacts, key=lambda x: x.get('power'),
                              reverse=True)
    return sorted_artifacts


def power_filter(mages: list[dict], min_power: int) -> list[dict]:
    filtered_mages = list(filter(lambda x: x.get('power') >= min_power, mages))
    return filtered_mages


def spell_transformer(spells: list[str]) -> list[str]:
    pass


def mage_stats(mages: list[dict]) -> dict:
    pass


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
             {'name': 'Olaf', 'power': 11, 'type': 'ice'}])
    min_power = 10

    filtered_mages = power_filter(mages, min_power)

    mages_left = []
    for i in range(len(filtered_mages)):
        mages_left.append(filtered_mages[i].get('name'))

    if len(mages_left) == 1:
        print(f"Only {mages_left} has enough power")
    else:
        print(f"{mages_left} have enough power")


if __name__ == "__main__":
    main()
