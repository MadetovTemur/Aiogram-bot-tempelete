from aiogram.types import Message, LabeledPrice, PreCheckoutQuery
from aiogram.filters import Command
from loader import dp, bot
import config
from aiogram.enums.content_type import ContentType
from aiogram.enums.currency import Currency
from filters import ContentTypeAnyFilter


# @dp.message(Command('payment'))
async def order(msg: Message):
  # 1111 1111 1111 1026  12/22  cvc 000
  await bot.send_invoice(
    chat_id=msg.chat.id,
    title='Buy',
    description='python telegram bot',
    payload='payment sistem',
    provider_token=config.PAYMENT_TOKEN,
    currency=Currency.UZS,
    prices=[
      LabeledPrice(
        label='Mavhiy soz',
        amount=0
      ),
      LabeledPrice(
        label='MCHJ',
        amount=0
      ),
      LabeledPrice(
        label='MHJ',
        amount=50000
      )
    ],
    max_tip_amount=900000,
    suggested_tip_amounts=[100000, 200000, 300000],
    # start_parameter='googlecom',
    provider_data=None,
    photo_url='https://i.ibb.co/zGw5X0B/image.jpg',
    photo_height=450,
    photo_size=100,
    photo_width=800,
    need_name=True,
    need_phone_number=True,
    need_email=True,
    need_shipping_address=False,

    send_phone_number_to_provider=False,
    send_email_to_provider=False,
    is_flexible=False,

    protect_content=True,
    allow_sending_without_reply=False,
    request_timeout=120
  )


@dp.pre_checkout_query()
async def pre_chekout_query(pre: PreCheckoutQuery):
  print(pre.dict(), end='\n\n')
  await bot.answer_pre_checkout_query(pre.id, ok=True)
  # await bot.answer_pre_checkout_query(pre.id, ok=False, error_message='Tolov otmadi')


# @dp.message(filters=)
async def seccessful_pay(msg: Message):
  to_msg = f'xaridingiz uchun raxmat {str(msg.successful_payment.total_amount)}' # type: ignore
  await msg.answer(to_msg)
  # await msg.answer(msg)












# {
#   'id': '3405547521164488342',
#   'from_user': {'id': 5087883117,
#                 'is_bot': False,
#                 'first_name': 'Madetov_017',
#                 'last_name': None,
#                 'username': 'madetov_017',
#                 'language_code': 'ru',
#                 'is_premium': None,
#                 'added_to_attachment_menu': None,
#                 'can_join_groups': None,
#                 'can_read_all_group_messages': None,
#                 'supports_inline_queries': None},
#   'currency': 'RUB',
#   'total_amount': 50500,
#   'invoice_payload': 'payment sistem',
#   'shipping_option_id': None,
#   'order_info': {
#     'name': 'Temur',
#     'phone_number':
#       '998910980818',
#       'email': 'temur1735@gamil.com',
#       'shipping_address': None
#       }
#   }
