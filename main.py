from telethon import TelegramClient, events
import asyncio

# Your Telegram API credentials
api_id = 28381521
api_hash = 'bfdeae68187ece42ae8fabc3b9e87737'
bot_username = 'MyMusicBot321_bot'

# Keywords to trigger the forward
keywords = ['space', 'nurillo', 'unit', 'stephan', 'jason', 'bob', 'eld',
            'danyorovic', 'john', 'anvarbek', 'islom', 'harry', 'ilkhamov',
            'ken', 'alex', 'safety', 'load', 'eta', 'cargo']

# Create client
client = TelegramClient('session_name', api_id, api_hash)

# Message handler
@client.on(events.NewMessage(incoming=True))
async def handler(event):
    message_text = event.raw_text.lower()
    if any(keyword in message_text for keyword in keywords):
        await client.send_message(bot_username, f'🔔 Triggered: {event.raw_text}')

# Start client
client.start()
print("✅ Script running. Watching for messages...")

asyncio.get_event_loop().run_forever()
