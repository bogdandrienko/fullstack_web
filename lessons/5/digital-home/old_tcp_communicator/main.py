"""
pyqt6(ui) + asyncio(async python) + aiohttp(web) +
aiofiles(logs) + aiosqlite(db - local cache)
"""

import datetime
import json
import random
import sys
import time
import threading
import sqlite3

import asyncio
import aiosqlite
import aiofiles

from PyQt6 import uic
from PyQt6.QtWidgets import QWidget, QApplication


class Ui(QWidget):
    start_app_delay = 1  # 30s
    saver_delay = 3  # 3s - зависит от частоты обновления устройства
    sender_delay = 5  # 5s - звисит от нагрузки на сервер и от количества трафика
    database_src = "src/database.db"  # :memory:
    log_src = f'src/logs/{datetime.datetime.now().strftime("%Y_%m_%d_%H")}.txt' # 2023_10_14_12
    date_time_format = "%Y-%m-%d %H:%M:%S.%f"

    def __init__(self):
        super().__init__()
        self.ui = uic.loadUi("src/main.ui", self)
        self.show()  # to tray

        new_thread = threading.Thread(target=self.start_app)
        new_thread.start()

    def start_app(self):
        time.sleep(self.start_app_delay)

        # from source -> database(queue)
        new_thread = threading.Thread(target=self.start_worker_saver)
        new_thread.start()

        # from database(queue) -> web
        new_thread = threading.Thread(target=self.start_worker_sender)
        new_thread.start()

    def start_worker_saver(self):
        with sqlite3.connect(self.database_src) as connection:
            cursor = connection.cursor()
            query = """
CREATE TABLE IF NOT EXISTS Message(
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
datetime TEXT,
message TEXT NOT NULL
);
"""
            cursor.execute(query)

        while True:
            time.sleep(self.saver_delay)
            asyncio.run(self.worker_saver())  # sync -> async

    async def get_data_from_source(self) -> dict:
        # from api / db / file / ...
        await asyncio.sleep(1)
        int_1 = random.randint(1, 100000000)

        # плавающая ошибка
        if int_1 % 2 == 0:
            raise Exception("Invalid data")

        return {"id": int_1, "value": int_1 * 2}

    async def save_data_to_database(self, date_time: str, message: dict):
        async with aiosqlite.connect(self.database_src) as connection:
            query = """
INSERT INTO Message 
(datetime, message) 
VALUES 
(?, ?)
"""
            await connection.execute(query, (date_time, json.dumps(message)))  # против SQL injection
            await connection.commit()

    async def worker_saver(self):
        try:
            try:
                message: dict = await self.get_data_from_source()  # пока нет ответа, поток работает где-то ещё
            except:  # если первый раз не отработало, то попытаться ещё раз
                await asyncio.sleep(1)
                message: dict = await self.get_data_from_source()

            date_time = datetime.datetime.now().strftime(self.date_time_format)
            try:
                await self.save_data_to_database(date_time=date_time, message=message)
            except:
                await asyncio.sleep(1)
                await self.save_data_to_database(date_time=date_time, message=message)

            self.ui.label_datetime.setText(date_time)
            self.ui.label_message.setText(json.dumps(message))
        except Exception as error:
            data_time = datetime.datetime.now().strftime(self.date_time_format)
            error_message = f'{data_time} ERROR: {error}\n'

            print(error_message)
            self.ui.label_datetime.setText(data_time)
            self.ui.label_message.setText(f'ERROR: {error}')
            async with aiofiles.open(self.log_src, mode='a') as f:
                await f.write(error_message)

    def start_worker_sender(self):
        while True:
            time.sleep(self.sender_delay)
            asyncio.run(self.worker_sender())

    async def get_messages_from_database(self) -> list[dict]:
        async with aiosqlite.connect(self.database_src) as db:
            query = """
SELECT id, datetime, message
FROM Message
ORDER BY id ASC
LIMIT 10;
"""
            async with db.execute(query) as cursor:
                rows: list[dict] = []
                async for row in cursor:
                    rows.append(
                        {"id": row[0], "datetime": row[1], "message": row[2]}
                    )
                return rows

    async def send_message_to_api(self, body: bytes) -> bool:
        async with aiosqlite.connect(self.database_src) as connection:
            query = """
INSERT INTO Message 
(datetime, message) 
VALUES 
(?, ?)
"""
            await connection.execute(query, (date_time, json.dumps(message)))  # против SQL injection
            await connection.commit()

    async def delete_messages_from_database(self, id_from: int, id_to):
        async with aiosqlite.connect(self.database_src) as connection:
            query = """
INSERT INTO Message 
(datetime, message) 
VALUES 
(?, ?)
"""
            await connection.execute(query, (date_time, json.dumps(message)))  # против SQL injection
            await connection.commit()

    async def worker_sender(self):
        # 1 - взять из базы первые 10 записей
        messages: list[dict] = await self.get_messages_from_database()
        print(f"messages: {messages}")

        # 2 - отправить записи на backend



        # try:
        #     messages: list[dict] = await self.get_messages_from_database()

            #
            #
            # # 3 - удалить эти записи из очереди при успешном ответе на сервера
            #
            # try:
            #     message: dict = await self.get_data_from_source()  # пока нет ответа, поток работает где-то ещё
            # except:  # если первый раз не отработало, то попытаться ещё раз
            #     await asyncio.sleep(1)
            #     message: dict = await self.get_data_from_source()
            #
            # date_time = datetime.datetime.now().strftime(self.date_time_format)
            # try:
            #     await self.save_data_to_database(date_time=date_time, message=message)
            # except:
            #     await asyncio.sleep(1)
            #     await self.save_data_to_database(date_time=date_time, message=message)
            #
            # self.ui.label_datetime.setText(date_time)
            # self.ui.label_message.setText(json.dumps(message))
        # except Exception as error:
        #     data_time = datetime.datetime.now().strftime(self.date_time_format)
        #     error_message = f'{data_time} ERROR: {error}\n'
        #
        #     print(error_message)
        #     self.ui.label_datetime.setText(data_time)
        #     self.ui.label_message.setText(f'ERROR: {error}')
        #     async with aiofiles.open(self.log_src, mode='a') as f:
        #         await f.write(error_message)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    ui = Ui()
    sys.exit(app.exec())



