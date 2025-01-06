from sqlalchemy import select, delete, update
from sqlalchemy.orm import Session
from databases.models import *

async def add_word():
    async with async_session() as session:
        word = SwearWords(
            word="сука"
        )
        session.add(word)
        await session.commit()

async def all_word():
    async with async_session() as session:
        result = await session.scalars(select(SwearWords))
        return result.all() 


async def get_word_by_partial(word_part):
    async with async_session() as session:
        result = await session.scalars(select(SwearWords).where(
            SwearWords.word.ilike(f"%{word_part}%")))  
        return result.all() 
