from telebot import TeleBot, apihelper
import os
from dotenv import load_dotenv

load_dotenv()


API_TOKEN = os.environ.get("API_TOKEN")



apihelper.proxy = {
    "http": "socks5://127.0.0.1:10808",
    "https": "socks5://127.0.0.1:10808"
}

bot = TeleBot(API_TOKEN)

bot.infinity_polling()


