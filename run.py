import logging

import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot, Dispatcher, F
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.enums import ContentType
from app.handlers.user import user
from app.kassa.kassa import order_consult, pre_checkout_query, successful_payment


async def main():
    load_dotenv()
    bot = Bot(token=os.getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()
    dp.include_routers(user)
    
    
    dp.pre_checkout_query.register(pre_checkout_query)
    # dp.message.register(successful_payment, F.content_type == ContentType.SUCCESSFUL_PAYMENT) 
    
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())

    

# Запускаем через терминал
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Бот отключен")