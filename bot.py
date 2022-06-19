
from os import getenv
import random
import time
from dotenv import load_dotenv
from telegram.ext import Updater, MessageHandler, Filters

QUESTIONS = []

def load_questions():
    global QUESTIONS
    with open('domande.txt') as f:
        local_questions = f.read()
    QUESTIONS = local_questions.split("\n")


def bebbo_bot(update, context):
    context.bot.send_message(chat_id = update.effective_chat.id, text = "Here they come")
    while True:
        context.bot.send_message(chat_id = update.effective_chat.id, text = f"Domanda: {random.choice(QUESTIONS)}")
        time.sleep(3*60)


def error_callback(update, context):
    try:
        raise context.error
    except Exception:
        context.bot.send_message(chat_id = update.effective_chat.id, text = 'Errore')

if __name__ == "__main__":
    load_dotenv()
    load_questions()

    TELEGRAM_TOKEN = getenv('TELEGRAM_TOKEN')

    updater = Updater(TELEGRAM_TOKEN, use_context= True) 
    dispatcher = updater.dispatcher

    bot_handler = MessageHandler(Filters.text & (~Filters.command) and Filters.regex(r'!start'), bebbo_bot)
    dispatcher.add_handler(bot_handler)

    dispatcher.add_error_handler(error_callback)

    updater.start_polling()