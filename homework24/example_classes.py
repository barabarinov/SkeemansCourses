class Rectangle:
    def __init__(self, side_a, side_b):
        self.side_a = side_a
        self.side_b = side_b

    def __repr__(self):
        return f'Rectangle {self.side_a} x {self.side_b}'


class Circle:
    def __init__(self, radius):
        self.radius = radius

    def __repr__(self):
        return f'Radius {self.radius}'

    @staticmethod
    def from_rectangle(rectangle):
        radius = (rectangle.side_a ** 2 + rectangle.side_b ** 2) ** 0,5 / 2
        return Circle(radius)


def main():
    rectangle = Rectangle(3, 4)
    print(rectangle)

    first_circle = Circle(1)
    print(first_circle)

    second_circle = Circle.from_rectangle(rectangle)
    print(second_circle)


if __name__ == '__main__':
    main()
