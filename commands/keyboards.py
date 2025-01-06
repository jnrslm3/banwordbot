from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

async def inline_buttons():
    kb = InlineKeyboardBuilder()
    kb.add(InlineKeyboardButton(text="Инструкция", callback_data="guide"))
    kb.add(InlineKeyboardButton(text="Дополненная помощь", callback_data="help"))
    return kb.adjust(1).as_markup()
    