from aiogram import types

from loader import bot
from config import BOT_COMMADNS



async def set_default_commands():
  set_commands = []

  for command in BOT_COMMADNS['ru']:
    set_commands.append(
      types.BotCommand(command=command[0], description=command[1])
      )

  await bot.set_my_commands(commands=set_commands, scope=types.BotCommandScopeDefault())
