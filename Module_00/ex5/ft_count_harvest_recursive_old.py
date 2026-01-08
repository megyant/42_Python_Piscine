#!/usr/bin/env python3

def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def helper(now):
        if now > days:
            print("Harvest time!")
            return
        print(f'Day {now}')
        helper(now + 1)
    helper(1) 
