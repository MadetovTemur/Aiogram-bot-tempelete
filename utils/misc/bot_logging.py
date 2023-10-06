import logging, time, os, sys


async def bot_log() -> None:
  # | %(pathname)s  %(module)s %(levelname)s  (%(filename)s)
  FORMAT = '%(asctime)s | %(msecs)d ms | %(name)s' \
    '| %(funcName)s | %(module)s | (%(lineno)d - %(message)s) (%(process)d %(processName)s) | %(thread)d'
  logging.basicConfig(level=logging.NOTSET,
                        filename=f'{os.getcwd()}/utils/log/{time.strftime("%H-%d-%m-%y")}.log',
                        filemode='a',
                        format=FORMAT,
                        datefmt=time.strftime('%d.%m.%y %H:%M:%S'),
                        encoding='utf-8',
                        # errors=sys.exit()
                        )
