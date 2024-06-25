from bot.buttons.buttons_creator import problems_buttons, subproblems_buttons


def chose_problems_handlers(bot):
    @bot.callback_query_handler(func=lambda call: call.data == 'choose_problem')
    def handle_choose_problem(call):
        bot.answer_callback_query(call.id)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите проблему из списка ниже:", reply_markup=problems_buttons(backbutton_callback='restart'))

    @bot.callback_query_handler(func=lambda call: 'problems' in call.data)
    def handle_category_selection(call):
        markup = subproblems_buttons(call.data)
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите подтему из списка ниже:", reply_markup=markup)

    @bot.callback_query_handler(func=lambda call: call.data == 'choose_problem')
    def handle_choose_problem(call):
        bot.answer_callback_query(call.id)
        markup = problems_buttons()
        bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                              text="Выберите категорию проблемы:", reply_markup=markup)


