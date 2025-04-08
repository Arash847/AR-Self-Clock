from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfile
from datetime import datetime
import asyncio
import pytz
from keep_alive import keep_alive

api_id = 24711413  # جایگزین کن با api_id خودت
api_hash = '10e258eafb4f66acf2f829cd3819dc7f'  # جایگزین کن با api_hash خودت
phone_number = '+98...'  # شماره موبایلت با +98

client = TelegramClient('session', api_id, api_hash)

async def update_name_clock():
    await client.start(phone=phone_number)
    while True:
        tehran_time = datetime.now(pytz.timezone('Asia/Tehran')).strftime('%H:%M')
        await client(UpdateProfile(first_name=f'ArashR {tehran_time}'))
        await asyncio.sleep(60)

keep_alive()

with client:
    client.loop.run_until_complete(update_name_clock())
