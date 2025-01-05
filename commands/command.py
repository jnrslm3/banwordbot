from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import logging
from databases.querysets import KEYWORDS

command_router = Router()


@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("You started the bot!")


@command_router.message(F.text)
async def delete_keyword_messages(message: Message):
    for keyword in KEYWORDS:
        if keyword in message.text.lower():
            try:
                await message.delete()
                logging.info(f"Deleted message: {message.text}")
            