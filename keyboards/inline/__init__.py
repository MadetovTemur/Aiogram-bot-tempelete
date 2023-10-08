from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from utils.callbackdate import InlayinCallbacks



selective = InlineKeyboardMarkup(inline_keyboard=[
  [
    InlineKeyboardButton(text='Кнопкий 1', callback_data='btn'),
    InlineKeyboardButton(text='Google', url='https://google.com')
  ]
])

def info_inlayin():
  btn = InlineKeyboardBuilder()
  btn.button(text='Callback class', callback_data=InlayinCallbacks(model='Std', price='cs'))
  btn.adjust(1)
  return btn.as_markup()
