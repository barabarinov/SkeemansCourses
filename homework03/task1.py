class Vehicle:
    def __init__(self, brand, year, max_speed):
        self.brand = brand
        self.year = year
        self.max_speed = max_speed

    def move(self):
        print(f'Vehicle {self.brand} is moving with max speed {self.max_speed}!')

    def set_max_speed(self, max_speed):
        self.max_speed = max_speed

class Bus(Vehicle):

    def move(self):
        return f'Bus {self.brand} is moving'

if __name__ == '__name__':
    volzwagen_golf = Vehicle("VolzWagen Golf", 2010, 220)
    volzwagen_golf.move()

    honda_civic = Vehicle("Honda Civic", 1991, 190)

    toyota_camry = Vehicle("Toyota Camry", 2001, 210)

    volvo_recharge = Vehicle("Volvo Recharge", 2021, 230)

    some_bus = Bus("Volvo", 2001, 70)

    volzwagen_golf.move()
    honda_civic.move()
    toyota_camry.move()
    volvo_recharge.move()
    some_bus.move()

class Animal:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def say(self):
        print(f'Animal {self.name} is saying', self)

class Horse(Animal):

    def say(self):
        return f'Horse {self.name} is saying'
