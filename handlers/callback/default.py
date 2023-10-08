from aiogram.types import CallbackQuery, Message
from aiogram import F


from loader import dp
from utils.callbackdate import InlayinCallbacks



@dp.callback_query(F.contains('btn'))
# @dp.callback_query(F.data.startswith('btn:'))
async def defoult(call : CallbackQuery):
  await call.answer(text='Ты нажал колбек кнопка', show_alert=True)
  # call.message.answer('Callback query')


@dp.callback_query(InlayinCallbacks.filter())
async def inlayin_defoults(call: CallbackQuery):
  await call.answer(text='Ты нажал колбек кнопка филтиный варианть ', show_alert=True)


@dp.callback_query(InlayinCallbacks.filter(F.model == 'Iphone'))
async def inlayin_defoults2(call: CallbackQuery):
  await call.answer(text='Iphone 16')
