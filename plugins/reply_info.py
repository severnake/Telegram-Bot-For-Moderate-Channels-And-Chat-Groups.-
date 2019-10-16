from plugins.cfgbot import bot

''' reply_info module '''


@bot.message_handler(func=lambda message:
                message.text =='id' or 
                message.text=='ID' or 
                message.text=='info' or 
                message.text=='INFO'
                    )
def replay_info_str(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_full_name = str(user_first_name) + " " + str(user_last_name)

    reply_id = message.chat.id
    msg_id = message.message_id
    user_photos_ids = bot.get_user_profile_photos(user_id)
    user_latest_photo_id = user_photos_ids.photos[0][0].file_id


    bot.send_photo(chat_id=reply_id, 
                photo=user_latest_photo_id, 
                caption="*FullName:* {}\n*UserName:* @{}\n*ID:* `{}`".format(
                    user_full_name, user_name, user_id),
                reply_to_message_id= msg_id, 
                parse_mode="markdown",)


@bot.message_handler(commands=['id', 'ID', 'info', 'INFO'])
def replay_info_cmd(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_full_name = str(user_first_name) + " " + str(user_last_name)

    reply_id = message.chat.id
    msg_id = message.message_id
    user_photos_ids = bot.get_user_profile_photos(user_id)
    user_latest_photo_id = user_photos_ids.photos[0][0].file_id


    bot.send_photo(chat_id=reply_id, 
                photo=user_latest_photo_id, 
                caption="*FullName:* {}\n*UserName:* @{}\n*ID:* `{}`".format(
                    user_full_name, user_name, user_id),
                reply_to_message_id= msg_id, 
                parse_mode="markdown",)