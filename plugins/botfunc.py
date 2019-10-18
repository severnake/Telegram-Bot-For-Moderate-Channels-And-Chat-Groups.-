from plugins.botcfg import bot
from plugins.botcfg import creators_ids, admins_ids, know_user_id
from plugins.botcfg import sudo_username, channel_username, know_user_info

''' Bot Function Plugin '''

# start message.
@bot.message_handler(commands=['start'])
def bot_start_cmd(message):
    chat_type = message.chat.type
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name

    user_full_name = str(user_first_name) + " " + str(user_last_name)
    if chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status
        if status_msg == 'left' and user_id not in know_user_id:
            know_user_info.append(chat_member_info.user)
            know_user_id.append(user_id)
            msg_join = f'_Please_ \nJoin {channel_username} First'
            bot.reply_to(message, text=msg_join, parse_mode='markdown')
        else:
            msg_start = f"*Welcome {user_full_name}*\
                        \nI'm here to manage your\
                        \nchannels and chat groups\
                        \nthis bot made with `telebotapi`\
                        \ncheck it at [PYPI](https://pypi.org/project/telebotapi/)\
                        \n\nFor activation contact\n {sudo_username} - {channel_username} "
            bot.reply_to(message, text=msg_start, parse_mode='markdown')


# Help
help_msg_creator = "*Creator*👨‍💼👩‍💼 *Help Menu* 📋\
                     =================\
                    \n`ban`: replay to msg user\
                    \n`unban`: replay to msg user\
                    \n`kick`: replay to msg user\
                    \n`kickme`: send `kickme`\
                    \n`pin`: replay to msg\
                    \n`unpin`: send `unpin`"

help_msg_admin = "*Admin*👨‍🔧👩‍🔧 *Help Menu* 📋\
                  ===============\
                    \n`ban`: replay to msg user\
                    \n`unban`: replay to msg user\
                    \n`kick`: replay to msg user\
                    \n`kickme`: send `kickme`\
                    \n`pin`: replay to msg\
                    \n`unpin`: send `unpin`"

help_msg_member = "*Member*👨‍🦱👩‍🦰 *Help Menu* 📋\
                   ================\
                    \n`kickme`: send `kickme`\
                    \npin: replay to msg\
                    \nunpin: send `unpin`"

help_msg_private = f"*Welcome {bot_start_cmd.user_full_name}*\
                \nI'm here to manage your\
                \nchannels and chat groups\
                \nthis bot made with `telebotapi`\
                \ncheck it at [PYPI](https://pypi.org/project/telebotapi)\
                \n\nFor activation contact\n {sudo_username} - {channel_username}"

# By send str 'help' or /help
@bot.message_handler(commands=['help'])
@bot.message_handler(func=lambda message: message.text == 'help')
def reply_help(message):

    chat_type = message.chat.type

    if chat_type == 'group' or chat_type == 'supergroup':
        chat_id = message.chat.id
        chat_admins = bot.get_chat_administrators(chat_id)
        user_id = message.from_user.id

        for x in chat_admins:
            if x.status == 'creator':
                creators_ids.append(x.user.id)
            elif x.status == 'administrator':
                admins_ids.append(x.user.id)

        if user_id in creators_ids:
            bot.reply_to(message, text=help_msg_creator, parse_mode='markdown')
        elif user_id in chat_admins:
            bot.reply_to(message, text=help_msg_admin, parse_mode='markdown')
        elif user_id not in admins_ids:
            bot.reply_to(message, text=help_msg_member, parse_mode='markdown')

    elif chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status
        if status_msg == 'left' and user_id not in know_user_id:
            know_user_info.append(chat_member_info.user)
            know_user_id.append(user_id)
            msg_join = f'_Please_ \nJoin {channel_username} First'
            bot.reply_to(message, text=msg_join, parse_mode='markdown')
        else:

            bot.reply_to(message, text=help_msg_private, parse_mode='markdown')


# Replay user info if user send id or info.
@bot.message_handler(commands=['id', 'info'])
@bot.message_handler(func=lambda message: message.text == 'id' or message.text == 'info')
def replay_info(message):
    user_id = message.from_user.id
    user_name = message.from_user.username
    user_first_name = message.from_user.first_name
    user_last_name = message.from_user.last_name
    user_full_name = str(user_first_name) + " " + str(user_last_name)
    chat_id = message.chat.id
    chat_type = message.chat.type
    msg_id = message.message_id

    if chat_type == 'group' or chat_type == 'supergroup':
        user_photos_ids = bot.get_user_profile_photos(user_id)
        user_latest_photo_id = user_photos_ids.photos[0][0].file_id
        caption = f"*FullName:* {user_full_name}\n*UserName:* @{user_name}\n*ID:* `{user_id}`"
        bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                       caption=caption, reply_to_message_id=msg_id, parse_mode="markdown")

    elif chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status

        if status_msg == 'left' and user_id not in know_user_id:
            know_user_info.append(chat_member_info.user)
            know_user_id.append(user_id)
            user_photos_ids = bot.get_user_profile_photos(user_id)
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            caption = f"*FullName:* {user_full_name}\n*UserName:* @{user_name}\n*ID:* `{user_id}`"
            bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                           caption=caption, reply_to_message_id=msg_id, parse_mode="markdown")

        else:
            user_photos_ids = bot.get_user_profile_photos(user_id)
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            caption = f"*FullName:* {user_full_name}\n*UserName:* @{user_name}\n*ID:* `{user_id}`"
            bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                           caption=caption, reply_to_message_id=msg_id, parse_mode="markdown")
