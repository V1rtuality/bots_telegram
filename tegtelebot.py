import telebot

# Создаем объект бота
bot = telebot.TeleBot("8689488400:AAGVWuHlFRLFNJlNLC-4UX15VJ5g1hm09Uw")

# Обработчик команды /start
@bot.message_handler(commands=['start'])
def cmd_start(message):
    bot.reply_to(
        message, 
        f"Привет, {message.from_user.first_name}! я специально создал бота для исходника на гит хаб"
    )

# Запуск бота
if __name__ == "__main__":
    print("Бот запущен...")
    bot.infinity_polling()
