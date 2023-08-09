# LIFO - последним вошёл, первым вышел
# FIFO - первым вошёл, первым вышел (очередь в магазине)

# https://www.youtube.com/watch?v=Pp84Sv041xA&t=18594s&ab_channel=%D0%93%D0%BB%D0%B5%D0%B1%D0%9C%D0%B8%D1%85%D0%B0%D0%B9%D0%BB%D0%BE%D0%B2

# []

class Fifo:
    def __init__(self):
        self.data = []  # [1, 2, 3]   4

    def setter(self, num: int) -> None:
        self.data.append(num)

    def getter(self) -> int:
        # self.data.pop(len(self.data)-1)  # O(1) - самый быстрый
        val = self.data.pop(0)
        print("Извлечено: ", val)
        return val

    def __str__(self):
        res = ""
        for i in self.data:
            res += f" {i}"
        return res[1:]


f1 = Fifo()
print(f1)
f1.setter(12)
print(f1)
f1.setter(666)
print(f1)
f1.setter(7)
print(f1)
print(f1.getter())
print(f1)
print(f1.getter())
print(f1)
print(f1.getter())
print(f1)
