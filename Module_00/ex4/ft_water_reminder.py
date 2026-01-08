def ft_water_reminder():
    last_watering = int(input("Days since last watering: "))
    watering_days = 2
    if last_watering > watering_days:
        print("Water the plants!")
    else:
        print("Plants are fine")
