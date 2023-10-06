from aiogram.filters.callback_data import CallbackData

class InlayinCallbacks(CallbackData, prefix='tel'):
  model: str
  price: str


# print(InlayinCallbacks(model='e', price='e'))
