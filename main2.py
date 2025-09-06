import telebot
from telebot import types
from cart import edit_card       # pul modulidan import
from avtobus import add_datetime # avtobus modulidan import

TOKEN = "7116883036:AAHHhoMUyuH49k-bgV-0evNt6_EvYw3sn9Q"
bot = telebot.TeleBot(TOKEN)

user_data = {}

# ================== PUL ==================
@bot.message_handler(func=lambda msg: msg.text == "Pul")
def ask_user_name(message):
    bot.send_message(message.chat.id, "✅ O‘z ismingizni kiriting (yoki 'skip' yozing):")
    bot.register_next_step_handler(message, process_user_name)

def process_user_name(message):
    user_data[message.chat.id] = {"username": message.text}
    bot.send_message(message.chat.id, "💳 O‘z karta raqamingizni kiriting (yoki 'skip'):")
    bot.register_next_step_handler(message, process_user_card)

def process_user_card(message):
    user_data[message.chat.id]["card_num"] = message.text
    bot.send_message(message.chat.id, "👤 Qabul qiluvchi ismini kiriting (yoki 'skip'):")
    bot.register_next_step_handler(message, process_receiver_name)

def process_receiver_name(message):
    user_data[message.chat.id]["receiver_name"] = message.text
    bot.send_message(message.chat.id, "💳 Qabul qiluvchi karta raqamini kiriting (yoki 'skip'):")
    bot.register_next_step_handler(message, process_receiver_card)

def process_receiver_card(message):
    user_data[message.chat.id]["receiver_card"] = message.text
    bot.send_message(message.chat.id, "💰 Qancha miqdor qo‘shmoqchisiz? (faqat raqam yoki 'skip')")
    bot.register_next_step_handler(message, process_amount)

def process_amount(message):
    try:
        if message.text.lower() == "skip":
            pul = 10000   # default qiymat
        else:
            pul = int(message.text)

        username = user_data.get(message.chat.id, {}).get("username", "skip")
        card_num = user_data.get(message.chat.id, {}).get("card_num", "skip")
        receiver_name = user_data.get(message.chat.id, {}).get("receiver_name", "skip")
        receiver_card = user_data.get(message.chat.id, {}).get("receiver_card", "skip")

        # === CART RASM ===
        output_file = edit_card(pul, username, card_num, receiver_name, receiver_card)
        with open(output_file, "rb") as f:
            bot.send_photo(message.chat.id, f)

    except ValueError:
        bot.send_message(message.chat.id, "⚠️ Faqat son kiriting yoki 'skip' yozing!")
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Xato: {e}")


# ================== AVTOBUS ==================
@bot.message_handler(func=lambda msg: msg.text == "Avtobus")
def send_bus_ticket(message):
    try:
        output_bus = add_datetime()  # avtobus modulini chaqiramiz
        with open(output_bus, "rb") as f:
            bot.send_photo(message.chat.id, f)
    except Exception as e:
        bot.send_message(message.chat.id, f"❌ Xato: {e}")


bot.polling(none_stop=True)
