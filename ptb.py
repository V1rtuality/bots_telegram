import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# Настройка логирования (полезно, чтобы видеть ошибки в консоли)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# Функция-обработчик команды /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Привет, {user_name}! я специально создал бота для исходника на гит хаб"
    )

if __name__ == "__main__":
    # Создаем приложение и передаем токен
    application = ApplicationBuilder().token("8689488400:AAGVWuHlFRLFNJlNLC-4UX15VJ5g1hm09Uw").build()
    
    # Регистрируем обработчик команды /start
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    
    print("Бот запущен...")
    # Запуск бота
    application.run_polling()
