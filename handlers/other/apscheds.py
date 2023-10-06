from loader import bot
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from datetime import datetime, timedelta

async def send_message_start(id):
  await bot.send_message(id, text='10s')

async def send_message_hour(id):
  await bot.send_message(id, text='hour')



scheduler = AsyncIOScheduler(timezone="Europe/Moscow")
scheduler.add_job(send_message_start, trigger='date', run_date=datetime.now() + timedelta(seconds=5) ,
                  kwargs={'id' : 5087883117})

# scheduler.add_job(send_message_hour, trigger='cron', hour=datetime.now().hour, minute=datetime.now().minute + 1,
#                   start_date=datetime.now()),
#                   kwargs={'id' : 5087883117})

scheduler.add_job(send_message_start, trigger='interval', seconds=20, kwargs={'id':5087883117})
scheduler.start()
