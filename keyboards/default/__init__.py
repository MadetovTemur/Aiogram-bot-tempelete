from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, KeyboardButtonPollType
from aiogram.utils.keyboard import ReplyKeyboardBuilder


btn1 = ReplyKeyboardMarkup(keyboard=[
  [
    KeyboardButton(text='Локатьсия', request_location=True),
    KeyboardButton(text='Контакь', request_contact=True),
    KeyboardButton(text='Викторина', request_poll=KeyboardButtonPollType(type='quiz') )# reguliar
  ]
], resize_keyboard=True, input_field_placeholder='Кнопкий', one_time_keyboard=False)


def get_bilder():
  bild = ReplyKeyboardBuilder()

  bild.button(text='1')
  bild.button(text='4')
  bild.button(text='3')
  bild.button(text='2',request_chat=True)

  bild.adjust(1, 1, 2)
  bild.as_markup(resize_keyboard=True, input_field_placeholder='Кнопкий', one_time_keyboard=False)

  return bild
