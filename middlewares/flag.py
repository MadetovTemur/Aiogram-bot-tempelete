from aiogram import BaseMiddleware
from aiogram.types import Message
from typing import (Dict, Any, Callable, Awaitable)
from aiogram.dispatcher.flags import get_flag
from aiogram.utils.chat_action import ChatActionSender

class ChatActionsMiddleware(BaseMiddleware):
  def __init__(self, bot) -> None:
    self.bot = bot

  async def __call__(self,
                     handler: Callable[[Message, Dict[str, Any] ], Awaitable[Any] ],
                     event: Message,
                     data: Dict[str, Any]
                     ) -> Any :
    chat_action = get_flag(data, 'chat_action')
    if not chat_action:
      return await handler(event, data)
    async with ChatActionSender(action=chat_action, chat_id=event.chat.id, bot=self.bot):
      return await handler(event, data)
