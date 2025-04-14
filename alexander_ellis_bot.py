from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = '7651417714:AAGxq5lb66C7HYvw0u4_aP71YrA7yDABVwY'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Доброе утро. Это Александр Эллис. Я слушаю. С чего начнем наш день?"
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_message = update.message.text
    response = f"Александр Эллис: Хм… любопытный выбор. Что ты хочешь этим достичь?"
    await update.message.reply_text(response)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

app.run_polling()
