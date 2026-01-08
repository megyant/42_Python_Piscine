#!/usr/bin/env python3

def ft_plant_age():
    age = int(input("Enter plant age in days: "))
    ready_age = 60
    if age < ready_age:
        print("Plant needs more time to grow.")
    else:
        print("Plant is ready to harvest!")
