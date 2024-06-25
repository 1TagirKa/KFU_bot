from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
from bot.config.config import problems

def problems_buttons(backbutton_callback = None) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    for category, details in problems.items():
        button = InlineKeyboardButton(category, callback_data=details['callback_data'])
        markup.add(button)
    if backbutton_callback: markup.add(InlineKeyboardButton('🔙ВЕРНУТЬСЯ В НАЧАЛО', callback_data=backbutton_callback))
    return markup

def subproblems_buttons(callback_data) -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    # Ищем правильную категорию по callback_data
    category = next((item for item in problems.values() if item['callback_data'] == callback_data), None)

    if not category:
        print(f"Ошибка: Категория с callback_data '{callback_data}' не найдена.")
        return markup

    # Добавляем кнопки для субпроблем
    subproblems = category.get('subproblems', {})
    for subproblem_name, subproblem_tag in subproblems.items():
        print(subproblem_tag)
        markup.add(InlineKeyboardButton(subproblem_name, callback_data=subproblem_tag))

    # Кнопка "Назад"
    markup.add(InlineKeyboardButton('🔙 Назад', callback_data='choose_problem'))
    return markup

def choosing_application_type_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    yourself_button = InlineKeyboardButton('🧑‍💻Заполнить самостоятельно', url='https://shelly.kpfu.ru/e-ksu/tech_center_system.web_request_form?p_eu=1&p1=352051&p2=24290092828725529529923225141382&p_h=0BAE8A4F0E0B2502F90DDA661ED17983')
    help_button = InlineKeyboardButton('🤖Помочь составить', callback_data='start_create_application')
    start_button = InlineKeyboardButton('Вернуться в самое начало', callback_data='restart')
    markup.add(yourself_button, help_button, start_button)
    return markup

def did_solution_help_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton('Помогло✅', callback_data='successfully_completed')
    not_button = InlineKeyboardButton('Не помогло⛔', callback_data='unsuccessfully_completed')
    markup.add(yes_button, not_button)
    return markup

def restart_button() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton('Начать заново', callback_data='restart')
    markup.add(start_button)
    return markup

def start_button() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup()
    start_button = InlineKeyboardButton('Начать', callback_data='restart')
    markup.add(start_button)
    return markup

def correct_answer_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=2)
    yes_button = InlineKeyboardButton('Да✅', callback_data='_')
    no_button = InlineKeyboardButton('Нет⛔', callback_data='write_problem')
    markup.add(yes_button, no_button)
    return markup
