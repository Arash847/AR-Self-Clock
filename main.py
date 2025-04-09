import asyncio
from telethon import TelegramClient
from telethon.sessions import SQLiteSession
from telethon.tl.functions.account import UpdateProfileRequest
from datetime import datetime
import pytz
import time
from keep_alive import keep_alive

# اطلاعات اتصال
api_id = 24711413        # جایگزین کن
api_hash = '10e258eafb4f66acf2f829cd3819dc7f'  # جایگزین کن

# استفاده از فایل session آپلودشده
session_file = "arash_session.session"
client = TelegramClient(SQLiteSession(session_file), api_id, api_hash)

# bold کردن ساعت
def bold_numbers(text):
    bold_digits = {
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯',
        '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳',
        '8': '𝟴', '9': '𝟵', ':': ':'
    }
    return ''.join(bold_digits.get(char, char) for char in text)

# اجرای دقیق رأس هر دقیقه
def wait_until_next_minute():
    now = time.time()
    wait = 60 - (now % 60)
    time.sleep(wait)

async def update_clock():
    await client.connect()
    if not await client.is_user_authorized():
        print("خطا: session معتبر نیست.")
        return
    while True:
        tehran_time = datetime.now(pytz.timezone("Asia/Tehran")).strftime("%H:%M")
        bold_time = bold_numbers(tehran_time)
        new_name = f".𝑨𝒓𝒂𝒔𝒉𝑹. {bold_time}"
        try:
            await client(UpdateProfileRequest(first_name=new_name))
            print("آپدیت شد:", new_name)
        except Exception as e:
            print("خطا:", e)
        wait_until_next_minute()

keep_alive()

if __name__ == "__main__":
    asyncio.run(update_clock())
