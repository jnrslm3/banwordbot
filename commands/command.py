from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import logging
from databases.querysets import KEYWORDS

command_router = Router()


@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("You started the bot!")


