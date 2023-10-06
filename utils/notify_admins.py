import logging

from aiogram import Bot
from config import ADMINS


async def on_startup_notify(bot: Bot):
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Bot faollashdi!")
        except Exception as err:
            logging.exception(err)

async def on_stop_notify(bot: Bot):
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Bot ishdan toxdadi!")
        except Exception as err:
            logging.exception(err)
