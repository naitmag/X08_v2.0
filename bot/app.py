import asyncio

from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

import config

from aiogram import Bot, Dispatcher, types
from handlers import commands

bot = Bot(
    config.SECRET_TOKEN,
    default=DefaultBotProperties(
        parse_mode=ParseMode.HTML
    )
)


async def main():
    dp = Dispatcher()

    dp.include_routers(
        commands.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    print("[+]BOT STARTED")
    asyncio.run(main())
