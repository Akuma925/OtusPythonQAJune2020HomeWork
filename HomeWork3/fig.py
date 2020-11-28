class Fig:
    def __init__(self, name):
        self.name = name
        self.area = 0
        self.perimeter = 0

    def information_employee(self):
        print('Name = {} '.format(self.name))
        print('S = {} '.format(self.area))
        print('P = {} '.format(self.perimeter))

    def add_square(self, new_fig):
        print(self.__class__)
        # print(self.__class__)
        # print(new_fig.__class__)
        if not isinstance(new_fig, self.__class__):
            print(f'{new_fig.__name__} is not a Fig')
        return
        res = self.area + new_fig.aria
        print("S: = ", res)
        return self.area + new_fig.aria


class Rectangle(Fig):
    def __init__(self, name, a, b):
        self.a = a
        self.b = b
        super().__init__(name)

    def getArea(self):
        self.area = self.a * self.b
        print(f'S: = {self.area}')
        return self.area

    def getPerimeter(self):
        self.perimeter = 2 * (self.a * self.b)
        print(f'P: = {self.perimeter}')
        return self.area


"""Квадрат"""


class Squer(Fig):
    def __init__(self, a, name):
        self.a = a
        super().__init__(name)

    def getArea(self):
        self.area = (self.a * self.a)
        print('S: = {} '.format(self.area))

    def getPerimeter(self):
        self.perimeter = 2 * self.a
        print(f'P: = {self.perimeter}')
        return self.area


elem = Squer(name="Квадрат", a=5)

elem.getArea()
elem.getPerimeter()
elem.information_employee()

elem1 = Rectangle(name="Rectangle", a=10, b=15)
elem1.getArea()
elem1.getPerimeter()
elem1.information_employee()

elem1.add_square(elem.__class__)

# """Триугольник"""
# class Triangle(Fig):
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c
#
#     def triangle(self):
#         print('a = {}'.format(self.a))
#         print('b = {}'.format(self.b))
#         print('c = {}'.format(self.c))
#         print('S = {} '.format(self.s))
#         print('P = {} '.format(self.p))
