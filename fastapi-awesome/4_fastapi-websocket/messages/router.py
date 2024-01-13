from typing import List
from fastapi import APIRouter, WebSocket, WebSocketDisconnect, Depends
from sqlalchemy import Result, desc
from sqlalchemy import insert, select
from sqlalchemy.orm import Session
from database import async_session_maker, get_async_session
from . import schemas, models


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def send_personal_message(self, message: str, websocket: WebSocket):
        await websocket.send_text(message)

    async def broadcast(self, message: str, add_to_db: bool):
        if add_to_db:
            await self.add_messages_to_database(message)
        for connection in self.active_connections:
            await connection.send_text(message)

    @staticmethod
    async def add_messages_to_database(message: str):
        async with async_session_maker() as session:
            query = insert(models.Message).values(text=message)
            await session.execute(query)
            await session.commit()


router = APIRouter()
manager = ConnectionManager()


@router.get("/", response_model=list[schemas.Message])
async def read_messages(async_session: Session = Depends(get_async_session)):
    result: Result = await async_session.execute(select(models.Message).order_by(desc(models.Message.created_at)).limit(5))
    return result.scalars()


@router.websocket("/ws/{client_id}")
async def websocket_endpoint(websocket: WebSocket, client_id: int):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.broadcast(f"Client #{client_id} says: {data}", add_to_db=True)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
        await manager.broadcast(f"Client #{client_id} left the chat", add_to_db=False)
