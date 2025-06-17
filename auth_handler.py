from telegram import Update
from telegram.ext import ContextTypes

# 🔐 ইন-মেমোরি ডাটাবেজ
user_db = {}

# 📍 স্টেট ডিফাইন
ASK_NAME = 1

# 📥 স্টার্ট সাইনআপ - বাটনে ক্লিক করলে
async def auth_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await update.callback_query.message.reply_text("👤 দয়া করে আপনার *নাম* লিখুন:", parse_mode="Markdown")
    return ASK_NAME

# 📝 নাম গ্রহণ ও সংরক্ষণ
async def save_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.message.text
    username = update.effective_user.username or "NoUsername"

    user_db[user_id] = {
        "name": name,
        "username": username
    }

    await update.message.reply_text(
        f"✅ ধন্যবাদ {name}!\nআপনার একাউন্ট সফলভাবে তৈরি হয়েছে।"
    )
    return -1  # end conversation
