from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
import logging
from commands.keyboards import *

command_router = Router()

def keywords(file_path: "/Users/nurislam/Desktop/projects/telegram_bots/ban_word_bot/list_of_badwords.txt"):
    with open(file_path, 'r') as file:
        return [line.strip().lower() for line in file]

KEYWORDS = keywords("list_of_badwords.txt")

@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("""Вы активировали бота. Этот бот удаляет все матершинные слова в чате группы или канала. \n 
    Если хотите добавить бота к себе в группу следуйте по инструкции""" , reply_markup = await inline_buttons())


@command_router.message(F.text)
async def delete_keyword_messages(message: Message):
    for keyword in KEYWORDS:
        if keyword in message.text.lower():
            await message.delete()

@command_router.callback_query(F.data.startswith('help'))
async def help_handler(callback: CallbackQuery):
    await callback.message.answer("Для дополнительной помощи обращайтесь сюда @jnrslm3 ")