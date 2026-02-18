import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

# GitHub Secrets orqali olinadigan ma'lumotlar
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]

# Botlar ro'yxati
bots = [
    "Transcript_robot",
    "SHodlikAIbot",
    "Hammaga_javobot",
    "Longmanrobot",
    "teacher_tutorbot",
    "TTSpro_robot"
]

# 50 ta random so'zlar ro'yxati
words = [
    "salom", "qalaysiz", "ishlar yaxshimi", "nima gap", "hello", "hi", "test", "ping", 
    "start", "word", "random", "ok", "run", "python", "telegram", "bot", "coding", 
    "uzbekistan", "tashkent", "namangan", "andijon", "fargona", "samarqand", "buxoro", 
    "xiva", "termiz", "navoiy", "jizzax", "guliston", "nukus", "dunyo", "quyosh", 
    "osmon", "yulduz", "oy", "kitob", "ilm", "maktab", "universitet", "dars", 
    "ustoz", "shogird", "omad", "baxt", "shodlik", "tabassum", "quvonch", "mehr", 
    "do'st", "aka", "uka", "opa", "singil"
]

# Xato haqida xabar boradigan user
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")

# Tuzatilgan qism: StringSession ishlatilgan
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def send_alert(msg):
    try:
        await client.send_message(alert_chat, f"🚨 XATO:\n{msg}")
    except:
        pass

async def main():
    # Sessiyani boshlash
    await client.start()
    print("Sessiya muvaffaqiyatli ishga tushdi!")

    for bot in bots:
        try:
            text = random.choice(words)
            await client.send_message(bot, text)
            print(f"Yuborildi -> {bot}: {text}")

            # Random delay (anti-ban uchun 15 dan 40 soniyagacha)
            await asyncio.sleep(random.randint(15, 40))

        except Exception as e:
            err = f"{bot} -> {e}"
            print("Xato yuz berdi:", err)
            await send_alert(err)

if __name__ == "__main__":
    asyncio.run(main())
