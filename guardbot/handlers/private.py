from ..config import bot, sudo_username, channel_username
from ..utils.language import lang
from ..utils.redisdb import rdb

""" Private Management Handlers """
from tgbotapi.types import InlineKeyboardMarkup, InlineKeyboardButton


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
        user_until_date = lang(rdb.hget(user_id, 'language_code'))[
            't_user_until_date_cap1']
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
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['t_choose'],
                         reply_markup=gen_help(), parse_mode='HTML',
                         disable_web_page_preview=True)
    elif call.data == 's_back':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(un=user_firstname, su=sudo_username, cu=channel_username),
                         reply_markup=gen_start(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 's_lang':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['t_choose'], reply_markup=gen_lang(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 'h_group':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['h_group'], reply_markup=gen_group(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_channel':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['h_channel'], reply_markup=gen_channel(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_private':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['h_private'], reply_markup=gen_private(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 's_main':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(un=user_firstname, su=sudo_username, cu=channel_username),
                         reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_back':
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['t_choose'], reply_markup=gen_help(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 'l_ar':
        rdb.hset(user_id, 'language_code', 'ar')
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(
            un=user_firstname, su=sudo_username, cu=channel_username), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'l_en':
        rdb.hset(user_id, 'language_code', 'en')
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(
            un=user_firstname, su=sudo_username, cu=channel_username), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'l_sp':
        rdb.hset(user_id, 'language_code', 'sp')
        bot.delete_message(chat_id, message_id)
        bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(
            un=user_firstname, su=sudo_username, cu=channel_username), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'p_id':
        if None != user_lastname:
            user_fullname = str(user_firstname) + ' ' + str(user_lastname)
        else:
            user_fullname = str(user_firstname)
        user_photos_ids = bot.get_user_profile_photos(user_id)
        if user_photos_ids.total_count == 0:
            bot.delete_message(chat_id, message_id)
            bot.send_message(chat_id, text=lang(rdb.hget(user_id, 'language_code'))['t_info_p_user'].format(fn=user_fullname,
                                                                                                            un=user_username, id=user_id),
                             parse_mode='HTML', reply_markup=gen_private())
        else:
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            bot.delete_message(chat_id, message_id)
            bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id,
                           caption=lang(rdb.hget(user_id, 'language_code'))['t_info_p_user'].format(fn=user_fullname, un=user_username,
                                                                                                    id=user_id),
                           reply_markup=gen_private(),
                           parse_mode="HTML")

    else:
        return None


def gen_start():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=str(lang('en')['b_help']), callback_data="s_help"),
               InlineKeyboardButton(text=str(lang('en')['b_support']), url='https://t.me/grid9x'))
    markup.add(InlineKeyboardButton(text=str(lang('en')['b_ch_lang']), callback_data='s_lang'))
    return markup


def gen_help():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=lang('en')[
               'b_channel'], callback_data='h_channel'))
    markup.add(InlineKeyboardButton(text=lang(
        'en')['b_group'], callback_data='h_group'))
    markup.add(InlineKeyboardButton(text=lang('en')[
               'b_private'], callback_data='h_private'))
    markup.add(InlineKeyboardButton(text=lang(
        'en')['b_back'], callback_data='s_back'))
    return markup


def gen_lang():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text='العربية 🇮🇶', callback_data='l_ar'))
    markup.add(InlineKeyboardButton(text='English 🌎', callback_data='l_en'))
    markup.add(InlineKeyboardButton(text='española 🌎', callback_data='l_sp'))
    markup.add(InlineKeyboardButton(text=lang('en')
                                    ['b_back'], callback_data='s_back'))
    return markup


def gen_channel():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=lang('en')['b_back'], callback_data='h_back'),
               InlineKeyboardButton(text=lang('en')['b_main'], callback_data='s_main'))
    return markup


def gen_group():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=lang('en')[
               'b_add'], url='http://t.me/gu9rdbot?startgroup'))
    markup.add(InlineKeyboardButton(text=lang('en')['b_back'], callback_data='h_back'),
               InlineKeyboardButton(text=lang('en')['b_main'], callback_data='s_main'))
    return markup


def gen_private():
    markup = InlineKeyboardMarkup()
    markup.add(InlineKeyboardButton(text=lang(
        'en')['b_id'], callback_data='p_id'))
    markup.add(InlineKeyboardButton(text=lang('en')['b_back'], callback_data='h_back'),
               InlineKeyboardButton(text=lang('en')['b_main'], callback_data='s_main'))
    return markup


# start message.
@bot.message_handler(commands=lang('en')['t_start'])
def start(message):
    chat_type = message.chat.type
    user_firstname = message.from_user.first_name
    user_id = message.from_user.id
    rdb.hset(user_id, 'language_code', message.from_user.language_code)
    if chat_type == 'private':
        bot.send_message(chat_id=message.chat.id, text=lang(rdb.hget(user_id, 'language_code'))['start_msg'].format(un=user_firstname, su=sudo_username, cu=channel_username),
                         reply_markup=gen_start(), parse_mode='HTML',
                         disable_web_page_preview=False)
    else:
        return None


# By send 'help' or /help
@bot.message_handler(commands=lang('en')['t_help'])
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_help'])
def replay_help(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_type == 'private':
        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                     'h_private'], parse_mode='HTML')
    elif chat_type in ['group', 'supergroup']:
        for x in bot.get_chat_administrators(chat_id):
            rdb.hset(chat_id, x.user.id, x.status)
        gcsm, gcsmm, gcsp, gcsom, gcawpp, gcci, gciu, gcpm = get_chat_permissions(
            chat_id)
        if rdb.hget(chat_id, user_id) == 'creator':
            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['creator_help'].format(
                gcsm=gcsm, gcsmm=gcsmm, gcsp=gcsp, gcsom=gcsom, gcawpp=gcawpp, gcci=gcci, gciu=gciu, gcpm=gcpm), parse_mode='HTML')
        else:
            if rdb.hget(chat_id, user_id) == 'administrator':
                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['admin_help'].format(
                    gcsm=gcsm, gcsmm=gcsmm, gcsp=gcsp, gcsom=gcsom, gcawpp=gcawpp, gcci=gcci, gciu=gciu, gcpm=gcpm), parse_mode='HTML')
            else:
                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                             'member_help'], parse_mode='HTML')
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)


# Replay user info
@bot.message_handler(commands=lang('en')['t_info'])
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_info'])
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

    if chat_type in ['private']:
        user_photos_ids = bot.get_user_profile_photos(user_id)
        if user_photos_ids.total_count == 0:
            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_p_user'].format(
                fn=user_fullname, un=user_username, id=user_id), parse_mode='HTML')
        else:
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=lang(rdb.hget(user_id, 'language_code'))[
                           't_info_p_user'].format(fn=user_fullname, un=user_username, id=user_id), reply_to_message_id=msg_id, parse_mode="HTML")
    elif chat_type in ['group', 'supergroup']:
        for x in bot.get_chat_administrators(chat_id):
            rdb.hset(chat_id, x.user.id, x.status)
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_firstname = message.reply_to_message.from_user.first_name
            target_user_username = message.reply_to_message.from_user.username
            target_user_lastname = message.reply_to_message.from_user.last_name
            target_user_status = get_user_permissions(
                chat_id, target_user_id)[0]
            target_user_until_date = get_user_permissions(
                chat_id, target_user_id)[2]
            tcbe = get_user_permissions(chat_id, target_user_id)[4]
            tcdm = get_user_permissions(chat_id, target_user_id)[7]
            tcru = get_user_permissions(chat_id, target_user_id)[8]
            tcpu = get_user_permissions(chat_id, target_user_id)[9]
            tcci = get_user_permissions(chat_id, target_user_id)[10]
            tciu = get_user_permissions(chat_id, target_user_id)[11]
            tcpm = get_user_permissions(chat_id, target_user_id)[12]
            tcsm = get_user_permissions(chat_id, target_user_id)[13]
            tcsmm = get_user_permissions(chat_id, target_user_id)[14]
            tcsp = get_user_permissions(chat_id, target_user_id)[-3]
            tcsom = get_user_permissions(chat_id, target_user_id)[16]
            tcawpp = get_user_permissions(chat_id, target_user_id)[17]
            if None != target_user_lastname:
                target_user_fullname = str(
                    target_user_firstname) + ' ' + str(target_user_lastname)
            else:
                target_user_fullname = str(target_user_firstname)
            target_photos_ids = bot.get_user_profile_photos(target_user_id)
            if rdb.hget(chat_id, user_id) in ['creator', 'administrator']:
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_creator'].format(fn=target_user_fullname,
                                                                                                                     un=target_user_username,
                                                                                                                     id=target_user_id,
                                                                                                                     us=target_user_status),
                                     parse_mode='HTML')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(user_id, 'language_code'))['t_info_creator'].format(fn=target_user_fullname,
                                                                                                                 un=target_user_username,
                                                                                                                 id=target_user_id,
                                                                                                                 us=target_user_status),
                                       reply_to_message_id=msg_id,
                                       parse_mode='HTML')
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_admin'].format(fn=target_user_fullname,
                                                                                                                   un=target_user_username,
                                                                                                                   id=target_user_id,
                                                                                                                   us=target_user_status,
                                                                                                                   cbe=tcbe, ciu=tciu,
                                                                                                                   cru=tcru, cpu=tcpu,
                                                                                                                   cpm=tcpm, cdm=tcdm,
                                                                                                                   cci=tcci),
                                     parse_mode='HTML')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(user_id, 'language_code'))['t_info_admin'].format(fn=target_user_fullname,
                                                                                                               un=target_user_username,
                                                                                                               id=target_user_id,
                                                                                                               us=target_user_status,
                                                                                                               cbe=tcbe, ciu=tciu,
                                                                                                               cru=tcru, cpu=tcpu,
                                                                                                               cpm=tcpm, cdm=tcdm,
                                                                                                               cci=tcci),
                                       reply_to_message_id=msg_id,
                                       parse_mode='HTML')
                else:
                    if target_photos_ids.total_count == 0:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_member'].format(fn=target_user_fullname,
                                                                                                                    un=target_user_username,
                                                                                                                    id=target_user_id,
                                                                                                                    us=target_user_status,
                                                                                                                    ud=target_user_until_date,
                                                                                                                    uciu=tciu, ucsm=tcsm,
                                                                                                                    ucsp=tcsp, ucsmm=tcsmm,
                                                                                                                    ucsom=tcsom, ucci=tcci,
                                                                                                                    ucpm=tcpm, ucawpp=tcawpp),
                                     parse_mode='HTML')
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(user_id, 'language_code'))['t_info_member'].format(fn=target_user_fullname,
                                                                                                                un=target_user_username,
                                                                                                                id=target_user_id,
                                                                                                                us=target_user_status,
                                                                                                                ud=target_user_until_date,
                                                                                                                uciu=tciu, ucsm=tcsm,
                                                                                                                ucsp=tcsp, ucsmm=tcsmm,
                                                                                                                ucsom=tcsom, ucci=tcci,
                                                                                                                ucpm=tcpm, ucawpp=tcawpp),
                                       reply_to_message_id=msg_id,
                                       parse_mode='HTML')
            else:
                if target_photos_ids.total_count == 0:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_user'].format(fn=target_user_fullname,
                                                                                                              un=target_user_username,
                                                                                                              id=target_user_id,
                                                                                                              us=target_user_status),
                                 parse_mode='HTML')
                else:
                    target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=target_latest_photo_id,
                                   caption=lang(rdb.hget(user_id, 'language_code'))['t_info_user'].format(fn=target_user_fullname,
                                                                                                          un=target_user_username,
                                                                                                          id=target_user_id,
                                                                                                          us=target_user_status),
                                   reply_to_message_id=msg_id,
                                   parse_mode='HTML')
        else:
            if None != user_lastname:
                user_fullname = str(user_firstname) + ' ' + str(user_lastname)
            else:
                user_fullname = str(user_firstname)
            us = get_user_permissions(chat_id, user_id)[0]
            ud = get_user_permissions(chat_id, user_id)[2]
            cbe = get_user_permissions(chat_id, user_id)[4]
            cdm = get_user_permissions(chat_id, user_id)[7]
            cru = get_user_permissions(chat_id, user_id)[8]
            cpu = get_user_permissions(chat_id, user_id)[9]
            cci = get_user_permissions(chat_id, user_id)[10]
            ciu = get_user_permissions(chat_id, user_id)[11]
            cpm = get_user_permissions(chat_id, user_id)[12]
            csm = get_user_permissions(chat_id, user_id)[13]
            csmm = get_user_permissions(chat_id, user_id)[14]
            csp = get_user_permissions(chat_id, user_id)[-3]
            csom = get_user_permissions(chat_id, user_id)[16]
            cawpp = get_user_permissions(chat_id, user_id)[17]
            user_photos_ids = bot.get_user_profile_photos(user_id)
            if rdb.hget(chat_id, user_id) == 'creator':
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_creator'].format(
                        fn=user_fullname, un=user_username, id=user_id, us=us), parse_mode='HTML')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=lang(rdb.hget(user_id, 'language_code'))['t_info_creator'].format(
                        fn=user_fullname, un=user_username, id=user_id, us=us), reply_to_message_id=msg_id, parse_mode="HTML")
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_admin'].format(
                        fn=user_fullname, un=user_username, id=user_id, us=us, cbe=cbe, ciu=ciu, cru=cru, cpu=cpu, cpm=cpm, cdm=cdm, cci=cci), parse_mode='HTML')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=lang(rdb.hget(user_id, 'language_code'))['t_info_admin'].format(
                        ffn=user_fullname, un=user_username, id=user_id, us=us, cbe=cbe, ciu=ciu, cru=cru, cpu=cpu, cpm=cpm, cdm=cdm, cci=cci), reply_to_message_id=msg_id, parse_mode="HTML")
            else:
                if user_photos_ids.total_count == 0:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_info_member'].format(
                        fn=user_fullname, un=user_username, id=user_id, us=us, ud=ud, cpm=cpm, csm=csm, csmm=csmm, csom=csom, csp=csp, cawpp=cawpp, ciu=ciu, cci=cci), parse_mode='HTML')
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(chat_id=chat_id, photo=user_latest_photo_id, caption=lang(rdb.hget(user_id, 'language_code'))['t_info_member'].format(
                        fn=user_fullname, un=user_username, id=user_id, us=us, ud=ud, cpm=cpm, csm=csm, csmm=csmm, csom=csom, csp=csp, cawpp=cawpp, ciu=ciu, cci=cci), reply_to_message_id=msg_id, parse_mode="HTML")
    elif chat_type in ['channel']:
        pass
    else:
        print('UNKOWN CHAT TYPE: ', chat_type)
