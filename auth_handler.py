from telegram import Update
from telegram.ext import ContextTypes

# 🔐 ইন-মেমোরি ডাটাবেস
user_db = {}

# 🔐 সাইনআপ / সাইনইন হ্যান্ডলার
async def auth_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    name = update.effective_user.full_name
    username = update.effective_user.username or "NoUsername"

    if user_id in user_db:
        await update.callback_query.answer(
            "✅ আপনি ইতিমধ্যেই রেজিস্টার্ড করেছেন!", show_alert=True
        )
    else:
        user_db[user_id] = {
            "name": name,
            "username": username
        }
        await update.callback_query.answer(
            f"✅ ধন্যবাদ {name}!\nআপনার একাউন্ট তৈরি হয়েছে!",
            show_alert=True
        )
