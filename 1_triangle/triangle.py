class Triangle:
    def __init__(self, length1: int, length2: int, length3: int):
        self.length1 = length1
        self.length2 = length2
        self.length3 = length3

    # def area(self) -> int:
    #     return self.length * self.width

    def perimeter(self) -> int:
        return self.length1 + self.length2 + self.length3

    # def angles_amount(self) -> int:
    #     return self.angle == 4

    def __dir__(self):
        return f'{self.__class__.__name__}[{self.length1} x {self.length2} x {self.length3}]'


if __name__ == '__main__':
    triangle = Triangle(4, 2, 2)
    print(triangle, triangle.perimeter())