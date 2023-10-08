import json
from aiogram import types, Bot
from aiogram.types import InputMediaPhoto, InputMediaVideo, FSInputFile
from aiogram.filters import Command
from aiogram.enums.input_media_type import InputMediaType
from aiogram.utils.chat_action import ChatActionSender

from loader import dp, bot


@dp.message(Command('audio'))
async def bot_aiodio(msg: types.Message):
  audio = FSInputFile(path='auio.mp3', filename='a.mp3')
  await msg.answer_audio(audio=audio)


@dp.message(Command('document'))
async def bot_doc(msg: types.Message):
  doc = FSInputFile(path='auio.docx')
  await msg.answer_document(document=doc, caption='It"s doc')


@dp.message(Command('photo'))
async def bot_photo(msg: types.Message):
  doc = FSInputFile(path='f.jpg')
  await msg.answer_photo(photo=doc, caption='It"s phoyo')


@dp.message(Command('document'))
async def bot_media(msg: types.Message):
  async with ChatActionSender.upload_voice(chat_id=msg.chat.id, bot=bot):
    photo1 = InputMediaPhoto(type=InputMediaType.PHOTO, media=FSInputFile(path='fr.jpg'), has_spoiler=True)
    vidio = InputMediaVideo(type=InputMediaType.VIDEO, media=FSInputFile(path='fr.mp4'), has_spoiler=True)

  await msg.answer_media_group(media=[photo1, vidio])
