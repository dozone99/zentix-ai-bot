import os from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes from dotenv import load_dotenv

load_dotenv() BOT_TOKEN = os.getenv("BOT_TOKEN")

✅ /start

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): await update.message.reply_text( "👋 স্বাগতম Zentix Ai Bot-এ!\n\n" "📌 মেনু দেখতে নিচের '📦 মেনু' বাটনে ক্লিক করুন।" )

✅ /menu

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE): await send_page(update, context, 1)

✅ Menu pagination

async def send_page(update, context, page): if update.callback_query: chat_id = update.callback_query.message.chat.id await update.callback_query.answer() else: chat_id = update.message.chat.id

if page == 1:
    keyboard = [
        [InlineKeyboardButton("🔑 সাইনআপ / সাইনইন", callback_data="auth")],
        [InlineKeyboardButton("🎬 ভিডিও এডিট", callback_data="video_edit")],
        [InlineKeyboardButton("🖼️ ফটো এডিট", callback_data="photo_edit")],
        [InlineKeyboardButton("📼 CapCut/Remini Pro", callback_data="capcut")],
        [InlineKeyboardButton("🛠️ ওয়েব/সফটওয়্যার অর্ডার", callback_data="web_order")],
        [InlineKeyboardButton("➡️ পরের পেজ", callback_data="page_2")]
    ]
elif page == 2:
    keyboard = [
        [InlineKeyboardButton("📱 SMM সার্ভিস", callback_data="smm")],
        [InlineKeyboardButton("🤖 ওয়াজিফা AI", callback_data="wazifa_ai")],
        [InlineKeyboardButton("🧠 Nur AI", callback_data="nur_ai")],
        [InlineKeyboardButton("📞 কাস্টমার কেয়ার", callback_data="customer_care")],
        [InlineKeyboardButton("⬅️ পেছনের পেজ", callback_data="page_1"), InlineKeyboardButton("➡️ পেজ ৩", callback_data="page_3")]
    ]
else:
    keyboard = [
        [InlineKeyboardButton("📲 টেলিকম প্যাক", callback_data="telecom")],
        [InlineKeyboardButton("🔥 গেম টপআপ", callback_data="topup")],
        [InlineKeyboardButton("💳 ব্যালেন্স", callback_data="balance")],
        [InlineKeyboardButton("⬅️ পেছনের পেজ", callback_data="page_2")]
    ]

reply_markup = InlineKeyboardMarkup(keyboard)
await context.bot.send_message(chat_id=chat_id, text="📦 নিচে থেকে আপনার প্রয়োজনীয় সার্ভিস বেছে নিন:", reply_markup=reply_markup)

✅ Callback handler

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE): data = update.callback_query.data if data.startswith("page_"): page_num = int(data.split("_")[1]) await send_page(update, context, page_num) else: await update.callback_query.answer("🚧 ফিচারটি এখনো তৈরি হচ্ছে!")

✅ Bot Run

app = ApplicationBuilder().token(BOT_TOKEN).build() app.add_handler(CommandHandler("start", start)) app.add_handler(CommandHandler("menu", menu)) app.add_handler(CallbackQueryHandler(handle_callback))

app.run_polling()
