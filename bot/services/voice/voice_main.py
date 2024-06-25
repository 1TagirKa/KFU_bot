import telebot
from bot_functions import get_voice_response

bot = telebot.TeleBot('6923133944:AAGOML81KKUckHHLXdbou52b4C6EBtX-Gms')

@bot.message_handler(func=lambda message: True)
def handle_message(message):
    audio_content = get_voice_response(message.text)
    if audio_content:
        with open('response.mp3', 'wb') as f:
            f.write(audio_content)
        with open('response.mp3', 'rb') as audio:
            bot.send_voice(message.chat.id, audio)
    else:
        bot.send_message(message.chat.id, 'Извините, не удалось преобразовать текст в речь.')

bot.polling()
