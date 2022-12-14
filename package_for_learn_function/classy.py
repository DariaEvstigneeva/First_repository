from math import sqrt

class Point:
    #конструктор для создания объекта
    def __init__(self, x, y): #класс содержит след. атрибуты: х и у
        self.x = x
        self.y = y

    #метод который вычисляет расстояние между двумя точками
    def distance2(self, p2): #p1 это точка 1, p2 это точка 2
        dx = p2.x - self.x
        dy = p2.y - self.y
        return sqrt(dx*dx+dy*dy)

    # функция сравнения объектов обязатеьна, если сравниваются объекты,
    # т.к логически объекты могут быть одинаковы, но физически отличаються
    def __eq__(self, p2):
        return self.x == p2.x and self.y == p2.y


    # сортировка по координате y (именно lt пользуется питон, когда выполняет сортировку
    def __lt__(self, other):
        return self.y > other.y
