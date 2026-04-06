import asyncio
from pyrogram import Client
import config

# Add this block to fix the Event Loop error
try:
    loop = asyncio.get_event_loop()
except RuntimeError:
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

# Your existing Client initialization
app = Client(
    "my_bot",
    api_id=config.API_ID,
    api_hash=config.API_HASH,
    bot_token=config.BOT_TOKEN
)

if __name__ == "__main__":
    print("Bot is starting...")
    app.run()
