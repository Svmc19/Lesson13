from telebot import TeleBot
from keyboard import generate_main_menu, laptop_manu, buy_laptop
from db import laptop_name,laptop_image,laptop_price,credit_price

token = '6734058764:AAGUJLRLoingzHwOngjfUngliE7k_qiwXGw'
bot = TeleBot(token)

@bot.message_handler(['start'])
def start(message):
    chat_id = message.chat.id
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    send_mess = f'Salom!\nIsmingiz: {first_name}\nFamiliyangiz{last_name}\nSizning user ID: {user_id}'
    contact = bot.send_message(chat_id, send_mess, reply_markup=generate_main_menu())
    bot.register_next_step_handler(contact, registeration)

def registeration(message):
    chat_id = message.chat.id
    phone_number = message.contact.phone_number
    bot.send_message(chat_id, f"Siz {phone_number} nomer orqali ro'yxatdan o'tdingiz!", reply_markup=laptop_manu())
    bot.register_next_step_handler(message, laptop)


def laptop(message):
    chat_id = message.chat.id
    if message.text == 'Laptop':
            laptop_data = f"Noutbok nomi: {laptop_name}\n\nNoutbok narxi: {laptop_price}\n\nMudatli to'lov: {credit_price}"
            bot.send_photo(chat_id, laptop_image, caption=laptop_data, reply_markup=buy_laptop())



while True:
    try:
        print("Bot run!")
        bot.polling()

    except:
        print("error")
        bot.stop_polling()
        



