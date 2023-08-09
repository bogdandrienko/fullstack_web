class Fugure:
    PI = 3.14  # атрибут класса (можно обращаться, не создавая экземпляр)

    def __init__(self, name: str = "Квадрат"):
        self.name = name  # атрибут экземпляра класса (обязателен при создании класса)


class Calculate(object):
    def __eq__(self, other):  # __магический__-method - обычно тут лежит "сравнение" двух объектов
        # тут надо описать критерии сравнения
        pass

    def __abs__(self):  # absolute - число по модулю
        # cl1 = abs(Calculate())
        pass

    def get_square(self):
        return self.side * 4

    # def __init__(self): - инициализатор, вызывает при создании экземпляра (возвращает ссылку на класс)
    # def __new__(self): - конструктор, получает аргументы и возвращает класс в метод init
    # def __new__(cls, *args, **kwargs):
    #     return cls(*args, **kwargs)
    # def __str__(self): - строковые представления объекта - print
    # def __repr__(self): - строковые глубокое представления объекта - print
    # def __add__(self, other): - сложение


class Circle(Fugure):  # одиночное наследование
    def __init__(self, name: str = "Круг"):
        super().__init__(name=name + "_")

    def __str__(self):
        return f"<1Point(Circle) name={self.name} />"

    def __repr__(self):
        return f"<2Point(Circle) name={self.name} />"


class Point(Circle):  # каскадное(одиночные в ряд) наследование
    def __init__(self, name: str = "Круг"):
        super().__init__(name=name + "_")
        self.side = 0


class Romb(Circle, Calculate):  # множественное наследование (приоритет слева направо)
    def __init__(self, side, name: str = "Ромб"):
        super().__init__(name=name + "_")
        self.side = side
        # self.radius = self.side * 4 # 0.1 c, 30% случаев, когда эта переменная не нужна
        self.radius = None  # public (публичная) - можно читать, можно заменять
        self._radius = "protected"  # protected (защищённый) - строго внутри класса, но напрямую
        self.__radius = "private"  # private (приватный) - строго внутри класса, через методы (getter, setter...)

    def getter_radius1(self, nullable: bool = False):
        if self.radius is None or nullable:
            self.radius = self.side * 4
        return self.radius

    def getter_radius(self, numbers: int):
        if self.radius is None:
            self.radius = self.side * 4
        return round(self.radius, numbers)

    def setter_radius(self, radius: int | float):
        self._radius = float(radius) + 0.00000001


# print(Fugure.PI)
# f1 = Fugure()
# print(f1.name)

c1 = Circle("Круглешок")
print(c1.name)
print(c1)  # <__main__.Circle object at 0x0000023852DB5BD0>
# print(c1)  # <__main__.Circle object at 0x0000023852DB5BD0>

r1 = Romb(name="Ромб", side=12)
print(r1.radius)
print(r1.getter_radius(1))
print(r1.radius)
print(r1._radius)
# print(r1.__radius)  # AttributeError: 'Romb' object has no attribute '__radius'
print(r1._Romb__radius)  # AttributeError: 'Romb' object has no attribute '__radius'

# лёгкий             средний     сложный        супер-надёжный
# процедурное                 ООП              функциональное(haskel, F#)
