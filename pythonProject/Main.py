import telebot
from telebot import types
from Settings import Settings
from Algorithms import Algorithms
import random

bot = telebot.TeleBot("7337994678:AAEOqV7DceI1Y6_WX1KJzi3Rf5ErvTMGCQU")

words = Settings.words
words_ru = Settings.words_ru
algorithms = Settings.algoritms

rand_word = "EMPTY"
encryp_word = "EMPTY"
lang = "EMPTY"

@bot.message_handler(commands=["start"])
def beggining(message):

    global rand_word
    global encryp_word
    rand_word = "EMPTY"
    encryp_word = "EMPTY"

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("Let's begin")

    btn2 = types.KeyboardButton("My statisticks")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Hello, let's begin the game. We use next algoritms: 1)Caesar cipher ", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def game(message):
    global rand_word
    global encryp_word
    global lang

    if message.text == "russian":
        lang = "RU"
    elif message.text == "english":
        lang = "ENG"

    if message.text == "Let's begin" or message.text == "try again" or message.text == "russian" or message.text == "english":
        if lang == "EMPTY":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("russian")
            btn2 = types.KeyboardButton("english")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Please, choice language", reply_markup=markup)
        else:
            rand_word = "EMPTY"

            r_a = 0 #random.randint(0, len(algorithms) - 1)
            r_w = random.randint(0, len(words) - 1) if lang == "ENG" else random.randint(0, len(words_ru) - 1)

            rand_word = words[r_w] if lang == "ENG" else words_ru[r_w]

            alg = Algorithms(rand_word, lang)

            if algorithms[r_a] == "CaesarCipher":
                encryp_word = alg.CaesarCipher()
                bot.send_message(message.chat.id, f"word = {encryp_word}, decipher this word. Attention, if you use Russian language, then there is no letter 'ё'. If you want to change the language, write 'english' or 'russian'")

    elif rand_word != "Empty":

        if message.text == rand_word:
            ra_w = rand_word
            rand_word = "EMPTY"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("try again")
            markup.add(btn_gu)

            bot.send_message(message.chat.id, f"You're right, the encrypted word is {ra_w}.", reply_markup=markup)

        elif message.text == "i give up":
            ra_w = rand_word
            rand_word = "EMPTY"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("try again")
            markup.add(btn_gu)

            bot.send_message(message.chat.id, f"What a pity! the encrypted word is: {ra_w}",reply_markup=markup)

        else:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("i give up")
            markup.add(btn_gu)
            bot.send_message(message.chat.id, f"You're wrong, try again, decipher this word: {encryp_word}", reply_markup=markup)

    elif message.text == "My statisticks":
        bot.send_message(message.chat.id,"statisticks")

bot.polling(non_stop=True)