from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["🎮 Play UNO"],
        ["ℹ️ Help"]
    ]
    reply_markup = ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True
    )

    await update.message.reply_text(
        "🃏 Welcome to UNO Game Bot!\n\nChoose an option:",
        reply_markup=reply_markup
    )

# /help command
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ How to Play UNO:\n\n"
        "• Click Play UNO\n"
        "• Join a room\n"
        "• Match starts automatically\n\n"
        "🚀 Full UNO coming soon!"
    )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    print("🤖 UNO Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
