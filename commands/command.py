from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
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

from aiogram.types import InputFile

@command_router.callback_query(F.data.startswith('guide'))
async def guide_handler(callback: CallbackQuery):
    guide_steps = [
        ("Откройте чат вашей группы в Telegram.", 'images/photo_2025-01-06 17.22.12.jpeg'),
        ("Нажмите на название группы в верхней части экрана, чтобы открыть настройки группы.", 'images/photo_2025-01-06 17.22.10.jpeg'),
        ("Прокрутите вниз и нажмите 'Добавить участника'.", 'images/photo_2025-01-06 17.22.06.jpeg'),
        ("Найдите бота, используя его имя пользователя (например, @your_bot_username).", 'images/photo_2025-01-06 17.22.14.jpeg'),
        ("После добавления бота вы должны повысить бота до администратора, затем надо настроить его права и параметры.", 'images/photo_2025-01-06 17.22.18.jpeg'),
        ("Это изображение показывает конечный результат после добавления бота.", 'images/photo_2025-01-06 17.22.21.jpeg'),
    ]
    
    for step_text, image_path in guide_steps:
        await callback.message.answer(step_text)
        image = FSInputFile(image_path)
        await callback.message.answer_photo(photo=image)