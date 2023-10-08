import sys
from aiogram import types
from aiogram.filters import Command


from loader import dp, txt
from config import BOT_COMMADNS


@dp.message(Command('help'), flags={'chat_action': "typing"})
async def bot_help(msg: types.Message, counter: str):
  to_msg = ""
  for commands in BOT_COMMADNS['uz']:
    to_msg += f"/{txt.bold(commands[0])} -- {commands[1]} \n"
  await msg.answer(to_msg)


@dp.message(Command('count'))
async def bot_count(msg: types.Message, counter: str):
  await msg.answer(f"{counter}")
