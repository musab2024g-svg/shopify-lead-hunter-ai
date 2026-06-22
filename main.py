from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from settings import TELEGRAM_BOT_TOKEN
from gemini_test import ask_gemini
from shopify_finder import find_store


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Shopify Lead Hunter AI\n\n"
        "Commands:\n"
        "/find - Find a Shopify lead"
    )


async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔍 Searching for stores..."
    )

    result = find_store()

    await update.message.reply_text(result)


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        result = ask_gemini(text)

        if len(result) > 4000:
            result = result[:4000]

        await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(
            f"Error: {str(e)}"
        )


def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("find", find))

    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            handle_message
        )
    )

    print("BOT RUNNING...")

    app.run_polling(
        drop_pending_updates=True
    )


if __name__ == "__main__":
    main()
