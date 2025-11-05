from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from config import BOT_TOKEN, ADMIN_KEY

# /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 خوش آمدید جنید نِز Ads Bot میں!\nمزید جاننے کے لیے /adminpanel لکھیں۔")

# /adminpanel command
async def adminpanel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Check if user sent the key
    args = context.args
    if not args:
        await update.message.reply_text("🔐 براہِ کرم ایڈمن کی درج کریں:\nمثال: /adminpanel JND786SUPERADMIN")
        return

    key = args[0]
    if key == ADMIN_KEY:
        await update.message.reply_text("✅ ایڈمن پینل تک رسائی مل گئی!\nآپ یہاں سے اعلانات یا انعامات مینج کر سکتے ہیں۔")
    else:
        await update.message.reply_text("❌ غلط ایڈمن کی! رسائی مسترد۔")

# Run bot
app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CommandHandler("adminpanel", adminpanel))

print("🤖 Bot is running...")
app.run_polling()
