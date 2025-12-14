from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    ContextTypes,
    MessageHandler,
    filters
)
from config import BOT_TOKEN
from game.lobby import join_lobby

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

# help
async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "ℹ️ UNO Rules (Coming Soon)\n\n"
        "• Join game\n"
        "• 2–4 players\n"
        "• Last card wins"
    )

# PLAY UNO button handler
async def play_uno(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    room_id, count = join_lobby(user.id)

    if count < 2:
        await update.message.reply_text(
            f"⏳ Waiting for players...\n"
            f"Room: {room_id}\n"
            f"Players joined: {count}/4"
        )
    else:
        await update.message.reply_text(
            f"🎉 Game Starting!\n"
            f"Room: {room_id}\n"
            f"Players: {count}"
        )

def main():
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))

    # BUTTON click handler
    app.add_handler(
        MessageHandler(filters.TEXT & filters.Regex("^🎮 Play UNO$"), play_uno)
    )

    print("🤖 UNO Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
