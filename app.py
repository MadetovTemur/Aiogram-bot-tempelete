import logging, asyncio
from aiogram import Bot
from aiogram.enums import ParseMode

import config, filters, handlers, middlewares, utils
from loader import dp




async def start() -> None:
  logging.basicConfig(level=logging.INFO)

  bot = Bot(config.BOT_TOKEN, parse_mode=ParseMode.HTML, protect_content=True)

  try:
    await dp.start_polling(bot)
  except(Exception) as err:
    logging.info(err)
    exit()
  finally:
    await bot.session.close()



if __name__ == "__main__":
  asyncio.run(start())
