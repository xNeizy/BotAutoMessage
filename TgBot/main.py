from config import token
import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.types import Message

bot = Bot(token)
dp = Dispatcher()

@dp.message()
async def text(message: Message):
    if message.chat.type == "supergroup":
        await message.reply(f"⚡@{message.from_user.username}, мы переехали в новый канал: @channel\n по этому отменяй подписку от этого канала и подписывайся на новый!")
    else:
        await message.reply(f"⚠Работаю только в каналах! (группах)")
        
    

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())