from aiogram import types, Bot
from aiogram.filters import  CommandStart


from loader import dp
from keyboards.default import btn
# from utils.set_bot_commands import set_default_commands



@dp.message(CommandStart())
async def bot_start(msg: types.Message, bot :Bot):
  # await bot.set_my_commands(commands=set_default_commands(), scope=types.BotCommandScopeDefault()) # type: ignore
  await msg.answer(f"Assalomu alaykum, {msg.from_user.full_name} !", reply_markup=btn)  # type: ignore
