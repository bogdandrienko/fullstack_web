import datetime
import time
import requests

def new():
    while True:
        fake_data = [
            {"id": 1, "name": "first", "date_time": str(datetime.datetime.now())},
            {"id": 2, "name": "second", "date_time": str(datetime.datetime.now())},
        ]
        json_data = fake_data
        headers = {'Content-Type': 'application/json', 'Token': 'application'}
        response = requests.post(url="http://127.0.0.1:8000/api/communicator", data=json_data, headers=headers)
        if response.status_code not in (200, 201):
            raise Exception(response.status_code)
        time.sleep(5)