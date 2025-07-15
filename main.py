
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "7577711655:AAGu885MWbntHlYPBaKVhPP6GlqBN32zhX4"
TEACHER_CHAT_ID = 5646476808

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("مرحباً! أرسل إجابتك وسيصل للمعلم مباشرة.")

async def handle_answer(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    answer = update.message.text
    message = f"📨 إجابة جديدة من {user.full_name} (@{user.username}):\n\n{answer}"
    await context.bot.send_message(chat_id=TEACHER_CHAT_ID, text=message)
    await update.message.reply_text("✅ تم إرسال إجابتك للمعلم بنجاح!")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_answer))

app.run_polling()
