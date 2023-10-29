from sqlalchemy import Column, Integer, String

from app.database import Base


class Messages(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True)
    message = Column(String)
