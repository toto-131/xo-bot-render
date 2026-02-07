import os
import telebot

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "✅ XO Bot работает 24/7 на Render! 🚀\n/play - начать игру")

@bot.message_handler(commands=['play'])
def play(message):
    bot.reply_to(message, "🎮 Игра в разработке!\nБот работает круглосуточно!")

print("🤖 Бот запускается...")
bot.infinity_polling()
