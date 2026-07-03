from telegram import (
    Update,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

import os

TOKEN = os.getenv("BOT_TOKEN")
# အမြဲပေါ်နေမယ့် Keyboard
keyboard = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(
                text="🎮 ဂိမ်းကစားရန်",
                web_app=WebAppInfo(url="https://www.365king.net")
            )
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False,
    is_persistent=True,
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_photo(
        photo="https://www.365king.net/logo.png",   # ဒီနေရာမှာ မင်းပုံ URL ထည့်
        caption="""👋 မင်္ဂလာပါ

🎮 အောက်က "ဂိမ်းကစားရန်" ကိုနှိပ်ပြီး ဝင်ကစားနိုင်ပါတယ်။
""",
        reply_markup=keyboard,
    )

# ဘာစာပို့ပို့ Keyboard ပြန်ပေါ်အောင်
async def keep_keyboard(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👇 အောက်က Button ကိုနှိပ်ပြီး ဂိမ်းဝင်ပါ။",
        reply_markup=keyboard,
    )

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, keep_keyboard))

print("Bot is running...")
app.run_polling()