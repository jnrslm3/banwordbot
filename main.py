import asyncio
import sys, logging
from aiogram import Bot, Dispatcher
from config import TOKEN
from commands.command import command_router
from databases.models import *
from databases.querysets import *

async def main():
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(command_router)
    await dp.start_polling(bot)
    # await create_tables()
    # await add_word()

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
