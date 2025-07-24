from config import TOKEN 
import telebot
import segno
import os

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['help'])
def handle_start(message):
    bot.send_message(message.chat.id, "Привет! Я Бот для преобразования текста в QR код. Напишите мне что-нибудь  через /convert")


@bot.message_handler(commands=['convert'])
def handle_convert_command(message):
    bot.send_message(message.chat.id, "Пожалуйста, отправьте мне текст для преобразования в QR-код.")

@bot.message_handler(func=lambda m: True)
def handle_text(message):
    text_to_convert = message.text
    qrcode = segno.make_qr(text_to_convert)
    filename = f"{message.chat.id}_qrcode.png"
    qrcode.save(filename)
    with open(filename, 'rb') as photo:
        bot.send_photo(message.chat.id, photo)
    os.remove(filename)
bot.infinity_polling()