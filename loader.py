
from aiogram import Dispatcher # Router
from aiogram.fsm.storage.memory import MemoryStorage


storage = MemoryStorage()
dp = Dispatcher(storage=storage)
