import asyncio
from telethon import TelegramClient, functions
from datetime import datetime
import pytz
import time
from keep_alive import keep_alive  # برای فعال موندن رپل

# مشخصات حساب (حتماً جایگزین کن)
api_id = 24711413      # <-- آیدی API خودت
api_hash = '10e258eafb4f66acf2f829cd3819dc7f'  # <-- هش API خودت
session_name = 'clock_selfbot'
base_name = ".𝑨𝒓𝒂𝒔𝒉𝑹."

# فونت بولد برای اعداد ساعت
def bold_numbers(text):
    bold_digits = {
        '0': '𝟬', '1': '𝟭', '2': '𝟮', '3': '𝟯',
        '4': '𝟰', '5': '𝟱', '6': '𝟲', '7': '𝟳',
        '8': '𝟴', '9': '𝟵', ':': ':'
    }
    return ''.join(bold_digits.get(char, char) for char in text)

# تأخیر تا شروع دقیق دقیقه بعد
def sleep_until_next_minute():
    now = time.time()
    time_to_wait = 60 - (now % 60)
    time.sleep(time_to_wait)

client = TelegramClient(session_name, api_id, api_hash)

async def main():
    await client.start()
    tehran_tz = pytz.timezone('Asia/Tehran')

    while True:
        now = datetime.now(tehran_tz).strftime("%H:%M")
        bold_time = bold_numbers(now)
        full_name = f"{base_name} {bold_time}"
        try:
            me = await client.get_me()
            last_name = me.last_name or ""
            await client(functions.account.UpdateProfileRequest(
                first_name=full_name,
                last_name=last_name
            ))
            print(f"آپدیت شد: {full_name}")
        except Exception as e:
            print("خطا:", e)

        sleep_until_next_minute()

# اجرای دائمی در رپل
if __name__ == "__main__":
    keep_alive()
    asyncio.run(main())
