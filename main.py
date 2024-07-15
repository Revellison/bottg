import telebot

bot = telebot.TeleBot("7353305734:AAFWjUng9GkwCiV6C2M7hlaU9hjfz7owibM")


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, f"Приветствую тебя, {message.from_user.first_name} {message.from_user.last_name}, здесь происходит фарм макскоинов")


@bot.message_handler(commands=["info"])
def main(message):
    bot.send_message(message.chat.id, f'Твой id {message.from_user.id}')
    bot.send_message(message.chat.id, f'Твой username @{message.from_user.username}')


bot.polling(none_stop=True)
