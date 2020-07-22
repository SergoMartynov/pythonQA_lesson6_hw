class Rectangle:
    def __init__(self, length: int, width: int):
        self.length = length
        self.width = width
        self.angle = angle

    def area(self) -> int:
        return self.length * self.width

    def perimeter(self) -> int:
        return 2 * self.length + 2 * self.width

    # def angles_amount(self) -> int:
    #     return self.angle == 4

    def __dir__(self):
        return f'{self.__class__.__name__}[{self.length} x {self.width}]'


if __name__ == '__main__':
    rectangle = Rectangle(4, 3)
    print(rectangle, rectangle.area(), rectangle.perimeter())