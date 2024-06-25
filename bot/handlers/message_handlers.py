from bot.config.config import problems
from bot.buttons.buttons_creator import choosing_application_type_buttons
from bot.buttons.buttons_creator import did_solution_help_buttons
from bot.buttons.buttons_creator import restart_button
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def register_message_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'restart')
    def handle_restart(call):
        markup = InlineKeyboardMarkup(row_width=2)
        button_write = InlineKeyboardButton("✍️Описать проблему", callback_data='write_problem')
        button_choose = InlineKeyboardButton("📋Выбрать из списка", callback_data='choose_problem')
        markup.add(button_write, button_choose)
        bot.send_message(chat_id=call.message.chat.id, text="Как вы хотите сообщить о проблеме?", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == 'successfully_completed')
    def handle_successfully_completed(call):
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Рад был вам помочь, если хотите оставить какое-замечание относительно моей работы, то можете написать сообщение ниже. Или можете начать процесс заново.",
                              reply_markup=restart_button())

    @bot.callback_query_handler(func=lambda call: call.data == 'unsuccessfully_completed')
    def handle_unsuccessfully_completed(call):
        markup = choosing_application_type_buttons()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text='Вы можете составить заявку на решению этой проблемы - можете сделать это самостоятельно на сайте или я могу помочь вам с её составлением.',
                              reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data in [tag for category in problems.values() for tag in
                                                                category['subproblems'].values()])
    @bot.callback_query_handler(func=lambda call: call.data.startswith('tag_'))
    def handle_subproblem_action(call):
        text = ''
        markup = InlineKeyboardMarkup()
        if call.data == 'no_internet_access':
            service_url = 'http://localhost:5002/solve'
            response = requests.post(service_url, json={"error_type": "Принтер не печатает"})
            if response.ok:
                text = response.json()['response']
            else:
                text = "Ошибка при получении ответа от сервиса"
            markup = did_solution_help_buttons()
        else:
            text = 'К сожалению, я не могу вам помочь с этой проблемой. Вы можете составить заявку на решению этой проблемы - можете сделать это самостоятельно на сайте или я могу помочь вам с её составлением.'
            markup = choosing_application_type_buttons()
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text=text, reply_markup=markup)

    @bot.message_handler(commands=['next'])
    def handle_subproblem_action(message):
        bot.send_message(chat_id=message.chat.id, text='''Для более оперативного решения вашей проблемы с принтером, я создал чат с сотрудником технического отдела. Пожалуйста, перейдите по следующей ссылке, чтобы описать свою проблему и поддерживать связь со специалистом: https://t.me/+YrgRg5zhNqtjZTcy''')

    @bot.message_handler(commands=['nextt'])
    def handle_subproblem_action(message):
        bot.send_message(chat_id=message.chat.id,
                         text='''Здравствуйте!

Этот чат создан специально для того, чтобы помочь вам решить вашу техническую проблему, связанную с принтером. В чат добавлен специалист технического отдела, который поможет вам описать свою проблему и всегда будет на связи для оказания поддержки.''')






