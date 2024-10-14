from telegram.ext import Updater, CommandHandler
from bot.commands import start, client, consultant
from settings import TELEGRAM_API_TOKEN
import logging

logging.basicConfig(level=logging.INFO)

# Функція для запуску Telegram-бота
def run_telegram_bot():
    # Створюємо Updater з токеном
    updater = Updater(token=TELEGRAM_API_TOKEN, use_context=True)

    # Отримуємо диспетчер для додавання обробників команд
    dispatcher = updater.dispatcher

    # Додаємо обробники команд
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("client", client))
    dispatcher.add_handler(CommandHandler("consultant", consultant))

    # Запускаємо бот у режимі опитування
    updater.start_polling()

    # Підтримуємо бота активним до завершення роботи
    updater.idle()

if __name__ == '__main__':
    run_telegram_bot()
