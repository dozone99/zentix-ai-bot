from telegram import Update
from telegram.ext import ContextTypes

# 🔐 ইন-মেমোরি ডাটাবেজ
user_db = {}

# 🧠 সাইনআপ / সাইনইন ফাংশন
async def auth_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.effective_user.full_name
    username = update.effective_user.username or "NoUsername"

    if user_id in user_db:
        await update.callback_query.answer(
            "✅ আপনি ইতিমধ্যে রেজিস্ট্রেশন করেছেন।", show_alert=True
        )
    else:
        user_db[user_id] = {
            "name": name,
            "username": username
        }
        await update.callback_query.answer(
            f"📅 ধন্যবাদ {name}!\nআপনার একাউন্ট তৈরি হয়েছে।", show_alert=True
        )