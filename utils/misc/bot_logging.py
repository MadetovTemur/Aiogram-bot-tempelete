import logging, time, os, sys, config


async def bot_log() -> None:

  logging.basicConfig(level=logging.NOTSET,
                        filename=f'{os.getcwd()}/utils/log/{time.strftime("%d-%m-%y")}.log',
                        filemode='a',
                        format=config.FORMAT,
                        datefmt=time.strftime('%d.%m.%y %H:%M:%S'),
                        encoding='utf-8',
                        # errors=sys.exit()
                        )
