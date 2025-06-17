import os from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, ReplyKeyboardMarkup from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, MessageHandler, ContextTypes, filters from dotenv import load_dotenv

Load environment variables

load_dotenv() BOT_TOKEN = os.getenv("BOT_TOKEN")

In-memory user storage

user_db = {}

Start Command

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE): keyboard = [["\ud83d\udce6 \u09ae\u09c7\u09a8\u09c1"]] reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True, one_time_keyboard=True) await update.message.reply_text( "\ud83c\udf1f \u09b8\u09cd\u09ac\u09be\u0997\u09a4\u09ae Zentix Ai Bot -\u098f!\n\n" "\ud83e\udd16 \u0986\u09ae\u09bf \u0986\u09aa\u09a8\u09be\u09b0 \u09ac\u09cd\u09af\u0995\u09cd\u09a4\u09bf\u0997\u09a4 AI \u09b8\u09b9\u0995\u09be\u09b0\u09c0\u09c0\u0964\n\n" "\ud83d\udce6 \u09ae\u09c7\u09a8\u09c1 \u09a6\u09c7\u0996\u09a4\u09c7 \u09a8\u09bf\u099a\u09c7\u09b0 '\ud83d\udce6 \u09ae\u09c7\u09a8\u09c1' \u09ac\u09be\u099f\u09a8\u09c7 \u0995\u09cd\u09b2\u09bf\u0995 \u0995\u09b0\u09c1\u09a8 \u2014\n" "\u09a8\u09a4\u09c1\u09a8 \u09aa\u09cd\u09b0\u09af\u09c1\u0995\u09cd\u09a4\u09bf\u09b0 \u09b8\u09be\u09a5\u09c7 \u09af\u09c1\u0995\u09cd\u09a4 \u09b9\u09cb\u09a8 \u098f\u0995 \u0995\u09cd\u09b2\u09bf\u0995\u09c7\u0964", reply_markup=reply_markup, parse_mode="Markdown" )

Menu Command

async def menu(update: Update, context: ContextTypes.DEFAULT_TYPE): await send_page(update, context, 1)

Signup/Auth Placeholder

async def auth(update: Update, context: ContextTypes.DEFAULT_TYPE): user_id = update.effective_user.id if user_id in user_db: await update.callback_query.answer("\u2705 আপনি ইতিমধ্যে নিবন্ধিত!", show_alert=True) else: user_db[user_id] = { "name": update.effective_user.full_name, "username": update.effective_user.username, } await update.callback_query.answer("\ud83d\udcc5 রেজিস্ট্রেশন সম্পন্ন হয়েছে!", show_alert=True)

Menu Pagination

async def send_page(update, context, page): if update.callback_query: chat_id = update.callback_query.message.chat.id await update.callback_query.answer() else: chat_id = update.message.chat.id

if page == 1:
    keyboard = [
        [InlineKeyboardButton("\ud83d\udd11 \u09b8\u09be\u0987\u09a8\u0986\u09aa / \u09b8\u09be\u0987\u09a8\u0987\u09a8", callback_data="auth")],
        [InlineKeyboardButton("\ud83c\udfae \u09ad\u09bf\u09a1\u09bf\u0993 \u098f\u09a1\u09bf\u099f", callback_data="video_edit")],
        [InlineKeyboardButton("\ud83d\uddbc\ufe0f \u09ab\u099f\u09cb \u098f\u09a1\u09bf\u099f", callback_data="photo_edit")],
        [InlineKeyboardButton("\ud83d\udcbc CapCut/Remini Pro", callback_data="capcut")],
        [InlineKeyboardButton("\ud83d\udee0\ufe0f \u0993\u09af\u09bc\u09c7\u09ac/\u09b8\u09ab\u099f\u0993\u09af\u09bc\u09be\u09b0 \u0985\u09b0\u09cd\u09a1\u09be\u09b0", callback_data="web_order")],
        [InlineKeyboardButton("\u27a1\ufe0f \u09aa\u09b0\u09c7\u09b0 \u09aa\u09c7\u099c", callback_data="page_2")]
    ]
elif page == 2:
    keyboard = [
        [InlineKeyboardButton("\ud83d\udcf1 SMM \u09b8\u09be\u09b0\u09cd\u09ad\u09bf\u09b8", callback_data="smm")],
        [InlineKeyboardButton("\ud83e\udd16 \u0993\u09af\u09bc\u09be\u099c\u09bf\u09ab\u09be AI", callback_data="wazifa_ai")],
        [InlineKeyboardButton("\ud83e\udeb0 Nur AI", callback_data="nur_ai")],
        [InlineKeyboardButton("\ud83d\udcde \u0995\u09be\u09b8\u09cd\u099f\u09ae\u09be\u09b0 \u0995\u09c7\u09af\u09bc\u09be\u09b0", callback_data="customer_care")],
        [InlineKeyboardButton("\u2b05\ufe0f \u09aa\u09c7\u099b\u09a8\u09c7\u09b0 \u09aa\u09c7\u099c", callback_data="page_1"), InlineKeyboardButton("\u27a1\ufe0f \u09aa\u09c7\u099c \u09e9", callback_data="page_3")]
    ]
else:
    keyboard = [
        [InlineKeyboardButton("\ud83d\udcf2 \u099f\u09c7\u09b2\u09bf\u0995\u09ae \u09aa\u09cd\u09af\u09be\u0995", callback_data="telecom")],
        [InlineKeyboardButton("\ud83d\udd25 \u0997\u09c7\u09ae \u099f\u09aa\u0986\u09aa", callback_data="topup")],
        [InlineKeyboardButton("\ud83d\udcb3 \u098f\u09a1 \u09ac\u09cd\u09af\u09be\u09b2\u09c7\u09a8\u09cd\u09b8", callback_data="balance")],
        [InlineKeyboardButton("\u2b05\ufe0f \u09aa\u09c7\u099b\u09a8\u09c7\u09b0 \u09aa\u09c7\u099c", callback_data="page_2")]
    ]

reply_markup = InlineKeyboardMarkup(keyboard)
await context.bot.send_message(
    chat_id=chat_id,
    text="\ud83d\udce6 \u09a8\u09bf\u099a\u09c7 \u09a5\u09c7\u0995\u09c7 \u0986\u09aa\u09a8\u09be\u09b0 \u09aa\u09cd\u09b0\u09af\u09cb\u099c\u09a8\u09c0\u09af\u09bc \u09b8\u09be\u09b0\u09cd\u09ad\u09bf\u09b8 \u09ac\u09c7\u099b\u09c7 \u09a8\u09bf\u09a8:",
    reply_markup=reply_markup
)

Callback handler

async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE): data = update.callback_query.data if data.startswith("page_"): page_num = int(data.split("_")[1]) await send_page(update, context, page_num) elif data == "auth": await auth(update, context) else: await update.callback_query.answer("\ud83d\udea7 \u09ab\u09bf\u099a\u09be\u09b0\u099f\u09bf \u098f\u0996\u09a8\u09cb \u09a4\u09cd\u09af\u09be\u09b0\u09bf \u09b9\u099a\u09cd\u099b\u09c7!", show_alert=True)

Run Bot

app = ApplicationBuilder().token(BOT_TOKEN).build() app.add_handler(CommandHandler("start", start)) app.add_handler(CommandHandler("menu", menu)) app.add_handler(CallbackQueryHandler(handle_callback)) app.add_handler(MessageHandler(filters.TEXT & filters.Regex(r"মেনু"), menu)) app.run_polling()
