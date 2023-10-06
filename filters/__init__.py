from aiogram.filters import Filter
from aiogram.filters import BaseFilter
from aiogram import types
from aiogram.enums.content_type import ContentType


class ContentTypeAnyFilter(Filter):
  def __init__(self, content_typie: str) -> None:
    self.content_typie = content_typie

  async def __call__(self, msg :types.Message) -> bool:
    data = msg.dict()
    try:
      if data[self.content_typie] is None:
        return False
      else:
        return True
    except (Exception) as err:
      print(err)
      exit()






class IsTrueContact(BaseFilter):
  async def __call__(self, msg: types.Message) -> bool:
    try:
      return msg.contact.user_id == msg.from_user.id # type: ignore
    except:
      return False
