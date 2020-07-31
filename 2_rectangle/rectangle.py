class Rectangle:
    name = 'прямоугольник'
    angles = 4

    def __init__(self, side1: int, side2: int):
        self.side1 = side1
        self.side2 = side2
        if side1 != side2:
            print('это прямоугольник')
        else:
            print('это не прямоугольник, а квадрат')

    def area(self) -> int:
        return self.side1 * self.side2

    def perimeter(self) -> int:
        return self.side1 * 2 + self.side2 * 2

    def __dir__(self):
        return f'{self.__class__.__name__}[{self.side1} x {self.side2}]'


if __name__ == '__main__':
    print('введите стороны прямоугольника')
    a = int(input('a = '))
    b = int(input('b = '))
    rectangle = Rectangle(a, b)
    print(f'количество углов = {rectangle.angles}')
    print(f'периметр = {rectangle.perimeter()}')
    print(f'площадь = {rectangle.area()}')
