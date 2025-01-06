from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message
import logging
from commands.keyboards import *

command_router = Router()

def keywords(file_path: "/Users/nurislam/Desktop/projects/telegram_bots/ban_word_bot/list_of_badwords.txt"):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file]

KEYWORDS = keywords("list_of_badwords.txt")

@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("You started the bot!", reply_markup = kb)


@command_router.message(F.text)
async def delete_keyword_messages(message: Message):
    for keyword in KEYWORDS:
        if keyword in message.text.lower():
            await message.delete()