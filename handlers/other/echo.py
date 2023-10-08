import json
from aiogram import types, Bot, F
# from filters import ContentTypeAnyFilter
from aiogram.filters import Command

from loader import dp, bot
from keyboards.inline import info_inlayin


@dp.message(Command('inlayin'))
async def bot_inlayin(msg: types.Message):
    await msg.answer("Инлайн кнопка", reply_markup=info_inlayin())


@dp.message(F.photo)
async def get_photo(msg: types.Message, bot: Bot):
  await msg.answer("Ты отправиль фото")
  file = await bot.get_file(msg.photo[-1].file_id) # type: ignore
  await bot.download_file(file.file_path, 'phot.jpg') # type: ignore


@dp.message(F.text == 'json')
async def bot_salom(msg: types.Message):
  to_msg = json.dumps(msg.dict(), default=str)
  await msg.answer(to_msg) # type: ignore


@dp.message(F.text == 'me')
async def bot_me(msg: types.Message):
  me = await bot.me()
  await bot.set_my_description('преветик', language_code='ru')
  to_msg = json.dumps(me.dict(), default=str)
  await msg.answer(to_msg) # type: ignore


@dp.message(F.text)
async def bot_echo(msg: types.Message):
    await msg.answer(msg.text) # type: ignore
