# -*- utf-8 -*-

BOT_ID :int = 6441125092
r"""id Бота """


BOT_TOKEN :str = "6441125092:AAF2TC230WQQksH4Ehvfk2hHHWY-7G5aRl0"
r"""Бот токен"""


ADMINS :list[int] = [6441125092]
r"""Списки админов"""


PARS_MODE_BOT :str = "html"
r"""Парс мод виберите один из вариантов
>>> ['HTML', 'Markdown', 'MarkdownV2']"""


PROTECT_CONTENT :bool = False
r"""Пересылка сообшения из бота"""

# PAYMENT_TOKEN :str = '381764678:TEST:68231'
PAYMENT_TOKEN :str = '1650291590:TEST:1696596531529_I0LctTJ42R3YliGc'
r"""Токен ЮКасса"""


BOT_COMMADNS :dict = {
  "uz": [
    ['start', 'Старть.'],
    ['help', 'Памагите'],
    # ['count', 'count'],
    # ['payment', 'payment'],
    # ['inlayin', 'inlayin'],
    # ['audio', 'Send audio'],
    # ['document', 'Send document'],
    # ['mediagroup', 'send media group'],
    # ['photo', 'send photo'],
    # ['sticker', 'send siker'],
    # ['vidio', 'send vidio'],
    # ['vidio_note', 'send Void'],
    # ['voice', 'send voice'],
  ]
}
r"""Бот камандий"""


# | %(pathname)s  %(module)s %(levelname)s  (%(filename)s)
FORMAT = ('%(asctime)s| %(msecs)dmc|%(name)s' \
    '|%(funcName)s|%(module)s|(%(lineno)d-%(message)s)|(%(process)d:%(processName)s)|%(thread)d')
