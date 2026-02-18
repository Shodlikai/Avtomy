import os
import asyncio
import random
from telethon import TelegramClient

api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session = os.environ["SESSION"]

# Botlar
bots = [
    "Transcript_robot",
    "SHodlikAIbot",
    "Hammaga_javobot",
    "Longmanrobot",
    "teacher_tutorbot",
    "TTSpro_robot"
]

# Random so‘zlar (xohlasangiz ko‘paytiring)
words = [
    "salom", "hello", "test", "ping", "start",
    "word", "random", "hi", "ok", "run"
]

# Xato signal boradigan user
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")

client = TelegramClient(session, api_id, api_hash)

async def send_alert(msg):
    try:
        await client.send_message(alert_chat, f"🚨 XATO:\n{msg}")
    except:
        pass

async def main():
    await client.start()

    for bot in bots:
        try:
            text = random.choice(words)
            await client.send_message(bot, text)
            print(f"Yuborildi -> {bot}: {text}")

            # Random delay (anti-ban)
            await asyncio.sleep(random.randint(10, 25))

        except Exception as e:
            err = f"{bot} -> {e}"
            print("Xato:", err)
            await send_alert(err)

asyncio.run(main())