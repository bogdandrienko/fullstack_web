"""Наше приложение"""
import os

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import HTMLResponse, RedirectResponse
from starlette.staticfiles import StaticFiles
from starlette.templating import Jinja2Templates

app: FastAPI = FastAPI(
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
    StaticFiles(directory="react/build/static"),
    name="static",
)
app.mount(
    "/media",
    StaticFiles(directory="media"),
    name="media",
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "localhost:3000",
        "http://127.0.0.1:3000",
        "127.0.0.1:3000",
        "http://127.0.0.1:8000",
        "127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
templates = Jinja2Templates(directory=os.path.join(os.path.dirname(__file__), ".."))


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    """Home page"""
    try:
        return templates.TemplateResponse(
            "backend/react/build/index.html", {"request": request}
        )
    except Exception as error:
        return templates.TemplateResponse(
            "backend/templates/error.html",
            {"request": request, "error": str(error.__str__)},
        )


@app.get("/1")  # URL (ссылка)
def root():  # VIEW (контроллер)
    """Рут"""
    return {"message": "Hello World"}


@app.get("/api/get_todos")
def get_todos():
    return {"message": "Hello Никита"}


@app.get("/users/{user_id}")  # path parameter
async def get_users(user_id: int = 1):  # user_id: int = 10   # required
    """path parameter"""

    return f"user_id: {user_id}"


@app.get("/trades")
async def get_trades(offset: int, limit: int = 10):  # query parameter
    # async def get_trades(commons: dict = Depends(common_parameters)):  # often query and path parameters
    # data = [x for x in range(1, 1000)]
    # return data[offset:][:limit]
    return f"OK{offset}{limit}"  # interpolation `${}`


class Trade(BaseModel):
    id: int
    user_id: int
    currency: str = Field(max_length=10)
    side: str
    price: float = Field(ge=0)
    amount: float
    # deg: Degree | None = []


@app.post("/trades", response_model=dict[str, int | list[Trade]])
async def add_trades(trades: list[Trade]):  # Pydantic
    # {..."amount": "ошибочное значение"} == 422, Unprocessable Entity
    # {..."price": -100} == 422, Unprocessable Entity
    # {..."currency": "111111111111111111111111111"} == 422, Unprocessable Entity
    # ...
    data = [{"example": None}]
    data.extend(trades)
    return {"status": 200, "data": data}


@app.get("/{path:path}", response_class=RedirectResponse)
async def default(request: Request, path: str):
    print(f"Path '{path}' is empty!")
    return RedirectResponse(url=app.url_path_for("home"), status_code=303)


if __name__ == "__main__":
    # 127.0.0.1:8000/docs
    # 127.0.0.1:8000/redoc
    uvicorn.run(app, host="127.0.0.1", port=8000)
