import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, CallbackQueryHandler, ContextTypes
import os
from dotenv import load_dotenv
from cnn import cnn

#WORKING!
#add embed?


load_dotenv()
KEY = os.getenv('key')

async def fear(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    #handles /fear command, outputs cnn fear and greed
    await update.message.reply_text(cnn())


def main() -> None:
    #integrate into API
    app = Application.builder().token(KEY).build()

    #fear cmd, add handler creates new commands
    app.add_handler(CommandHandler('fear', fear))

    #start bot
    app.run_polling()


if __name__ == "__main__":
    main()