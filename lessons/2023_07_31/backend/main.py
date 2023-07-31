"""Наше приложение"""

import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()


@app.get("/")  # URL (ссылка)
def root():  # VIEW (контроллер)
    """Рут"""
    return {"message": "Hello World"}


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


if __name__ == "__main__":
    # 127.0.0.1:8000/docs
    # 127.0.0.1:8000/redoc
    uvicorn.run(app, host="127.0.0.1", port=8000)
