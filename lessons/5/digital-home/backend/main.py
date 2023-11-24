import contextlib
import datetime
import json
import random
import sqlite3

#
import aiosqlite
import aiofiles
import aiohttp
import asyncio

#
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app = FastAPI(
    title="ChimichangApp",
    description="""
ChimichangApp API helps you do awesome stuff. 🚀

## Items

You can **read items**.

## Users

You will be able to:

* **Create users** (_not implemented_).
* **Read users** (_not implemented_).
""",
    summary="Deadpool's favorite app. Nuff said.",
    version="0.0.1",
    terms_of_service="https://example.com/terms/",
    contact={
        "name": "Deadpoolio the Amazing",
        "url": "https://x-force.example.com/contact/",
        "email": "dp@x-force.example.com",
    },
    license_info={
        "name": "Apache 2.0",
        "url": "https://www.apache.org/licenses/LICENSE-2.0.html",
    },
)
app.mount(
    "/static",
    StaticFiles(directory="build/static"),
    name="static",
)
# app.mount(
#     "/media",
#     StaticFiles(directory="media"),
#     name="media",
# )
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        # 3000
        "http://localhost:3000",
        "localhost:3000",
        "http://127.0.0.1:3000",
        "127.0.0.1:3000",
        # 8000
        "http://localhost:8000",
        "localhost:8000",
        "http://127.0.0.1:8000",
        "127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
async def startup_event():
    # redis
    # aioredis

    # безопасное создание базы данных и таблицы
    with contextlib.closing(sqlite3.connect("message.db")) as connection:  # sqlite3.connect(":memory:"))
        with connection as cursor:
            # TODO - последние для каждой подсистемы
            # для дашборда последних показателей(0.5)
            query = """
CREATE TABLE IF NOT EXISTS message (
    id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
    subsystem TEXT UNIQUE NOT NULL,
    message TEXT NOT NULL,
    datetime_subsystem TEXT NOT NULL,
    datetime_server TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""
            cursor.execute(query)
            cursor.commit()

    # безопасное создание базы данных и таблицы
    with contextlib.closing(sqlite3.connect("message.db")) as connection:  # sqlite3.connect(":memory:"))
        with connection as cursor:
            # TODO - все исторические
            # для графиков
            query = """
CREATE TABLE IF NOT EXISTS message_history (
id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
subsystem TEXT NOT NULL,
message TEXT NOT NULL,
datetime_subsystem TEXT NOT NULL,
datetime_server TEXT NOT NULL DEFAULT CURRENT_TIMESTAMP
);
"""
            cursor.execute(query)
            cursor.commit()

    print(f"\n.....server at {datetime.datetime.now()} started.....\n\n\n")


@app.on_event("shutdown")
def shutdown_event():
    print(f"\n\n\n.....server at {datetime.datetime.now()} stopped.....\n")


@app.get("/")
async def index():
    return "OK"


@app.get("/api")
async def read_root():
    return {"message": "ok"}


@app.get("/api/pagination/")
async def get_api_pagination(request: Request):
    if request.client.host != "127.0.0.1":
        if request.headers.get("Authorization", "") != "Token=token_auth123":
            raise Exception("Access denied")

    await asyncio.sleep(1.0)

    query_params = request.query_params
    # page = query_params["page"]  # required
    page = int(query_params.get("page", 1)) - 1  # default
    limit = int(query_params.get("limit", 10))
    # fake
    # костыль
    if page == -2:
        messages = []
        for i in range(1, 1000):
            messages.append(
                {
                    "id": i,
                    "param1": 139 + i,
                    "param2": 169 - i,
                    "name": random.choice(["Первый", "Второй", "Третий"]),
                    "datetime_iot": "2023-11-18 11:43:15.824762",
                }
            )
    else:
        messages = []
        for i in range(limit * page + 1, (limit * page) + 11):
            messages.append(
                {
                    "id": i,
                    "param1": 139 + i,
                    "param2": 169 - i,
                    "name": random.choice(["Первый", "Второй", "Третий"]),
                    "datetime_iot": "2023-11-18 11:43:15.824762",
                }
            )

    return {"data": messages, "x_total_count": 100}


@app.get("/api/communicator/")
async def get_api_communicator(request: Request):
    if request.client.host != "127.0.0.1":
        if request.headers.get("Authorization", "") != "Token=token_auth123":
            raise Exception("Access denied")

    await asyncio.sleep(1.0)

    # query_params = request.query_params
    # page = query_params["page"]
    # page = query_params.get("page", 1)
    datetime_server = datetime.datetime.now()

    # fake
    # messages = []
    # for i in range(0, 100):
    #     messages.append({"id": i, "param1": 139 + i, "param2": 169 - i, "datetime_iot": "2023-11-18 11:43:15.824762"})

    def get_by_name(name: str) -> str:
        match name.lower():
            case "пульсометр":
                return "pulse"
            case "водонагреватель":
                return "voda"
            case _:
                return "unknown"

    async with aiosqlite.connect("message.db") as connection:
        query = """
SELECT subsystem, message, datetime_subsystem, datetime_server
FROM message
ORDER BY subsystem ASC
"""
        async with connection.execute(query) as cursor:
            rows = await cursor.fetchall()
            messages = [{"subsystem": row[0], "message": json.loads(row[1]), "datetime_subsystem": row[2], "datetime_server": row[3]} for row in rows]
            print("\n\n\n")
            print(messages)
            data = {}
            for message in messages:
                sub = message["subsystem"]
                subname = get_by_name(sub)
                data[subname] = message
            print(data)
            print("\n\n\n")
    return {
        "data": data,
        "datetime_server": datetime_server,
    }


@app.post("/api/communicator/")
async def post_api_communicator(request: Request):
    if request.client.host != "127.0.0.1":
        if request.headers.get("Authorization", "") != "Token=token_auth123":
            raise Exception("Access denied")

    await asyncio.sleep(1.0)

    form_data = await request.json()
    print(form_data)
    subsystem = form_data["subsystem"]
    datetime_subsystem = form_data["datetime_subsystem"]
    datetime_server = datetime.datetime.now()
    messages = form_data.get("messages", {})

    async with aiosqlite.connect("message.db") as connection:
        # обновление последней(единственной) строки
        query1 = """
INSERT OR REPLACE INTO message (subsystem, message, datetime_subsystem, datetime_server) 
VALUES (?, ?, ?, ?)
"""
        await connection.execute(query1, (subsystem, json.dumps(messages, ensure_ascii=False), datetime_subsystem, datetime_server))

        # вставка строки
        query2 = """
INSERT INTO message_history (subsystem, message, datetime_subsystem, datetime_server) 
VALUES (?, ?, ?, ?)
"""
        await connection.execute(query2, (subsystem, json.dumps(messages, ensure_ascii=False), datetime_subsystem, datetime_server))
        await connection.commit()

    return {"message": "ok"}


"""

[
{'subsystem': 'водонагреватель', 'message': 
    {'id': 783, 'param1': 54, 'datetime_iot': '2023-11-22 20:24:20.018885'}, 'datetime_subsystem': '2023-11-22 20:24:20.018885', 'datetime_server': '2023-11-22 20:24:21.017175'}, 

{'subsystem': 'пульсометр', 'message':
    {'id': 723, 'param1': 161, 'param2': 232, 'datetime_iot': '2023-11-22 20:24:20.060918'}, 'datetime_subsystem': '2023-11-22 20:24:20.060918', 'datetime_server': '2023-11-22 20:24:21.065217'}
]

{
'voda': 
    {'subsystem': 'водонагреватель', 'message': {'id': 783, 'param1': 54, 'datetime_iot': '2023-11-22 20:24:20.018885'}, 'datetime_subsystem': '2023-11-22 20:24:20.018885', 'datetime_server': '2023-11-22 20:24:21.017175'}, 
'pulse': 
    {'subsystem': 'пульсометр', 'message': {'id': 723, 'param1': 161, 'param2': 232, 'datetime_iot': '2023-11-22 20:24:20.060918'}, 'datetime_subsystem': '2023-11-22 20:24:20.060918', 'datetime_server': '2023-11-22 20:24:21.065217'}
}

"""


@app.post("/api/register/")
async def post_api_register(request: Request):
    await asyncio.sleep(1.0)

    form_data = await request.json()
    print("\n\nform_data: ", form_data)

    return {"data": "Пользователь зарегистрирован!"}


templates = Jinja2Templates(directory="build")


@app.get("/react", response_class=HTMLResponse)
async def react(request: Request):
    headers = {"Cache-Control": "max-age=0"}
    return templates.TemplateResponse("index.html", {"request": request}, headers=headers)
