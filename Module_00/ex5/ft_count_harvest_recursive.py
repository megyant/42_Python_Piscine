def ft_count_harvest_recursive(now=1, days=None):
    if days is None:
        days = int(input("Days until harvest: "))

    if now > days:
        print("Harvest time!")
        return

    print(f'Day {now}')
    ft_count_harvest_recursive(now + 1, days)
