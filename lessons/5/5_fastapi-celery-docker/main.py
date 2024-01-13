import datetime
from fastapi import FastAPI
from fastapi import Request, status
from fastapi.encoders import jsonable_encoder
from fastapi.exceptions import ResponseValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.responses import HTMLResponse
from config import DEBUG

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


# http://127.0.0.1:8000/
# http://127.0.0.1:8000/docs


@app.exception_handler(ResponseValidationError)
async def validation_exception_handler(request: Request, exc: ResponseValidationError):
    print("Error: ", exc.errors())
    return JSONResponse(
        status_code=status.HTTP_422_UNPROCESSABLE_ENTITY,
        content=jsonable_encoder({"error detail": exc.errors()}),
    )


@app.on_event("startup")
async def startup_event():
    if DEBUG:
        print(f"\n.....server STARTED at {datetime.datetime.now()}.....\n\n\n")


@app.on_event("shutdown")
async def shutdown_event():
    if DEBUG:
        print(f"\n\n\n.....server STOPPED at {datetime.datetime.now()}.....\n")


@app.get("/", response_class=HTMLResponse)
async def root(request: Request):
    return "ok"


@app.get("/api", response_class=JSONResponse)
async def api(request: Request):
    return {"message": "ok"}
