import logging, asyncio, sys

import handlers, utils
from loader import dp, bot




async def start() -> None:
  global bot, dp
  await utils.misc.bot_log()

  # await dp.startup(utils.notify_admins.on_startup_notify()) # type: ignore
  # await dp.shutdown(utils.notify_admins.on_stop_notify()) # type: ignore

  try:
    await dp.start_polling(bot)
  except(Exception) as err:
    logging.error(err)
    sys.exit()
  finally:
    # await bot.session.close()
    sys.exit()



if __name__ == "__main__":
  asyncio.run(start())
