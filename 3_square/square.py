class Rectangle:
    def __init__(self, side1: int, side2: int, angle: int):
        self.side1 = side1
        self.side2 = side2
        self.angle = angle

    def area(self) -> int:
        return self.side1 * self.side2

    def perimeter(self) -> int:
        return 2 * self.side1 + 2 * self.side2

    # def angles_amount(self) -> int:
    #     return self.angle == 4

    def __dir__(self):
        return f'{self.__class__.__name__}[{self.side1} x {self.side2}]'


if __name__ == '__main__':
    rectangle = Rectangle(4, 3, 90)
    print(rectangle, rectangle.area(), rectangle.perimeter())