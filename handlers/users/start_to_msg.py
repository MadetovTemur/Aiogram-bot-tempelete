from aiogram import types, Bot
from aiogram.filters import  CommandStart


from loader import dp, txt
from config import ADMINS
from utils.bot_commands import set_default_commands



@dp.message(CommandStart())
async def bot_start(msg: types.Message, bot :Bot):
  await set_default_commands()
  await msg.answer(f"Привет как дела ?, {txt.italic(msg.from_user.full_name)} !")  # type: ignore
