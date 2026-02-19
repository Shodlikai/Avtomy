import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

# GitHub Secrets orqali olinadigan ma'lumotlar
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")

# Botlar va profilingiz
targets = [
    "Transcript_robot",
    "SHodlikAIbot",
    "Hammaga_javobot",
    "Longmanrobot",
    "teacher_tutorbot",
    "TTSpro_robot",
    "Otavaliyev_M"
]

# Tasodifiy so'zlar ro'yxati
words = [
    "salom", "qalaysiz", "ishlar yaxshimi", "nima gap", "hello", "hi", "test", "ping", 
    "start", "word", "random", "ok", "run", "python", "telegram", "bot", "coding", 
    "uzbekistan", "tashkent", "namangan", "andijon", "fargona", "samarqand", "buxoro", 
    "xiva", "termiz", "navoiy", "jizzax", "guliston", "nukus", "dunyo", "quyosh", 
    "osmon", "yulduz", "oy", "kitob", "ilm", "maktab", "universitet", "dars", 
    "ustoz", "shogird", "omad", "baxt", "shodlik", "tabassum", "quvonch", "mehr", 
    "do'st", "aka", "uka", "opa", "singil"
]

# Intervallar (daqiqalarda)
intervals = [45, 50, 55, 47, 62, 58]

# ASOSIY TUZATILGAN QISM: session_str maxsus StringSession qavsiga olingan!
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def send_alert(msg):
    """Xatolik yuz bersa xabar beradi"""
    try:
        await client.send_message(alert_chat, f"🚨 MUAMMO YUZ BERDI:\n\n{msg}")
    except Exception as e:
        print(f"Alert yuborishda xato: {e}")

async def main():
    try:
        # Sessiyani boshlash
        await client.start()
        
        # Tanlangan vaqtni kutish
        wait_min = random.choice(intervals)
        print(f"Bot {wait_min} daqiqadan keyin xabar yuborishni boshlaydi...")
        await asyncio.sleep(wait_min * 60)

        for target in targets:
            random_word = random.choice(words)
            try:
                await client.send_message(target, random_word)
                print(f"✅ {target} ga '{random_word}' yuborildi.")
                # Bot bloklanmasligi uchun qisqa pauza (5-10 soniya)
                await asyncio.sleep(random.randint(5, 10))
            except Exception as e:
                err_msg = f"{target} ga yuborishda xato: {str(e)}"
                print(f"❌ {err_msg}")
                await send_alert(err_msg)

    except Exception as e:
        await send_alert(f"Bot butunlay to'xtadi: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    
