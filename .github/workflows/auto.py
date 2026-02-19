import os
import asyncio
import random
from telethon import TelegramClient
from telethon.sessions import StringSession

# GitHub Secrets
api_id = int(os.environ["API_ID"])
api_hash = os.environ["API_HASH"]
session_str = os.environ["SESSION"]
alert_chat = os.environ.get("ALERT_CHAT", "Otavaliyev_M")

# Botlar va sizning profilingiz
targets = [
    "Transcript_robot", "SHodlikAIbot", "Hammaga_javobot", 
    "Longmanrobot", "teacher_tutorbot", "TTSpro_robot", 
    "Otavaliyev_M" # Sizga ham yozadi
]

# Random so'zlar
words = ["salom", "qalaysiz", "ishlar yaxshimi", "start", "python", "online", "ready", "ok"]

# Siz aytgan aniq intervallar (daqiqalarda)
intervals = [45, 50, 55, 47, 62, 58]

client = TelegramClient(StringSession(session_str), api_id, api_hash)

async def send_alert(msg):
    try:
        await client.send_message(alert_chat, f"🚨 **MUAMMO YUZ BERDI:**\n\n`{msg}`")
    except:
        pass

async def main():
    try:
        await client.start()
        
        # Ro'yxatdan bitta vaqtni tanlab, o'sha daqiqa davomida kutamiz
        wait_min = random.choice(intervals)
        print(f"Tanlangan interval: {wait_min} daqiqa. Kutish boshlandi...")
        await asyncio.sleep(wait_min * 60)

        for target in targets:
            random_word = random.choice(words)
            try:
                await client.send_message(target, random_word)
                print(f"✅ {target} ga yuborildi.")
                await asyncio.sleep(random.randint(5, 10)) # Spamdan himoya
            except Exception as e:
                await send_alert(f"{target} ga yozishda xato: {str(e)}")

    except Exception as e:
        await send_alert(f"Bot to'liq to'xtadi: {str(e)}")
    finally:
        await client.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
    
