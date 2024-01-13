from sanic import Sanic
from sanic.response import text, json

app = Sanic("MyHelloWorldApp")


@app.get("/")
async def index(request):
    return text("<p>Hello, World!</p>")


@app.get("/api")
async def api(request):
    return json({"message": "OK"})
