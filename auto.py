import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

# 1. GitHub Secrets orqali ma'lumotlarni olish
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")

# 2. Xabar yuboriladigan botlar va sizning profilingiz
targets = [
    "Transcript_robot",
    "SHodlikAIbot",
    "Hammaga_javobot",
    "Longmanrobot",
    "teacher_tutorbot",
    "TTSpro_robot",
    "Otavaliyev_M"
]

# 3. Random so'zlar ro'yxati
words = [
    "salom", "qalaysiz", "ishlar yaxshimi", "nima gap", "hello", "hi", "test", "ping", 
    "start", "word", "random", "ok", "run", "python", "telegram", "bot", "coding", 
    "uzbekistan", "tashkent", "namangan", "andijon", "fargona", "samarqand", "buxoro", 
    "xiva", "termiz", "navoiy", "jizzax", "guliston", "nukus", "dunyo", "quyosh", 
    "osmon", "yulduz", "oy", "kitob", "ilm", "maktab", "universitet", "dars", 
    "ustoz", "shogird", "omad", "baxt", "shodlik", "tabassum", "quvonch", "mehr", 
    "do'st", "aka", "uka", "opa", "singil"
]

# 4. Siz aytgan aniq intervallar (daqiqalarda)
intervals = [45, 50, 55, 47, 62, 58]

# 5. ASOSIY TUZATISH: StringSession qavs ichida bo'lishi shart!
client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def send_alert(msg):
    """Xatolik yuz bersa sizga xabar yuboradi"""
    try:
        await client.send_message(alert_chat, f"🚨 **MUAMMO YUZ BERDI:**\n\n`{msg}`")
    except Exception as e:
        print(f"Alert yuborishda xato: {e}")

async def main():
    try:
        # Sessiyani boshlash
        await client.start()
        
        # Ro'yxatdan bitta vaqtni tanlab, o'sha daqiqa davomida kutamiz
        wait_min = random.choice(intervals)
        print(f"Tanlangan interval: {wait_min} daqiqa. Kutish boshlandi...")
        await asyncio.sleep(wait_min * 60)

        for target in targets:
            # Har bir target uchun alohida random so'z
            random_word = random.choice(words)
            try:
                await client.send_message(target, random_word)
                print(f"✅ {target} ga '{random_word}' yuborildi.")
                # Qisqa tanaffus (spam filtrga tushmaslik uchun)
                await asyncio.sleep(random.randint(5, 10))
            except Exception as e:
                err = f"{target} ga yuborishda xato: {str(e)}"
                print(f"❌ {err}")
                await send_alert(err)

    except Exception as e:
        print(f"Kritik xato yuz berdi: {e}")
        await send_alert(f"Bot to'liq to'xtadi. Xato: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    
