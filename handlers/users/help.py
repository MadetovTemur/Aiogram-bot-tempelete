from aiogram import types
from aiogram.filters import Command

from loader import dp
from filters.iscon import IsTrueContact
from keyboards.default import btn1
from keyboards.inline import info_inlayin





@dp.message(Command('help'))
async def bot_help( msg: types.Message):
    text = ("Qanday yordam kerak?",
            "Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/inlayin - inlayin")

    await msg.answer("\n".join(text), reply_markup=btn1)

@dp.message(Command('inlayin'))
async def bot_inlayin(msg: types.Message):
    await msg.answer("Inlayin button", reply_markup=info_inlayin())


@dp.message(IsTrueContact())
async def bot_contact( msg: types.Message):
    await msg.answer("Kantakt")
