import telebot
from transliterate import to_cyrillic, to_latin


TOKEN = '6421196627:AAECL_nech3DTjlL1RW3HdqNPbA-COBaVnw'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalomu alaykum, Xush kelibsiz!"
    javob += "\nMatn kiriting nozzikina qo'lariz bilan: "
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda m: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)

bot.infinity_polling()


#matn = input("Matn kiriting: ")
#if matn.isascii():
#    print(to_cyrillic(matn))
#else:
#    print(to_latin(matn))