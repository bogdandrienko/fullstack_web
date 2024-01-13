import datetime
import threading
import time
from starlette.requests import Request


class CacheServer:
    def __init__(self):
        self.data: dict[str, any] = {}  # константная O(1)
        self.clear_tasks: dict[str, datetime.datetime] = {}

    def get(
        self,
        key: str = None,
        request: Request = None,
        query: callable = None,
        timeout: float = 1.0,
    ):
        if key is None:
            key = f"{request.url}_{request.method}_{''.join([str(x) for x in request.query_params.values()])}"
        value = self.data.get(key, None)
        if value is None and query:
            value = query()()
            self.set(key=key, value=value, timeout=timeout)

        return value

    def set(self, key: str, value: any, timeout: float = 1.0):
        self.data[key] = value
        threading.Thread(
            target=self.clear_cache,
            args=(),
            kwargs={
                "key": key,
                "timeout": timeout,
            },
        ).start()

    def clear(self, key: str):
        if self.data.get(key, None) is not None:
            del self.data[key]

    def reset(self):
        self.data = {}

    def clear_cache(self, key: str, timeout: float = 1.0):
        if 0.0 >= timeout > 99999:
            return

        # запоминаю время начала этой задачи
        date_time = datetime.datetime.now()
        self.clear_tasks[key] = date_time

        time.sleep(timeout)

        # отменяю задачу очистки кэша, если он был перезаписан
        if self.clear_tasks.get(key, None) != date_time:
            return

        if self.data.get(key, None) is not None:
            del self.data[key]
