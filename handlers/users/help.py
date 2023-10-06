from aiogram import types
from aiogram.filters import Command


from loader import dp



@dp.message(Command('help'))
async def bot_help(msg: types.Message):
    text = ("Qanday yordam kerak?",
            "Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam",
            "/payment - payment",
            "/inlayin - inlayin")

    await msg.answer("\n".join(text))


# @dp.message()
# async def bot_contact( msg: types.Message):
#     await msg.answer("Kantakt")
