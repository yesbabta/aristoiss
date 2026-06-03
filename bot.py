from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "8981871030:AAHyAuuuoHpRhfM9Sp0MySORAA8wD2Ldl0c"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    await update.message.reply_text(
        f"Приветствую, {user_first_name} в боте Aristois\n\n"
        f"📢 Зайдите в канал чтоб следить за новостями: https://t.me/+TbGWum5UxS5jOTQy"
    )

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("Бот запущен")
    app.run_polling()

if __name__ == "__main__":
    main()
