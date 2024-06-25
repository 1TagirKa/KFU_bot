from bot.models.text_classifier import classify_text
from bot.buttons.buttons_creator import correct_answer_buttons
def write_problems_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'write_problem')
    def handle_write_problem(call):
        bot.answer_callback_query(call.id)
        # Инициализация состояния с счётчиком попыток
        bot.user_data[call.from_user.id] = {'state': 'awaiting_problem_description', 'attempts': 0}
        bot.send_message(call.message.chat.id,
                         "Кратко опишите свою проблему, а я постараюсь определить её тип, чтобы помочь вам.")

    @bot.message_handler(func=lambda message: bot.user_data.get(message.from_user.id, {}).get('state') == 'awaiting_problem_description')
    def handle_problem_description(message):
        user_info = bot.user_data[message.from_user.id]
        response = classify_text(message.text)

        if response:
            bot.reply_to(message, f"Ваша проблема - это {response}", reply_markup=correct_answer_buttons())
            del bot.user_data[message.from_user.id]  # Очистка состояния после успешной классификации
        else:
            user_info['attempts'] += 1
            if user_info['attempts'] < 2:
                bot.send_message(message.chat.id,
                                 "Я не могу распознать вашу ошибку. Попробуйте написать ещё раз, но по-другому.")
            else:
                bot.send_message(message.chat.id,
                                 "Я не смог определить вашу проблему после нескольких попыток. Пожалуйста, воспользуйтесь другим способом или обратитесь к специалисту.")
                del bot.user_data[message.from_user.id]  # Очистка состояния после двух неудачных попыток
