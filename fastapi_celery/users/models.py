from __future__ import annotations

from sqlalchemy import Column, Integer, String

from fastapi_celery.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(128), unique=True, nullable=False)
    email = Column(String(128), unique=True, nullable=False)

    def __init__(self, username, email, *args, **kwargs):
        self.username = username
        self.email = email

    @classmethod
    def create(cls, session, **kwargs) -> User:
        obj_instantiate = cls(**kwargs)
        session.add(obj_instantiate)
        return obj_instantiate
