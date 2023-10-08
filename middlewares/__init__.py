from aiogram.utils.chat_action import ChatActionMiddleware
from loader import dp, bot
from .counter import CounterMiddleware
from .office import OfficeMiddleware



if __name__ == 'middlewares':
  # dp.update.middleware(OfficeMiddleware())
  dp.message.middleware(ChatActionMiddleware())
  dp.message.middleware(OfficeMiddleware())
  dp.message.middleware(CounterMiddleware())
