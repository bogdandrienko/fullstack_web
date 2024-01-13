import random
from fastapi import FastAPI
from fastapi import Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import JSONResponse
import utils

cache = utils.CacheServer()
app = FastAPI(title="Todo app", description="""Awesome Example of app. 🚀""")

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8000",
        "http://127.0.0.1:8000",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", response_class=JSONResponse)
async def root(request: Request):
    param1 = cache.get("root")
    if param1 is None:
        param1 = random.randint(1, 1000)
        cache.set("root", param1, timeout=5)

    return {"message": param1}
