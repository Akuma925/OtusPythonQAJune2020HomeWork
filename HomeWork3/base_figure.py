""" Методы и переменные геометрических фигур"""

import math
from math import pi

class BaseFigure:
    """ Методы и переменные геометрических фигур"""

    angles = None
    name = None
    perimeter = None
    area = None

    def add_square(self, other_figure):
        """ Метод возвращает сумму площадей двух геометриеских фигур"""
        
        if isinstance(other_figure, BaseFigure):
            sum_areas = self.area + other_figure.area
            return sum_areas
        else:
            return 'Передан неверный класс геометрической фигуры'

    def get_angles(self, figure):
        """ Метод возвращает количество углов геометрической фигуры"""

        return figure.angles

    def get_name(self, figure):
        """ Метод возвращает количество углов геометрической фигуры"""

        return figure.name

class Triangle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "треугольник" """

    def __init__(self, side_a, side_b, side_c):
        """ Метод-инициализатор класса "треугольник" """

        self.name = 'Triangle'
        self.angles = 3
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр треугольника """

        perimeter = self.side_a + self.side_b + self.side_c
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь треугольника """

        half_perimeter = 0.5*self.calculate_perimeter()
        area = math.sqrt(half_perimeter*
                         (half_perimeter - self.side_a)*
                         (half_perimeter - self.side_b)*
                         (half_perimeter - self.side_c))
        return area

class Rectangle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "прямоугольник" """

    def __init__(self, side_a, side_b):
        """ Метод-инициализатор класса "прямоугольник" """

        self.name = 'Rectangle'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр прямоугольника """

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь прямоугольника """

        area = self.side_a * self.side_b
        return area

class Square(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "квадрат" """

    def __init__(self, side_a, side_b):
        """ Метод-инициализатор класса "квадрат" """

        self.name = 'Square'
        self.angles = 4
        self.side_a = side_a
        self.side_b = side_b
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр квадрата """

        perimeter = 2 * (self.side_a + self.side_b)
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь квадрата """

        area = self.side_a * self.side_b
        return area

class Circle(BaseFigure):
    """ Класс с переменными и методами геометрической фигуры "круг" """

    def __init__(self, radius):
        """ Метод-инициализатор класса "круг" """

        self.name = 'Circle'
        self.angles = 0
        self.radius = radius
        self.perimeter = self.calculate_perimeter()
        self.area = self.calculate_area()

    def calculate_perimeter(self):
        """ Метод вычисляет периметр круга """

        perimeter = 2 * pi * self.radius
        return perimeter

    def calculate_area(self):
        """ Метод вычисляет площадь круга """

        area = pi * (self.perimeter ** 2)
        print(area)
        return area
