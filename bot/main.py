import telebot
from bot.config.config import TOKEN
from bot.handlers.command_handlers import register_command_handlers
from bot.handlers.message_handlers import register_message_handlers
from bot.handlers.write_problems_handlers import write_problems_handlers
from bot.handlers.chose_problems_handlers import chose_problems_handlers
from bot.handlers.create_application import create_application

bot = telebot.TeleBot(TOKEN)
bot.user_data = {}

def start_bot():
    register_command_handlers(bot)
    register_message_handlers(bot)
    chose_problems_handlers(bot)
    write_problems_handlers(bot)
    create_application(bot)
    bot.polling(none_stop=True)
