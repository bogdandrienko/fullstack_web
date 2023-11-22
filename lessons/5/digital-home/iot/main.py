# import asyncio  # async
# import aiohttp  # web
# import aiofiles  # logs
# import aiosqlite  # cache
import datetime
import random
import time
import requests
import os

while True:
    dt = datetime.datetime.now()
    try:
        # получить/конвертировать данные
        data = {
            "id": random.randint(1, 1000),
            "param1": random.randint(0, 70),
            "datetime_iot": str(dt),
        }

        # заголовки
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (HTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
            "Authorization": "Token=token_auth123",
        }

        # отправить данные
        response = requests.post(  # TCP/IP HTTP request POST
            url="http://127.0.0.1:8000/api/communicator/",
            json={"subsystem": "водонагреватель", "datetime_subsystem": str(dt), "messages": data},
            headers=headers,
            timeout=5.0,
        )
        # Exception не прошедшего запроса

        # проверка на успешную отправку
        if response.status_code not in (200, 201):
            raise Exception(response.status_code)
            # Exception успешно прошедшего запроса

        # лог об успехе
        os.makedirs("logs", exist_ok=True)
        with open(f'logs/info_{dt.strftime("%Y_%m_%d_%H")}.txt', "a", encoding="utf-8") as file:
            file.write(f"{dt} {response.status_code}\n")
            print(f"{dt} {response.status_code}\n")
    except Exception as error:
        # лог об ошибке
        os.makedirs("logs", exist_ok=True)
        with open(f'logs/error_{dt.strftime("%Y_%m_%d_%H")}.txt', "a", encoding="utf-8") as file:
            file.write(f"{dt} {error}\n")
            print(f"{dt} {error}\n")

    time.sleep(3.0)
