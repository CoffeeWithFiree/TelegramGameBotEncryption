import telebot
from telebot import types
from Settings import Settings
from Algorithms import Algorithms
import random

bot = telebot.TeleBot("...")

words = Settings.words
words_ru = Settings.words_ru
algorithms = Settings.algoritms
user_states = dict()

@bot.message_handler(commands=["start"])
def beggining(message):

    user_states[message.chat.id] = {"lang": "EMPTY", "rand_word": "EMPTY", "encryp_word": "EMPTY"}

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Let's begin")
    btn2 = types.KeyboardButton("My statisticks")
    markup.add(btn1, btn2)

    bot.send_message(message.chat.id, "Hello, let's begin the game. We use next algoritms: 1)Caesar cipher; 2)Atbash Cipher ", reply_markup=markup)

@bot.message_handler(content_types=["text"])
def game(message):
    user_state = user_states.setdefault(message.chat.id, {"lang": "EMPTY", "rand_word": "EMPTY", "encryp_word": "EMPTY"})

    if message.text == "russian":
        user_state["lang"] = "RU"
    elif message.text == "english":
        user_state["lang"] = "ENG"

    if message.text == "Let's begin" or message.text == "try again" or message.text == "russian" or message.text == "english":
        if user_state["lang"] == "EMPTY":

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn1 = types.KeyboardButton("russian")
            btn2 = types.KeyboardButton("english")
            markup.add(btn1, btn2)
            bot.send_message(message.chat.id, "Please, choice language", reply_markup=markup)
        else:
            r_a = random.randint(0, len(algorithms) - 1)
            r_w = random.randint(0, len(words) - 1) if user_state["lang"] == "ENG" else random.randint(0, len(words_ru) - 1)

            user_state["rand_word"] = words[r_w] if user_state["lang"] == "ENG" else words_ru[r_w]
            rand_word = user_state["rand_word"]

            alg = Algorithms(rand_word, user_state["lang"])

            if algorithms[r_a] == "CaesarCipher":
                user_state["encryp_word"] = alg.CaesarCipher()
            elif algorithms[r_a] == "AtbashCipher":
                user_state["encryp_word"] = alg.AtbashCipher()
            bot.send_message(message.chat.id, f"word = {user_state["encryp_word"]}, decipher this word. Attention, if you use Russian language, then there is no letter 'ё'. If you want to change the language, write 'english' or 'russian'")

    elif user_state["rand_word"] != "Empty":
        if message.text == user_state["rand_word"]:
            ra_w = user_state["rand_word"]
            user_state["rand_word"] = "EMPTY"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("try again")
            markup.add(btn_gu)

            bot.send_message(message.chat.id, f"You're right, the encrypted word is {ra_w}.", reply_markup=markup)

        elif message.text == "i give up":
            ra_w = user_state["rand_word"]
            user_state["rand_word"] = "EMPTY"

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("try again")
            markup.add(btn_gu)

            bot.send_message(message.chat.id, f"What a pity! the encrypted word is: {ra_w}",reply_markup=markup)

        else:

            markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
            btn_gu = types.KeyboardButton("i give up")
            markup.add(btn_gu)
            bot.send_message(message.chat.id, f"You're wrong, try again, decipher this word: {user_state["encryp_word"]}", reply_markup=markup)

    elif message.text == "My statisticks":
        bot.send_message(message.chat.id,"statisticks")

bot.polling(non_stop=True)
