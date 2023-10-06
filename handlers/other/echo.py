from aiogram import types, Bot, F
import json


from loader import dp
from keyboards.inline import selective



@dp.message(F.photo)
async def get_photo(msg: types.Message, bot: Bot):
  await msg.answer("Siz rasim yubordingiz")
  file = await bot.get_file(msg.photo[-1].file_id) # type: ignore
  # await bot.download_file(file.file_path, 'phot.jpg')


@dp.message(F.text == 'json')
async def bot_salom(msg: types.Message):
  to_msg = json.dumps(msg.dict(), default=str)
  await msg.answer(to_msg, reply_markup=selective) # type: ignore


@dp.message()
async def bot_echo(msg: types.Message):
    await msg.answer(msg.text) # type: ignore
