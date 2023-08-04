# TODO простой пример
class Mother1:  # (object)
    eyes = "blue"  # Атрибут класса


class Child1(Mother1):
    height = 1.8  # Атрибут класса


m1 = Mother1()
print(m1.eyes)

ch1 = Child1()
print(ch1.eyes)
print(ch1.height)


class Obj:
    DEBUG = True
    # print(DEBUG)
    # DEBUG = False
    is_start_rendering1 = True
    visible = "публичное"  # публичное свойство экземпляра класса
    _visible = "защищённое"  # защищённое свойство экземпляра класса
    __visible = "приватное"  # приватное свойство экземпляра класса


obj1 = Obj()
print(obj1.visible)
print(obj1._visible)
# print(obj1.__visible)
# print(obj1._Obj__visible)


