from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello {update.effective_user.first_name} {update.effective_user.id}")


app = ApplicationBuilder().token("6870605175:AAElZSI9Vm8LgAaP58NHlaFwuy5MFVPqnMs").build()

app.add_handler(CommandHandler("start", hello))

app.run_polling()
