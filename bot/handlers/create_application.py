import telebot

def create_application(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'start_create_application')
    def ask_app_description(call):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пожалуйста, максимально подробно опишите вашу проблему')
        bot.user_data[call.from_user.id] = {'state': 'awaiting_application_description'}

    @bot.message_handler(
        func=lambda message: bot.user_data.get(message.from_user.id, {}).get('state') == 'awaiting_application_description')
    def ask_file_description(message):
        bot.send_message(message.chat.id, f'Теперь отправьте файл по необходимости - это может быть фото, видео или любой другой файл, если же вы не хотите добавлять файл, нажмите на кнопку продолжить.')
        bot.user_data[message.from_user.id] = {'state': 'awaiting_application_file'}

    @bot.message_handler(
        func=lambda message: bot.user_data.get(message.from_user.id, {}).get(
            'state') == 'awaiting_application_file', content_types=['document', 'photo', 'audio', 'video', 'voice'])
    def send_application(message):
        bot.send_message(message.chat.id, 'Заявка успешно отправлена')


from telebot import TeleBot, types
import os

# Placeholder bot token
TOKEN = 'YOUR_BOT_TOKEN'
bot = TeleBot(TOKEN)

def setup_email_sending_handlers(bot):
    # Function to send email with the application details
    def finalize_and_send_email(user_id, chat_id):
        user_data = bot.user_data[user_id]
        subject = "Новая заявка"
        body = f"Описание проблемы: {user_data['description']}"
        to_email = "receiver@example.com"
        filename = user_data.get('file_path')

        send_email(subject, body, to_email, filename)

        bot.send_message(chat_id, 'Заявка успешно отправлена и передана по электронной почте.')
        # Clean up after sending the email
        if filename:
            os.remove(filename)
        del bot.user_data[user_id]

    @bot.callback_query_handler(func=lambda call: call.data == 'start_create_application')
    def ask_app_description(call):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Пожалуйста, максимально подробно опишите вашу проблему')
        bot.user_data[call.from_user.id] = {'state': 'awaiting_application_description'}

    @bot.message_handler(
        func=lambda message: bot.user_data.get(message.from_user.id, {}).get('state') == 'awaiting_application_description')
    def receive_description_and_ask_for_file(message):
        bot.user_data[message.from_user.id] = {
            'state': 'awaiting_application_file',
            'description': message.text
        }
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True)
        markup.add('Продолжить без файла')
        bot.send_message(message.chat.id, 'Теперь отправьте файл по необходимости - это может быть фото, видео или любой другой файл, если же вы не хотите добавлять файл, нажмите на кнопку ниже.',
                         reply_markup=markup)

    @bot.message_handler(
        func=lambda message: bot.user_data.get(message.from_user.id, {}).get('state') == 'awaiting_application_file',
        content_types=['document', 'photo', 'audio', 'video', 'voice', 'text'])
    def handle_file_or_no_file(message):
        user_id = message.from_user.id
        if message.content_type == 'text' and message.text == 'Продолжить без файла':
            finalize_and_send_email(user_id, message.chat.id)
        else:
            # Assuming message has a file, save it locally
            file_info = bot.get_file(message.document.file_id if message.content_type == 'document' else message.photo[-1].file_id)
            downloaded_file = bot.download_file(file_info.file_path)
            local_file_path = os.path.join('downloaded_files', file_info.file_path.split('/')[-1])
            with open(local_file_path, 'wb') as new_file:
                new_file.write(downloaded_file)
            bot.user_data[user_id]['file_path'] = local_file_path
            finalize_and_send_email(user_id, message.chat.id)

# Initialize handlers
setup_email_sending_handlers(bot)

