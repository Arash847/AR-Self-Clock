import asyncio
import os
import time
from telethon import TelegramClient
from telethon.sessions import StringSession
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz
from keep_alive import keep_alive

api_id = 24711413  # جایگزین کن با api_id واقعی
api_hash = '10e258eafb4f66acf2f829cd3819dc7f'  # جایگزین کن با api_hash واقعی

# رشته session که بهم دادی:
session_string = "1BJWap1sBu12ONB2jbGf0dlSirrz1usmTlHD9tvniU75VOrDZ6NnluE825DIXexmRwrgAEwTp5qshVqeggQuEWbA9abh9U1ZenozlsiRVbegOo6b3BPzyL3LrzC_6mUDopc8YIfo7QUxCDj6AtPvCAvMD-JVu6FnYIBqeFzXKQJXCocveP-6JcrEjpnC-KN6ZDIhvwcLgXLK49U1ox3mjeOrTr-wi9DcCejpsHzMGwsuAN1GCJydjftLHK0wiqomdfudA2oB-QMPSrLxdUG9-UL0eXQufgCdiIc1Ixww-SWcglyKgpyzNZ30CXYm-_O7UMDF4SOICe6trePJVhz9WxecLRWsBXGM="

client = TelegramClient(StringSession(session_string), api_id, api_hash)

def bold_numbers(text):
    bold_digits = {
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯',
        '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳',
        '8': '𝟴', '9': '𝟵', ':': ':'
    }
    return ''.join(bold_digits.get(char, char) for char in text)

def wait_until_next_minute():
    now = time.time()
    wait = 60 - (now % 60)
    time.sleep(wait)

async def update_clock():
    await client.connect()
    if not await client.is_user_authorized():
        print("خطا: session معتبر نیست!")
        return
    while True:
        tehran_time = datetime.now(pytz.timezone("Asia/Tehran")).strftime("%H:%M")
        bold_time = bold_numbers(tehran_time)
        new_name = f".𝑨𝒓𝒂𝒔𝒉𝑹. {bold_time}"
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print("به‌روزرسانی شد:", new_name)
        except Exception as e:
            print("خطا:", e)
        wait_until_next_minute()

keep_alive()

if __name__ == "__main__":
    asyncio.run(update_clock())
