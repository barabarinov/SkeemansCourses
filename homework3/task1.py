
# Write a class Vehicle, that have brand, year_of_production and max_speed attributes in it.
# Add method move, that prints 'Vehicle is moving'
# Instantiate some of the vehicles

class Vehicle:
    def __init__(self, brand, year, max_speed):
        self.brand = brand
        self.year = year
        self.max_speed = max_speed
    def move(self):
        print(f'{Vehicle} is moving')
# class Buse:
#     def __init__(self):
#         super().__init__()


