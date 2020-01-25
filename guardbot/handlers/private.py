from ..config import bot, channel_username
from ..config import creators_ids, admins_ids, vusers_ids, vusers_info
""" Private Management Handlers """
from telebotapi.types import InlineKeyboardMarkup, InlineKeyboardButton

start_msg = "*Welcome!* 🎉\
                    \nI'm here to manage your\
                    \nchannels and chat groups\
                    \njust add me to it 👀 \
                    \n\nthis bot made with `telebotapi`\
                    \ncheck it at `PYPI` 🔰 \
                    \nhttps://pypi.org/project/telebotapi \
                    \n\nFor activation contact ⤵️ \
                    \n@MA24th 🛠 - @grid9x ⚙️ "

private_help = "*Help Menu* 📋\
                    \n============\
                    \n/start : start message\
                    \n/id : replay your info"
creators_help = "*Help Menu* 📋\
                    \n============\
                    \n`ban`: replay to msg user\
                    \n`unban`: replay to msg user\
                    \n`kick`: replay to msg user\
                    \n`kickme`: send `kickme`\
                    \n`pin`: replay to msg\
                    \n`unpin`: send `unpin`"
admin_help = "*Help Menu* 📋\
                    \n============\
                    \n`ban`: replay to msg user\
                    \n`unban`: replay to msg user\
                    \n`kick`: replay to msg user\
                    \n`kickme`: send `kickme`\
                    \n`pin`: replay to msg\
                    \n`unpin`: send `unpin`"
member_help = "*Help Menu* 📋\
                    \n============\
                    \n`kickme`: send `kickme`\
                    \n`pin`: replay to msg\
                    \n`unpin`: send `unpin`"


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):

    if call.data == "s_help":
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, private_help, reply_markup=gen_help(), parse_mode='markdown',
                         disable_web_page_preview=True)
    elif call.data == 'h_back':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, start_msg, reply_markup=gen_start(), parse_mode='markdown',
                         disable_web_page_preview=False)
    elif call.data == 's_lang':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, 'Make a Choose', reply_markup=gen_lang(), parse_mode='markdown',
                         disable_web_page_preview=True)
    elif call.data == 'l_back':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, start_msg, reply_markup=gen_start(), parse_mode='markdown',
                         disable_web_page_preview=False)
    elif call.data == 'h_add':
        bot.answer_callback_query(call.id, 'Under Development')
    elif call.data == 'l_en':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, start_msg, reply_markup=gen_start(), parse_mode='markdown',
                         disable_web_page_preview=False)
    elif call.data == 'l_ar':
        bot.delete_message(call.message.chat.id, call.message.message_id)
        bot.send_message(call.message.chat.id, start_msg, reply_markup=gen_start(), parse_mode='markdown',
                         disable_web_page_preview=False)
    else:
        return None


def gen_start():
    markup = InlineKeyboardMarkup()
    markup.row_width = 6
    markup.add(InlineKeyboardButton('Help 📋', callback_data="s_help"),
               InlineKeyboardButton('Support ⚙️', callback_data="s_support", url='https://t.me/grid9x'))
    markup.add(InlineKeyboardButton('Choose a language 🌍', callback_data='s_lang'))
    return markup


def gen_help():
    markup = InlineKeyboardMarkup()
    markup.row_width = 6
    markup.add(InlineKeyboardButton('Add Me 👥', callback_data='h_add'))
    markup.add(InlineKeyboardButton('Back ↩️', callback_data='h_back'))
    return markup


def gen_lang():
    markup = InlineKeyboardMarkup()
    markup.row_width = 6
    markup.add(InlineKeyboardButton('العربية 🇮🇶', callback_data='l_ar'))
    markup.add(InlineKeyboardButton('English 🌎', callback_data='l_en'))
    markup.add(InlineKeyboardButton('Back ↩️', callback_data='l_back'))
    return markup


# start message.
@bot.message_handler(commands=['start'])
def start(message):
    chat_type = message.chat.type
    if chat_type == 'private':
        bot.send_message(message.chat.id, start_msg, reply_markup=gen_start(), parse_mode='markdown',
                         disable_web_page_preview=False)
    else:
        return None


# By send 'help' or /help
@bot.message_handler(commands=['help', 'Help'])
@bot.message_handler(func=lambda message: message.text == 'help' or message.text == 'Help')
def reply_help(message):
    chat_type = message.chat.type
    user_id = message.from_user.id
    if chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status
        if status_msg == 'left' and user_id not in vusers_ids:
            vusers_info.append(chat_member_info.user)
            vusers_ids.append(user_id)
            msg_join = f'_Please_ \nJoin {channel_username} First'
            bot.reply_to(message, text=msg_join, parse_mode='markdown')
        else:
            bot.reply_to(message, text=private_help, parse_mode='markdown')
    elif chat_type == 'group' or chat_type == 'supergroup':
        chat_id = message.chat.id
        chat_admins = bot.get_chat_administrators(chat_id)
        for x in chat_admins:
            if x.status == 'creator':
                creators_ids.append(x.user.id)
            elif x.status == 'administrator':
                admins_ids.append(x.user.id)
        if user_id in creators_ids:
            bot.reply_to(message, text=creators_help, parse_mode='markdown')
        elif user_id in chat_admins:
            bot.reply_to(message, text=admin_help, parse_mode='markdown')
        else:
            bot.reply_to(message, text=member_help, parse_mode='markdown')
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)


# Replay user info if user send id.
@bot.message_handler(commands=['id', 'Id'])
@bot.message_handler(func=lambda message: message.text == 'id' or message.text == 'Id')
def replay_info(message):
    user_id = message.from_user.id
    user_username = message.from_user.username
    user_firstname = message.from_user.first_name
    user_lastname = message.from_user.last_name
    user_fullname = str(user_firstname) + " " + str(user_lastname)
    chat_id = message.chat.id
    chat_type = message.chat.type
    msg_id = message.message_id
    if chat_type == 'group' or chat_type == 'supergroup':
        user_photos_ids = bot.get_user_profile_photos(user_id)
        if user_photos_ids.total_count == 0:
            caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
            bot.reply_to(message, caption, parse_mode='markdown')
        else:
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
            bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=caption, reply_to_message_id=msg_id,
                           parse_mode="markdown")
    elif chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status
        if status_msg == 'left' and user_id not in vusers_ids:
            vusers_info.append(chat_member_info.user)
            vusers_ids.append(user_id)
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
                bot.reply_to(message, caption, parse_mode='markdown')
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=caption, reply_to_message_id=msg_id,
                               parse_mode="markdown")
        else:
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
                bot.reply_to(message, caption, parse_mode='markdown')
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                caption = f"*Fullname:* {user_fullname}\n*Username:* @{user_username}\n*ID:* `{user_id}`"
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=caption, reply_to_message_id=msg_id,
                               parse_mode="markdown")
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)
