import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo
from telegram.ext import Application, CommandHandler, ContextTypes

# ضع التوكن الجديد هنا
TOKEN = "ضـع_تـوكـن_بـوتـك_الـجـديـد_هـنـا"
# ضع رابط GitHub Pages هنا
WEBAPP_URL = "رابط_صفحة_جيت_هاب_الخاصة_بك"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # زر لفتح التطبيق المصغر
    keyboard = [[
        InlineKeyboardButton(text="🚀 دخول المنصة العالمية", web_app=WebAppInfo(url=WEBAPP_URL))
    ]]
    
    await update.message.reply_text(
        f"🌟 أهلاً بك يا {update.effective_user.first_name} في Ballon Global!\n\n"
        "لقد أصبحت المنصة الآن تطبيقاً متكاملاً بين يديك.\n"
        "اضغط على الزر أدناه للبدء:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )

if __name__ == "__main__":
    application = Application.builder().token(TOKEN).build()
    application.add_handler(CommandHandler("start", start))
    print("🚀 البوت شغال وجاهز لاستقبال المستخدمين...")
    application.run_polling()
