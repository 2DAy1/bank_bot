from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ContextTypes

# Обробка команди /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функція для обробки команди /start.
    Пропонує вибір ролі між клієнтом і консультантом."""
    keyboard = [['/client', '/consultant']]
    reply_markup = ReplyKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "Привіт! Виберіть свою роль:",
        reply_markup=reply_markup
    )

# Обробка команди /client
async def client(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функція для обробки команди /client.
    Реакція на вибір ролі клієнта."""
    await update.message.reply_text("Ви обрали роль Клієнта. Як я можу вам допомогти?")

# Обробка команди /consultant
async def consultant(update: Update, context: ContextTypes.DEFAULT_TYPE):
    """Функція для обробки команди /consultant.
    Реакція на вибір ролі консультанта."""
    await update.message.reply_text("Ви обрали роль Консультанта. Як я можу вам допомогти?")
