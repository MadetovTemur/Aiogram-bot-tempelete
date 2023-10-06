from aiogram import types


async def set_default_commands():
  commands = [
    types.BotCommand(command="start",  description="Botni qayta ishga tushurish"),
    types.BotCommand(command="help", description="Yordam"),
  ],
  return commands
