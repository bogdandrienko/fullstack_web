import aioredis
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from config import DB_SQLITE_PATH
from sqlalchemy import MetaData

SQLALCHEMY_DATABASE_URL = f"sqlite+aiosqlite:///{DB_SQLITE_PATH}"
async_engine = create_async_engine(SQLALCHEMY_DATABASE_URL, echo=False)
SessionLocal = sessionmaker(async_engine, expire_on_commit=False, class_=AsyncSession)
Base = declarative_base()
metadata = MetaData()
# redis = aioredis.from_url("redis://localhost:6379", decode_responses=True)


async def get_async_session():
    async_session = SessionLocal()
    try:
        yield async_session
    finally:
        await async_session.close()
