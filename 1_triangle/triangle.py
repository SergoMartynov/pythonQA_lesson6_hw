class Triangle:
    name = 'треугольник'
    angles = 3

    def __init__(self, side1: int, side2: int, side3: int):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        if side1 + side2 <= side3 or side1 + side3 <= side2 or side2 + side3 <= side1:
            print('треугольник не существует')
        elif side1 != side2 and side1 != side3 and side2 != side3:
            print('треугольник разносторонний')
        elif side1 == side2 == side3:
            print('треугольник равносторонний')
        else:
            print('треугольник равнобедренный')

    def area(self) -> int:
        return self.side1 * self.side2 * self.side3

    def perimeter(self) -> int:
        return self.side1 + self.side2 + self.side3

    def __dir__(self):
        return f'{self.__class__.__name__}[{self.side1} x {self.side2} x {self.side3}]'


if __name__ == '__main__':
    print('введите стороны треугольника')
    a = int(input('a = '))
    b = int(input('b = '))
    c = int(input('c = '))
    triangle = Triangle(a, b, c)
    print(f'количество углов = {triangle.angles}')
    print(f'периметр = {triangle.perimeter()}')
    print(f'площадь = {triangle.area()}')
