import logging

from loader import bot
from config import ADMINS


async def on_startup_notify():
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Bot faollashdi!")
        except Exception as err:
            logging.error(err)

async def on_stop_notify():
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Bot ishdan toxdadi!")
        except Exception as err:
            logging.error(err)
