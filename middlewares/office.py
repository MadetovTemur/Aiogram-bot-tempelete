from datetime import datetime
from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import (Dict, Any, Callable, Awaitable)


class OfficeMiddleware(BaseMiddleware):
  def __init__(self) -> None:
    self.counter = 0
  async def office_day(self, weekday: list[int], hour: list[int]) -> bool:

    return datetime.now().weekday() in weekday and datetime.now().hour in hour

  async def __call__(self,
                     handler: Callable[[Message, Dict[str, Any] ], Awaitable[Any] ],
                     event: Message,
                     data: Dict[str, Any]
                     ) -> Any :
    if await self.office_day(weekday=[0, 1, 2, 3, 4, 5, 6], hour=[i for i in range(4, 22) ]):
      return await handler(event, data)

    to_msg = 'Времия работа бота:\n Пн-Пт с 5 до 23. \nПриходите в рабоче часы.'
    await event.answer(to_msg)
