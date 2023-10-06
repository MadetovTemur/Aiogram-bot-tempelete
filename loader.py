from aiogram import Bot
from aiogram import Dispatcher # Router
from aiogram.fsm.storage.memory import MemoryStorage
import config

storage = MemoryStorage()
dp = Dispatcher(storage=storage)
bot = Bot(config.BOT_TOKEN, parse_mode=config.PARS_MODE_BOT, protect_content=config.PROTECT_CONTENT)
