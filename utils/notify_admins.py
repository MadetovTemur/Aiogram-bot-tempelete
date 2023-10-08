import logging

from loader import bot, dp
from config import ADMINS

# @dp.startup()
async def on_startup_notify():
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Бот актив !")
        except Exception as err:
            logging.error(err)

# @dp.shutdown()
async def on_stop_notify():
    for admin in ADMINS:
        try:
          await bot.send_message(admin, "Бот остановился !")
        except Exception as err:
            logging.error(err)
