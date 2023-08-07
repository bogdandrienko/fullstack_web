# tkinter - встроенная, лёгкая и примитивная
# pyside2 - клон от pyqt5
# pyqt6 - лучшая на рынке ui интерфейсов
# kivy - сложная, сложная сборка, но кроссплатформа
import json
# TODO интерфейс на pyqt
import sys
import threading
import multiprocessing
import requests
from PyQt6 import QtWidgets, QtCore, QtGui
import cv2
from requests import Response
from bs4 import BeautifulSoup

# from PyQt6.QtWidgets import (
#     QApplication,
#     QCheckBox,
#     QComboBox,
#     QDateEdit,
#     QDateTimeEdit,
#     QDial,
#     QDoubleSpinBox,
#     QFontComboBox,
#     QLabel,
#     QLCDNumber,
#     QLineEdit,
#     QMainWindow,
#     QProgressBar,
#     QPushButton,
#     QRadioButton,
#     QSlider,
#     QSpinBox,
#     QTimeEdit,
#     QVBoxLayout,
#     QWidget,
#     QGridLayout,
# )

# 1: only code
# 2: with ui-designer


class Ui(QtWidgets.QWidget):
    def __init__(self, title: str):
        super().__init__()

        # вёрстка
        self.setWindowTitle(title)
        self.setGeometry(0, 0, 1280, 720)

        self.layout = QtWidgets.QGridLayout(self)
        # self.layout = QtWidgets.QVBoxLayout(self)
        # self.layout = QtWidgets.QHBoxLayout(self)

        self.label_path = QtWidgets.QLabel("Путь к картинке: ")
        self.layout.addWidget(self.label_path, 0, 0)

        self.edit_path = QtWidgets.QLineEdit("static/images/img.jpg")
        self.layout.addWidget(self.edit_path, 0, 1)

        self.button = QtWidgets.QPushButton("обработать")
        self.button.clicked.connect(self.start)
        self.layout.addWidget(self.button, 1, 1)
        # вёрстка

        # вывод на дисплей
        self.show()

    def start(self):
        print("...started...")
        try:
            path = self.edit_path.text()
            img = cv2.imread(path, cv2.IMREAD_COLOR)
            height, width, channels = img.shape

            # b/w
            grayImage = cv2.cvtColor(img[50:height-50, 50:width-50], cv2.COLOR_BGR2GRAY)
            (thresh, blackAndWhiteImage) = cv2.threshold(grayImage, 127, 255, cv2.THRESH_BINARY)

            # cv2.imshow('Black white image', blackAndWhiteImage)
            # cv2.imshow('Original image', img)
            # cv2.imshow('Gray image', grayImage)
            # cv2.waitKey(0)
            # cv2.destroyAllWindows()
            new_path = path.split(".")  # static/images/img.jpg
            file_path = new_path[0]
            extension = new_path[-1]
            new = f"{file_path}_new.{extension}"
            print(new)
            cv2.imwrite(new, grayImage)

        # cv2.imshow()
        # img = cv2.imwrite("geeksforgeeks.png", cv2.IMREAD_COLOR)
        except Exception as error:
            print(error)
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        def exam():
            url = "https://jsonplaceholder.typicode.com/posts/66"
            response: Response = requests.get(url=url, headers=headers)
            # response.text  # str
            # response.content  # butes
            # response.json()  # dict
            print(type(response), response)
            with open("static/data.json", "w") as file:
                json.dump(response.json(), file)

        # native - not SPA
        # beatifulsoup - bs4 - библитека для более удобной работы с многостраничныеми сайтами
        # selenium - эмуляция браузера (крайне сложно защититься)
        #

        def native():
            url = 'https://www.gismeteo.kz/weather-shymkent-5324/'
            response = requests.get(url=url, headers=headers)
            data = response.content.decode()
            data1 = data.split('''"day">Сегодня''')[1]
            data2 = data1.split('''class="tab-image"''')[0]
            day_with_night = data2.split('''<span class="unit unit_temperature_c">''')
            day_with_night = day_with_night[1::]
            if len(day_with_night[0]) < len(day_with_night[1]):
                day = day_with_night[1].split('''</span>''')[0]
                night = day_with_night[0].split('''</span>''')[0]
            else:
                day = day_with_night[0].split('''</span>''')[0]
                night = day_with_night[1].split('''</span>''')[0]
            print(f'{url}: Днём температура: {day}, а ночью: {night}')

        url = "https://www.google.com/search?q=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1" \
              "%83&rlz=1C1IXYC_ruKZ978KZ978&oq=%D1%82%D0%B5%D0%BD%D0%B3%D0%B5+%D0%BA+%D0%B4%D0%BE%D0%BB%D0%BB%D0%B0%D1%80%D1" \
              "%83&aqs=chrome.0.0i433i512j0i512l9.4659j1j7&sourceid=chrome&ie=UTF-8"
        headers = {
            "user-agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                          'AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/102.0.0.0 Safari/537.36'
        }
        response = requests.get(url=url, headers=headers)
        print(type(response), response)
        soup = BeautifulSoup(response.content, 'html.parser')
        valute = soup.findAll("span", {"class": "DFlfde SwHCTb"})[0]
        print(valute)
        print(f'{float(valute.get_text().replace(",", ".")) * 50000} $')

        pass


if __name__ == "__main__":  # вызывается только при "прямом" запуске файла (ui.py)
    app = QtWidgets.QApplication([])
    ui = Ui("Наше приложение для обработки фото")
    sys.exit(app.exec())
