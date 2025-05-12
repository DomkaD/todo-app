from collections.abc import AsyncGenerator
from typing import Annotated
from enum import Enum as PyEnum
from fastapi import Depends
from fastapi_users.db import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import Column, String, Enum, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase, relationship

DATABASE_URL = "sqlite+aiosqlite:///./test.db"


class Base(DeclarativeBase):
    pass

class Role(PyEnum):
    PARENT = "parent"
    CHILD = "child"

class User(SQLAlchemyBaseUserTableUUID, Base):
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    role = Column(Enum(Role), nullable=False)
    parent_id = Column(String, nullable=True)


engine = create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)


async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)


DbSession = Annotated[AsyncSession, Depends(get_async_session)]
