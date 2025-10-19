import telebot
import movie_parser

# Замените 'ВАШ_ТОКЕН' на токен, полученный от BotFather
TOKEN = 'ВАШ_ТОКЕН'
bot = telebot.TeleBot(TOKEN)


# Обработчик команды '/start'
@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "Привет! Добро пожаловать в справочный бот по фильмам!")


@bot.message_handler(func=lambda message: True)
def response(message):
    movie_title = message.text

    movie_url = movie_parser.get_movie_url(movie_title)

    if movie_url:

        movie_info = movie_parser.get_movie_info(movie_url)
        if movie_info:
            text = f"Название: {movie_info['title']}\nОписание: {movie_info['description']}"

            bot.send_message(message.chat.id, text)
        else:
            bot.send_message(message.chat.id, "Ошибка. Попробуйте позже")
    else:
        bot.send_message(message.chat.id, "Ошибка. Попробуйте позже")


bot.polling()
