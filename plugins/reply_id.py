from plugins.cfgbot import bot

''' reply_id module '''


@bot.message_handler(commands=["id", "ID"])
def send_id_cmd(message):
    user_id = message.chat.id
    user_name = message.from_user.username
    user_full_name = str(message.from_user.first_name) + " " + str(message.from_user.last_name)

    bot.reply_to(message, text="*FullName: {}\nUserName: {}\nID: {}".format(user_full_name, user_name, user_id),
                 parse_mode="markedown")


@bot.message_handler(func=lambda message: message.text == "ايدي")
def send_id_str(message):
    user_id = message.chat.id
    user_name = message.from_user.username
    user_full_name = str(message.from_user.first_name) + " " + str(message.from_user.last_name)

    bot.reply_to(message, text="*FullName: {}\nUserName: {}\nID: {}".format(user_full_name, user_name, user_id),
                 parse_mode="markedown")