import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler

BOT_TOKEN = os.environ["BOT_TOKEN"]  # <-- Use environment variable
ADSTERA_LINK = "https://otieu.com/4/9058346"

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("▶️ Watch Video", url=ADSTERA_LINK)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "🎬 *Click below to watch the video*\n\n"
        "⚠️ Video will open in browser",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
