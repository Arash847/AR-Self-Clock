from telethon.sync import TelegramClient
from telethon.tl.functions.account import UpdateProfile
from datetime import datetime
import asyncio
import pytz
from keep_alive import keep_alive

api_id = 24711413  # جایگزین با api_id خودت
api_hash = '10e258eafb4f66acf2f829cd3819dc7f'  # جایگزین با api_hash خودت
phone = '+989335398546'  # شماره‌ات با +98

client = TelegramClient('session', api_id, api_hash)

async def update_clock():
    await client.start(phone=phone)
    while True:
        tehran_time = datetime.now(pytz.timezone('Asia/Tehran')).strftime('%H:%M')
        display_name = f".𝑨𝒓𝒂𝒔𝒉𝑹. {tehran_time}"
        await client(UpdateProfile(first_name=display_name))
        await asyncio.sleep(60)

keep_alive()

with client:
    client.loop.run_until_complete(update_clock())
