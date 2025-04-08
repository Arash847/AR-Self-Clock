from telethon import TelegramClient, functions, types
from datetime import datetime
import pytz
import asyncio
import os

# Your API ID and Hash from environment variables
api_id = os.getenv('API_ID')
api_hash = os.getenv('API_HASH')

# Your phone number from environment variable
phone_number = os.getenv('PHONE_NUMBER')

# Function to get current time in Tehran timezone
def get_tehran_time():
    tehran_tz = pytz.timezone('Asia/Tehran')
    return datetime.now(tehran_tz).strftime('%H:%M')

async def update_profile_name():
    # Create the client and connect
    client = TelegramClient('session_name', api_id, api_hash)
    await client.start(phone_number)

    while True:
        current_time = get_tehran_time()
        new_name = f".𝑨𝒓𝒂𝒔𝒉𝑹. {current_time}"
        await client(functions.account.UpdateProfileRequest(
            first_name=new_name
        ))
        await asyncio.sleep(60)  # Wait for 1 minute

if __name__ == '__main__':
    asyncio.run(update_profile_name())
