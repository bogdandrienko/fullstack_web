"""Главный файл"""


class MeClass:
    """Вспомогательный класс"""

    def __init__(self, value):
        self.value = value

    def get_value(self):
        return self.value

    def set_value(self, value):
        try:
            self.value = int(value)
        except ValueError:
            print("Неверный формат!")
