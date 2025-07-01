from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup
from dotenv import load_dotenv
import os
from utils.instagram_downloader import download_instagram_post
from utils.acrcloud_recognizer import recognize_audio
from utils.music_downloader import download_song_from_youtube

load_dotenv()

bot = Client(
    "insta_music_bot",
    bot_token=os.getenv("BOT_TOKEN"),
    api_id=int(os.getenv("API_ID")),
    api_hash=os.getenv("API_HASH")
)

@bot.on_message(filters.command("start"))
async def start(_, msg: Message):
    await msg.reply("Assalomu alaykum! Instagram link yoki audio yuboring.")

@bot.on_message(filters.text & filters.private)
async def handle_instagram_url(_, msg: Message):
    if "instagram.com" in msg.text:
        await msg.reply("⏬ Yuklab olinmoqda...")
        path, audio_path = download_instagram_post(msg.text)
        await msg.reply_document(path)

        if audio_path:
            result = recognize_audio(audio_path)
            if result:
                buttons = [
                    [InlineKeyboardButton(f"🎵 {res['title']} - {res['artist']}", callback_data=f"dl|{res['title']} {res['artist']}")]
                    for res in result
                ]
                await msg.reply("Tanlang", reply_markup=InlineKeyboardMarkup(buttons))
            else:
                await msg.reply("Musiqa topilmadi.")

@bot.on_message(filters.audio | filters.voice)
async def handle_voice(_, msg: Message):
    await msg.download("temp_audio.ogg")
    result = recognize_audio("temp_audio.ogg")
    if result:
        buttons = [
            [InlineKeyboardButton(f"🎵 {res['title']} - {res['artist']}", callback_data=f"dl|{res['title']} {res['artist']}")]
            for res in result
        ]
        await msg.reply("Tanlang", reply_markup=InlineKeyboardMarkup(buttons))
    else:
        await msg.reply("Hech narsa topilmadi.")

@bot.on_callback_query()
async def callback_handler(_, call):
    if call.data.startswith("dl|"):
        query = call.data.split("|", 1)[1]
        await call.message.edit("🎧 Yuklab olinmoqda...")
        path = download_song_from_youtube(query)
        if path:
            await call.message.reply_document(path)
        else:
            await call.message.reply("Topilmadi yoki xatolik yuz berdi.")

bot.run()
