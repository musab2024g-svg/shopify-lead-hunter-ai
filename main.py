from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

from settings import TELEGRAM_BOT_TOKEN


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🚀 Shopify Lead Hunter AI جاهز للعمل"
    )


async def find(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔎 البحث عن المتاجر سيضاف في الخطوة القادمة"
    )


def main():
    app = Application.builder().token(
        TELEGRAM_BOT_TOKEN
    ).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("find", find))

    print("BOT RUNNING...")

    app.run_polling()


if __name__ == "__main__":
    main()
