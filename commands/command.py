from aiogram import Router, F
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery, FSInputFile
import logging
from commands.keyboards import *
from databases.querysets import *



command_router = Router()


@command_router.message(Command("start"))
async def start_handler(message: Message):
    await message.answer("""Добро пожаловать! Вы успешно активировали бота. Этот бот автоматически удаляет матершинные слова из сообщений в чате группы или канала. 

        Если вы хотите добавить бота в свою группу, пожалуйста, следуйте инструкции ниже.""" , reply_markup = await inline_buttons())

@command_router.message(F.text)
async def delete_keyword_messages(message: Message):
    
        

@command_router.callback_query(F.data.startswith('help'))
async def help_handler(callback: CallbackQuery):
    await callback.message.answer("Для дополнительной помощи обращайтесь сюда @jnrslm3 ")

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