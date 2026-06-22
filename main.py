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


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Shopify Lead Hunter AI جاهز للعمل\n\nأرسل أي سؤال وسأستخدم Gemini للرد."
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text

    try:
        await update.message.reply_text("🔍 جاري التحليل...")

        result = ask_gemini(text)

        if len(result) > 4000:
            result = result[:4000]

        await update.message.reply_text(result)

    except Exception as e:
        await update.message.reply_text(
            f"❌ Error:\n{str(e)}"
        )


def main():
    app = Application.builder().token(TELEGRAM_BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))

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
