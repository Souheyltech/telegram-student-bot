from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, ContextTypes, filters

TOKEN = "7577711655:AAGu885MWbntHlYPBaKVhPP6GlqBN32zhX4"
ADMIN_ID = 5646476808  # رقم معرفك كمعلم

async def forward_to_teacher(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.message.from_user
    text = update.message.text

    # إرسال الرسالة إليك
    await context.bot.send_message(
        chat_id=ADMIN_ID,
        text=f"📩 رسالة من الطالب {user.first_name} (@{user.username}):\n{text}"
    )

    # رد تلقائي للطالب
    await update.message.reply_text("✅ أرسلت إجابتك للمعلم، شكرًا.")

app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, forward_to_teacher))
app.run_polling()