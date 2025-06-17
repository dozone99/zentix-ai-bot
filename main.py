import os
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 স্বাগতম Zentix Ai Bot-এ!\n\n"
        "📌 ফিচার মেনু দেখতে /menu টাইপ করুন।"
    )

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📋 মেনু:\n"
        "1. 🎬 ভিডিও এডিট\n"
        "2. 🖼️ ফটো এডিট\n"
        "3. 🤖 ওয়াজিফা AI\n"
        "4. 💳 ব্যালেন্স চেক\n"
        "👉 আরও ফিচার আসছে..."
    )

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("menu", menu))

app.run_polling()
