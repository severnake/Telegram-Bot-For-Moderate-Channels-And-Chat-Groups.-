from ..config import bot, channel_username, lang
from ..config import creators_ids, admins_ids, vusers_ids, vusers_info
from ..utils.language import ch_lang

""" Private Management Handlers """
from telebotapi.plugins import InlineKeyboardMarkup, InlineKeyboardButton


def get_chat_permissions(chat_id):
    chat_permissions = bot.get_chat(chat_id).permissions
    if chat_permissions.can_send_messages:
        gcsm = '✅'
    else:
        gcsm = '❌'
    if chat_permissions.can_send_media_messages:
        gcsmm = '✅'
    else:
        gcsmm = '❌'
    if chat_permissions.can_send_polls:
        gcsp = '✅'
    else:
        gcsp = '❌'
    if chat_permissions.can_send_other_messages:
        gcsom = '✅'
    else:
        gcsom = '❌'
    if chat_permissions.can_add_web_page_previews:
        gcawpp = '✅'
    else:
        gcawpp = '❌'
    if chat_permissions.can_change_info:
        gcci = '✅'
    else:
        gcci = '❌'
    if chat_permissions.can_invite_users:
        gciu = '✅'
    else:
        gciu = '❌'
    if chat_permissions.can_pin_messages:
        gcpm = '✅'
    else:
        gcpm = '❌'
    return gcsm, gcsmm, gcsp, gcsom, gcawpp, gcci, gciu, gcpm


def get_user_permissions(chat_id, user_id):
    user_permissions = bot.get_chat_member(chat_id, user_id)
    user_status = user_permissions.status
    user_custom_title = user_permissions.custom_title
    if user_permissions.until_date == 0:
        user_until_date = ch_lang(lang[-1])['t_user_until_date_cap1']
    else:
        user_until_date = user_permissions.until_date
    user_is_member = user_permissions.is_member
    if user_permissions.can_be_edited:
        ucbe = '✅'
    else:
        ucbe = '❌'
    if user_permissions.can_post_messages:
        ucppm = '✅'
    else:
        ucppm = '❌'
    if user_permissions.can_edit_messages:
        ucem = '✅'
    else:
        ucem = '❌'
    if user_permissions.can_delete_messages:
        ucdm = '✅'
    else:
        ucdm = '❌'
    if user_permissions.can_restrict_members:
        ucru = '✅'
    else:
        ucru = '❌'
    if user_permissions.can_promote_members:
        ucpu = '✅'
    else:
        ucpu = '❌'
    if user_permissions.can_change_info:
        ucci = '✅'
    else:
        ucci = '❌'
    if user_permissions.can_invite_users:
        uciu = '✅'
    else:
        uciu = '❌'
    if user_permissions.can_pin_messages:
        ucpm = '✅'
    else:
        ucpm = '❌'
    if user_permissions.can_send_messages:
        ucsm = '✅'
    else:
        ucsm = '❌'
    if user_permissions.can_send_media_messages:
        ucsmm = '✅'
    else:
        ucsmm = '❌'
    if user_permissions.can_send_polls:
        ucsp = '✅'
    else:
        ucsp = '❌'
    if user_permissions.can_send_other_messages:
        ucsom = '✅'
    else:
        ucsom = '❌'
    if user_permissions.can_add_web_page_previews:
        ucawpp = '✅'
    else:
        ucawpp = '❌'
    return user_status, user_custom_title, user_until_date, user_is_member, ucbe, ucppm, ucem, ucdm, ucru, ucpu, ucci, \
           uciu, ucpm, ucsm, ucsmm, ucsp, ucsom, ucawpp


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message_id = call.message.message_id
    chat_id = call.message.chat.id
    user_id = call.from_user.id
    user_username = call.from_user.username
    user_firstname = call.from_user.first_name
    user_lastname = call.from_user.last_name
    if call.data == "s_help":
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(lang[-1])['t_choose'],
                         reply_markup=gen_help(), parse_mode='MarkdownV2',
                         disable_web_page_preview=True)
    elif call.data == 's_back':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['start_msg'].format(user_firstname),
                         reply_markup=gen_start(), parse_mode='Markdown',
                         disable_web_page_preview=False)
    elif call.data == 's_lang':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(lang[-1])['t_choose'], reply_markup=gen_lang(), parse_mode='Markdown',
                         disable_web_page_preview=False)
    elif call.data == 'h_group':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['h_group'], reply_markup=gen_sub_help(),
                         parse_mode='Markdown', disable_web_page_preview=False)
    elif call.data == 'h_channel':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['h_channel'], reply_markup=gen_sub_help(),
                         parse_mode='Markdown', disable_web_page_preview=False)
    elif call.data == 'h_private':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['h_private'], reply_markup=gen_private(),
                         parse_mode='MarkdownV2', disable_web_page_preview=False)
    elif call.data == 's_main':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['start_msg'].format(user_firstname),
                         reply_markup=gen_start(), parse_mode='Markdown', disable_web_page_preview=False)
    elif call.data == 'h_back':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(lang[-1])['t_choose'], reply_markup=gen_help(), parse_mode='MarkdownV2',
                         disable_web_page_preview=False)
    elif call.data == 'h_add':
        bot.answer_callback_query(call.id, text=ch_lang(user_lang=lang[-1])['t_dev'])
    elif call.data == 'l_en':
        lang.append('en')
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['start_msg'].format(user_firstname),
                         reply_markup=gen_start(), parse_mode='Markdown', disable_web_page_preview=False)
    elif call.data == 'l_ar':
        lang.append('ar')
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=ch_lang(user_lang=lang[-1])['start_msg'], reply_markup=gen_start(),
                         parse_mode='Markdown', disable_web_page_preview=False)
    elif call.data == 'p_id':
        if None != user_lastname:
            user_fullname = str(user_firstname) + ' ' + str(user_lastname)
        else:
            user_fullname = str(user_firstname)
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        user_status = chat_member_info.status
        if user_status == 'left' and user_id not in vusers_ids:
            vusers_info.append(chat_member_info.user)
            vusers_ids.append(user_id)
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                bot.delete_message(chat_id, message_id)
                bot.send_message(chat_id, text=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname,
                                                                                         un=user_username, id=user_id),
                                 parse_mode='MarkdownV2', reply_markup=gen_private())
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                bot.delete_message(chat_id, message_id)
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                               caption=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                 id=user_id),
                               reply_markup=gen_private(),
                               parse_mode="MarkdownV2")
        else:
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                bot.delete_message(chat_id, message_id)
                bot.send_message(chat_id, text=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname,
                                                                                         un=user_username, id=user_id),
                                 parse_mode='MarkdownV2', reply_markup=gen_private())
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                bot.delete_message(chat_id, message_id)
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                               caption=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                 id=user_id),
                               reply_markup=gen_private(),
                               parse_mode="MarkdownV2")

    else:
        return None


def gen_start():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=str(ch_lang(lang[-1])['b_help']), callback_data="s_help"),
               InlineKeyboardButton(text=str(ch_lang(lang[-1])['b_support']), callback_data="s_support",
                                    url='https://t.me/grid9x'))
    markup.add(InlineKeyboardButton(text=str(ch_lang(lang[-1])['b_ch_lang']), callback_data='s_lang'))
    return markup


def gen_help():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_channel'], callback_data='h_channel'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_group'], callback_data='h_group'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_private'], callback_data='h_private'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_back'], callback_data='s_back'))
    return markup


def gen_sub_help():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_add'], callback_data='h_add'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_back'], callback_data='h_back'),
               InlineKeyboardButton(text=ch_lang(lang[-1])['b_main'], callback_data='s_main'))
    return markup


def gen_lang():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='العربية 🇮🇶', callback_data='l_ar'))
    markup.add(InlineKeyboardButton(text='English 🌎', callback_data='l_en'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_back'], callback_data='s_back'))
    return markup


def gen_private():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_id'], callback_data='p_id'))
    markup.add(InlineKeyboardButton(text=ch_lang(lang[-1])['b_back'], callback_data='h_back'),
               InlineKeyboardButton(text=ch_lang(lang[-1])['b_main'], callback_data='s_main'))
    return markup


# start message.
@bot.message_handler(commands=ch_lang(lang[-1])['t_start'])
def start(message):
    chat_type = message.chat.type
    user_firstname = message.from_user.first_name
    if chat_type == 'private':
        bot.send_message(chat_id=message.chat.id, text=ch_lang(user_lang=lang[-1])['start_msg'].format(user_firstname),
                         reply_markup=gen_start(), parse_mode='Markdown',
                         disable_web_page_preview=False)
    else:
        return None


# By send 'help' or /help
@bot.message_handler(commands=ch_lang(lang[-1])['t_help'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_help'])
def replay_help(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_type == 'private':
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        status_msg = chat_member_info.status
        if status_msg == 'left' and user_id not in vusers_ids:
            vusers_info.append(chat_member_info.user)
            vusers_ids.append(user_id)
            bot.reply_to(message, text=ch_lang(lang[-1])['msg_join'].format(channel_username), parse_mode='MarkdownV2')
        else:
            bot.reply_to(message, text=ch_lang(lang[-1])['private_help'], parse_mode='MarkdownV2')
    elif chat_type in ['group', 'supergroup']:
        chat_admins = bot.get_chat_administrators(chat_id)
        for x in chat_admins:
            if x.status == 'creator':
                creators_ids.append(x.user.id)
            elif x.status == 'administrator':
                admins_ids.append(x.user.id)
        gcsm, gcsmm, gcsp, gcsom, gcawpp, gcci, gciu, gcpm = get_chat_permissions(chat_id)
        if user_id in creators_ids:
            bot.reply_to(message, text=ch_lang(lang[-1])['creator_help'].format(gcsm=gcsm, gcsmm=gcsmm, gcsp=gcsp,
                                                                                gcsom=gcsom, gcawpp=gcawpp, gcci=gcci,
                                                                                gciu=gciu, gcpm=gcpm),
                         parse_mode='MarkdownV2')
        else:
            if user_id in chat_admins:
                bot.reply_to(message, text=ch_lang(lang[-1])['admin_help'].format(gcsm=gcsm, gcsmm=gcsmm, gcsp=gcsp,
                                                                                  gcsom=gcsom, gcawpp=gcawpp, gcci=gcci,
                                                                                  gciu=gciu, gcpm=gcpm),
                             parse_mode='MarkdownV2')
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['member_help'], parse_mode='MarkdownV2')
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)


# Replay user info
@bot.message_handler(commands=ch_lang(lang[-1])['t_info'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_info'])
def replay_info(message):
    msg_id = message.message_id
    chat_id = message.chat.id
    chat_type = message.chat.type
    user_id = message.from_user.id
    user_username = message.from_user.username
    user_firstname = message.from_user.first_name
    user_lastname = message.from_user.last_name
    if None != user_lastname:
        user_fullname = str(user_firstname) + ' ' + str(user_lastname)
    else:
        user_fullname = str(user_firstname)

    if chat_type in ['channel']:
        pass
    if chat_type in ['group', 'supergroup']:
        chat_admins = bot.get_chat_administrators(chat_id)
        for x in chat_admins:
            if x.status == 'creator':
                creators_ids.append(x.user.id)
            elif x.status == 'administrator':
                admins_ids.append(x.user.id)
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_firstname = message.reply_to_message.from_user.first_name
            target_user_username = message.reply_to_message.from_user.username
            target_user_lastname = message.reply_to_message.from_user.last_name
            tup = get_user_permissions(chat_id, target_user_id)
            target_user_status = tup[0]
            target_user_until_date = tup[2]
            tcbe = tup[4]
            tcdm = tup[7]
            tcru = tup[8]
            tcpu = tup[9]
            tcci = tup[10]
            tciu = tup[11]
            tcpm = tup[12]
            tcsm = tup[13]
            tcsmm = tup[14]
            tcsp = tup[-3]
            tcsom = tup[16]
            tcawpp = tup[17]
            if None != target_user_lastname:
                target_user_fullname = str(target_user_firstname) + ' ' + str(target_user_lastname)
            else:
                target_user_fullname = str(target_user_firstname)
            target_photos_ids = bot.get_user_profile_photos(target_user_id)
            if user_id in creators_ids or user_id in admins_ids:
                if target_user_id in creators_ids:
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_info_user'].format(fn=target_user_fullname,
                                                                                                un=target_user_username,
                                                                                                id=target_user_id,
                                                                                                us=target_user_status),
                                     parse_mode='MarkdownV2')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=ch_lang(lang[-1])['t_info_user'].format(fn=target_user_fullname,
                                                                                          un=target_user_username,
                                                                                          id=target_user_id,
                                                                                          us=target_user_status),
                                       reply_to_message_id=msg_id,
                                       parse_mode='MarkdownV2')
                elif target_user_id in admins_ids:
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_info_admin'].format(fn=target_user_fullname,
                                                                                              un=target_user_username,
                                                                                              id=target_user_id,
                                                                                              us=target_user_status,
                                                                                              cbe=tcbe, uciu=tciu,
                                                                                              ucru=tcru, ucpu=tcpu,
                                                                                              ucpm=tcpm, ucdm=tcdm,
                                                                                              ucci=tcci),
                                     parse_mode='MarkdownV2')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=ch_lang(lang[-1])['t_info_admin'].format(fn=target_user_fullname,
                                                                                              un=target_user_username,
                                                                                              id=target_user_id,
                                                                                              us=target_user_status,
                                                                                              cbe=tcbe, uciu=tciu,
                                                                                              ucru=tcru, ucpu=tcpu,
                                                                                              ucpm=tcpm, ucdm=tcdm,
                                                                                              ucci=tcci),
                                       reply_to_message_id=msg_id,
                                       parse_mode='MarkdownV2')
                else:
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_info_member'].format(fn=target_user_fullname,
                                                                                              un=target_user_username,
                                                                                              id=target_user_id,
                                                                                              us=target_user_status,
                                                                                              ud=target_user_until_date,
                                                                                              uciu=tciu, ucsm=tcsm,
                                                                                              ucsp=tcsp, ucsmm=tcsmm,
                                                                                              ucsom=tcsom, ucci=tcci,
                                                                                              ucpm=tcpm, ucawpp=tcawpp),
                                     parse_mode='MarkdownV2')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=ch_lang(lang[-1])['t_info_member'].format(fn=target_user_fullname,
                                                                                              un=target_user_username,
                                                                                              id=target_user_id,
                                                                                              us=target_user_status,
                                                                                              ud=target_user_until_date,
                                                                                              uciu=tciu, ucsm=tcsm,
                                                                                              ucsp=tcsp, ucsmm=tcsmm,
                                                                                              ucsom=tcsom, ucci=tcci,
                                                                                              ucpm=tcpm, ucawpp=tcawpp),
                                       reply_to_message_id=msg_id,
                                       parse_mode='MarkdownV2')
            else:
                if target_photos_ids.total_count == 0:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_info_user'].format(fn=target_user_fullname,
                                                                                       un=target_user_username,
                                                                                       id=target_user_id,
                                                                                       us=target_user_status),
                                 parse_mode='MarkdownV2')
                else:
                    target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                   caption=ch_lang(lang[-1])['t_info_user'].format(fn=target_user_fullname,
                                                                                      un=target_user_username,
                                                                                      id=target_user_id,
                                                                                      us=target_user_status),
                                   reply_to_message_id=msg_id,
                                   parse_mode='MarkdownV2')
        else:
            user_status = get_user_permissions(chat_id, user_id)[0]
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_id in creators_ids:
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message,
                                 text=ch_lang(lang[-1])['t_info_user'].format(fn=user_fullname, un=user_username,
                                                                              id=user_id, us=user_status),
                                 parse_mode='MarkdownV2')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                                   caption=ch_lang(lang[-1])['t_info_user'].format(fn=user_fullname, un=user_username,
                                                                                   id=user_id, us=user_status),
                                   reply_to_message_id=msg_id,
                                   parse_mode="MarkdownV2")
            elif user_id in admins_ids:
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message,
                                 text=ch_lang(lang[-1])['t_info_admin'].format(fn=user_fullname, un=user_username,
                                                                               id=user_id, us=user_status),
                                 parse_mode='MarkdownV2')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                                   caption=ch_lang(lang[-1])['t_info_admin'].format(fn=user_fullname, un=user_username,
                                                                                    id=user_id, us=user_status),
                                   reply_to_message_id=msg_id,
                                   parse_mode="MarkdownV2")
            else:
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message,
                                 text=ch_lang(lang[-1])['t_info_user'].format(fn=user_fullname, un=user_username,
                                                                              id=user_id, us=user_status),
                                 parse_mode='MarkdownV2')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                                   caption=ch_lang(lang[-1])['t_info_user'].format(fn=user_fullname, un=user_username,
                                                                                   id=user_id, us=user_status),
                                   reply_to_message_id=msg_id,
                                   parse_mode="MarkdownV2")
    elif chat_type in ['private']:
        chat_member_info = bot.get_chat_member(channel_username, user_id)
        user_status = chat_member_info.status
        if user_status == 'left' and user_id not in vusers_ids:
            vusers_info.append(chat_member_info.user)
            vusers_ids.append(user_id)
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                     id=user_id),
                             parse_mode='MarkdownV2')
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                               caption=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                 id=user_id),
                               reply_to_message_id=msg_id,
                               parse_mode="MarkdownV2")
        else:
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if user_photos_ids.total_count == 0:
                bot.reply_to(message,
                             text=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                     id=user_id),
                             parse_mode='MarkdownV2')
            else:
                user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                               caption=ch_lang(lang[-1])['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                     id=user_id),
                               reply_to_message_id=msg_id,
                               parse_mode="MarkdownV2")
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)
