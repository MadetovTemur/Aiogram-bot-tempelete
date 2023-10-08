import logging, asyncio, sys
from aiogram import types
from loader import dp, bot




async def start() -> None:
  import middlewares, handlers, utils
  global bot, dp
  await utils.misc.bot_log()


  try:
    await dp.start_polling(bot)
  except(Exception) as err:
    logging.error(err)
    sys.exit()
  finally:
    logging.info('Finished to bot')
    await bot.delete_my_commands(scope=types.BotCommandScopeDefault())
    sys.exit()




if __name__ == "__main__":
  asyncio.run(start())
