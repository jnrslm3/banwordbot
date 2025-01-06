from sqlalchemy import String, Integer, Column, ForeignKey, Date, create_engine, Text, Table
from sqlalchemy.orm import relationship, sessionmaker, Mapped, mapped_column, DeclarativeBase
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker , AsyncAttrs



class Base(AsyncAttrs,DeclarativeBase):
    pass

class SwearWords(Base):
    __tablename__ = "words"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    word : Mapped[str] = mapped_column(String(255), nullable=False)

from config import MYSQL_URL
engine = create_async_engine(MYSQL_URL, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)