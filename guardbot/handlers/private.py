from ..config import bot, sun, cun
from ..utils.language import lang
from ..utils.redisdb import rdb

""" Private Management Handlers """
from tgbotapi.types import InlineKeyboardMarkup, InlineKeyboardButton


def get_chat_permissions(chat_id):
    chat_permissions = bot.get_chat(chat_id).permissions
    cp = {}
    if chat_permissions.can_send_messages:
        cp['cms'] = '✅'
    else:
        cp['cms'] = '❌'
    if chat_permissions.can_send_media_messages:
        cp['csmm'] = '✅'
    else:
        cp['csmm'] = '❌'
    if chat_permissions.can_send_polls:
        cp['csp'] = '✅'
    else:
        cp['csp'] = '❌'
    if chat_permissions.can_send_other_messages:
        cp['csom'] = '✅'
    else:
        cp['csom'] = '❌'
    if chat_permissions.can_add_web_page_previews:
        cp['cawpp'] = '✅'
    else:
        cp['cawpp'] = '❌'
    if chat_permissions.can_change_info:
        cp['cci'] = '✅'
    else:
        cp['cci'] = '❌'
    if chat_permissions.can_invite_users:
        cp['ciu'] = '✅'
    else:
        cp['ciu'] = '❌'
    if chat_permissions.can_pin_messages:
        cp['cpm'] = '✅'
    else:
        cp['cpm'] = '❌'
    return cp


def get_user_permissions(chat_id, user_id):
    user_permissions = bot.get_chat_member(chat_id, user_id)
    cm = {'us': user_permissions.status, 'uct': user_permissions.custom_title, 'uim': user_permissions.is_member}
    if user_permissions.until_date == 0 or None:
        cm['cud'] = lang(rdb.hget(user_id, 'language_code'))['t_user_until_date_cap1']
    else:
        cm['cud'] = user_permissions.until_date
    if user_permissions.can_be_edited:
        cm['cbe'] = '✅'
    else:
        cm['cbe'] = '❌'
    if user_permissions.can_post_messages:
        cm['cpom'] = '✅'
    else:
        cm['cpom'] = '❌'
    if user_permissions.can_edit_messages:
        cm['cem'] = '✅'
    else:
        cm['cem'] = '❌'
    if user_permissions.can_delete_messages:
        cm['cdm'] = '✅'
    else:
        cm['cdm'] = '❌'
    if user_permissions.can_restrict_members:
        cm['crm'] = '✅'
    else:
        cm['crm'] = '❌'
    if user_permissions.can_promote_members:
        cm['cpmm'] = '✅'
    else:
        cm['cpmm'] = '❌'
    if user_permissions.can_change_info:
        cm['cci'] = '✅'
    else:
        cm['cci'] = '❌'
    if user_permissions.can_invite_users:
        cm['ciu'] = '✅'
    else:
        cm['ciu'] = '❌'
    if user_permissions.can_pin_messages:
        cm['cpm'] = '✅'
    else:
        cm['cpm'] = '❌'
    if user_permissions.can_send_messages:
        cm['csm'] = '✅'
    else:
        cm['csm'] = '❌'
    if user_permissions.can_send_media_messages:
        cm['csmm'] = '✅'
    else:
        cm['csmm'] = '❌'
    if user_permissions.can_send_polls:
        cm['csp'] = '✅'
    else:
        cm['csp'] = '❌'
    if user_permissions.can_send_other_messages:
        cm['csom'] = '✅'
    else:
        cm['csom'] = '❌'
    if user_permissions.can_add_web_page_previews:
        cm['cawpp'] = '✅'
    else:
        cm['cawpp'] = '❌'
    return cm


@bot.callback_query_handler(func=lambda call: True)
def callback_query(call):
    message_id = call.message.message_id
    cid = call.message.chat.id
    uid = call.from_user.id
    uun = call.from_user.username
    ufn = call.from_user.first_name
    user_lastname = call.from_user.last_name
    if call.data == "s_help":
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_choose'],
                         reply_markup=gen_help(), parse_mode='HTML',
                         disable_web_page_preview=True)
    elif call.data == 's_back':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(uun=ufn, su=sun, cu=cun),
                         reply_markup=gen_start(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 's_lang':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_choose'], reply_markup=gen_lang(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 'h_group':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['h_group'], reply_markup=gen_group(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_channel':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['h_channel'], reply_markup=gen_channel(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_private':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['h_private'], reply_markup=gen_private(),
                         parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 's_main':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(uun=ufn, su=sun, cu=cun),
                         reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'h_back':
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_choose'], reply_markup=gen_help(), parse_mode='HTML',
                         disable_web_page_preview=False)
    elif call.data == 'l_ar':
        rdb.hset(uid, 'language_code', 'ar')
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(
            uun=ufn, su=sun, cu=cun), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'l_en':
        rdb.hset(uid, 'language_code', 'en')
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(
            uun=ufn, su=sun, cu=cun), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'l_sp':
        rdb.hset(uid, 'language_code', 'sp')
        bot.delete_message(cid, message_id)
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(
            uun=ufn, su=sun, cu=cun), reply_markup=gen_start(), parse_mode='HTML', disable_web_page_preview=False)
    elif call.data == 'p_id':
        if None != user_lastname:
            ufulln = str(ufn) + ' ' + str(user_lastname)
        else:
            ufulln = str(ufn)
        user_photos_ids = bot.get_user_profile_photos(uid)
        if user_photos_ids.total_count == 0:
            bot.delete_message(cid, message_id)
            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_p_user'].format(ufulln, uun, uid),
                             parse_mode='HTML', reply_markup=gen_private())
        else:
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            bot.delete_message(cid, message_id)
            bot.send_photo(cid, photo=user_latest_photo_id,
                           caption=lang(rdb.hget(uid, 'language_code'))['t_info_p_user'].format(ufulln, uun, uid),
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
    ctype = message.chat.type
    cid = message.chat.id
    ufn = message.from_user.first_name
    uid = message.from_user.id
    rdb.hset(uid, 'language_code', message.from_user.language_code)
    if ctype == 'private':
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['start_msg'].format(uun=ufn, su=sun, cu=cun),
                         reply_markup=gen_start(), parse_mode='HTML',
                         disable_web_page_preview=False)
    else:
        return None


# By send 'help' or /help
@bot.message_handler(commands=lang('en')['t_help'])
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_help'])
def replay_help(message):
    ctype = message.chat.type
    cid = message.chat.id
    uid = message.from_user.id
    mid = message.message_id
    if ctype == 'private':
        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['h_private'], parse_mode='HTML', reply_to_message_id=mid)
    elif ctype in ['group', 'supergroup']:
        for x in bot.get_chat_administrators(cid):
            rdb.hset(cid, x.user.id, x.status)
        cp = get_chat_permissions(cid)
        if rdb.hget(cid, uid) == 'creator':
            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['creator_help'].format(
                csm=cp['csm'], csmm=cp['csmm'], csp=cp['csp'], csom=cp['csom'], cawpp=cp['cawpp'], cci=cp['cci'], ciu=cp['ciu'], cpm=cp['cpm']), parse_mode='HTML', reply_to_message_id=mid)
        else:
            if rdb.hget(cid, uid) == 'administrator':
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['admin_help'].format(
                    csm=cp['csm'], csmm=cp['csmm'], csp=cp['csp'], csom=cp['csom'], cawpp=cp['cawpp'], cci=cp['cci'], ciu=cp['ciu'], cpm=cp['cpm']), parse_mode='HTML', reply_to_message_id=mid)
            else:
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                             'member_help'], parse_mode='HTML', reply_to_message_id=mid)
    else:
        print('UNKOWN CHAT TYPE: ', ctype)


# Replay user info
@bot.message_handler(commands=lang('en')['t_info'])
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_info'])
def replay_info(message):
    mid = message.message_id
    cid = message.chat.id
    ctype = message.chat.type
    uid = message.from_user.id
    uun = message.from_user.username
    ufn = message.from_user.first_name
    user_lastname = message.from_user.last_name
    if None != user_lastname:
        ufulln = str(ufn) + ' ' + str(user_lastname)
    else:
        ufulln = str(ufn)

    if ctype in ['private']:
        user_photos_ids = bot.get_user_profile_photos(uid)
        if user_photos_ids.total_count == 0:
            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_p_user'].format(
                fn=ufulln, uun=uun, id=uid), parse_mode='HTML', reply_to_message_id=mid)
        else:
            user_latest_photo_id = user_photos_ids.photos[0][0].file_id
            bot.send_photo(cid, photo=user_latest_photo_id, caption=lang(rdb.hget(uid, 'language_code'))[
                           't_info_p_user'].format(fn=ufulln, uun=uun, id=uid), reply_to_message_id=mid, parse_mode="HTML")
    elif ctype in ['group', 'supergroup']:
        for x in bot.get_chat_administrators(cid):
            rdb.hset(cid, x.user.id, x.status)
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            tfn = message.reply_to_message.from_user.first_name
            tun = message.reply_to_message.from_user.username
            tln = message.reply_to_message.from_user.last_name
            tp = get_user_permissions(cid, tid)
            if None != tln:
                tfulln = str(
                    tfn) + ' ' + str(tln)
            else:
                tfulln = str(tfn)
            target_photos_ids = bot.get_user_profile_photos(tid)
            if rdb.hget(cid, uid) in ['creator', 'administrator']:
                if rdb.hget(cid, tid) == 'creator':
                    if target_photos_ids.total_count == 0:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_creator'].format(tfulln, uun=tun, uid=tid, us=tp['us']),
                                     parse_mode='HTML', reply_to_message_id=mid)
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(cid, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(uid, 'language_code'))['t_info_creator'].format(tfulln, uun=tun, uid=tid, us=tp['us']),
                                       reply_to_message_id=mid,
                                       parse_mode='HTML')
                elif rdb.hget(cid, tid) == 'administrator':
                    if target_photos_ids.total_count == 0:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_admin'].format(tfulln, uun=tun, uid=tid, us=tp['us'], cbe=tp['cbe'], ciu=tp['ciu'], cru=tp['cru'], cpu=tp['cpu'], cpm=tp['cpm'], cdm=tp['cdm'], cci=tp['cci']),
                                     parse_mode='HTML', reply_to_message_id=mid)
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(cid, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(uid, 'language_code'))['t_info_admin'].format(tfulln, uun=tun, uid=tid, us=tp['us'], cbe=tp['cbe'], ciu=tp['ciu'], cru=tp['cru'], cpu=tp['cpu'], cpm=tp['cpm'], cdm=tp['cdm'], cci=tp['cci']),
                                       reply_to_message_id=mid,
                                       parse_mode='HTML')
                else:
                    if target_photos_ids.total_count == 0:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_member'].format(tfulln,
                                                                                                                    uun=tun,
                                                                                                                    id=tid,
                                                                                                                    us=tp['us'],
                                                                                                                    ud=tp['un'],
                                                                                                                    ciu=tp['ciu'], csm=tp['csm'],
                                                                                                                    csp=tp['csp'], csmm=tp['csmm'],
                                                                                                                    csom=tp['csom'], cci=tp['cci'],
                                                                                                                    cpm=tp['cpm'], cawpp=tp['cawpp']),
                                     parse_mode='HTML', reply_to_message_id=mid)
                    else:
                        target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                        bot.send_photo(cid, photo=target_latest_photo_id,
                                       caption=lang(rdb.hget(uid, 'language_code'))['t_info_member'].format(tfulln,
                                                                                                                    uun=tun,
                                                                                                                    id=tid,
                                                                                                                    us=tp['us'],
                                                                                                                    ud=tp['un'],
                                                                                                                    ciu=tp['ciu'], csm=tp['csm'],
                                                                                                                    csp=tp['csp'], csmm=tp['csmm'],
                                                                                                                    csom=tp['csom'], cci=tp['cci'],
                                                                                                                    cpm=tp['cpm'], cawpp=tp['cawpp']),
                                       reply_to_message_id=mid,
                                       parse_mode='HTML')
            else:
                if target_photos_ids.total_count == 0:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_user'].format(tfulln, uun=tun, uid=tid, us=tp['us']),
                                 parse_mode='HTML', reply_to_message_id=mid)
                else:
                    target_latest_photo_id = target_photos_ids.photos[0][0].file_id
                    bot.send_photo(cid, photo=target_latest_photo_id,
                                   caption=lang(rdb.hget(uid, 'language_code'))['t_info_user'].format(tfulln, uun=tun, uid=tid, us=tp['us']),
                                   reply_to_message_id=mid,
                                   parse_mode='HTML')
        else:
            if None != user_lastname:
                ufulln = str(ufn) + ' ' + str(user_lastname)
            else:
                ufulln = str(ufn)
            up = get_user_permissions(cid, uid)
            user_photos_ids = bot.get_user_profile_photos(uid)
            if rdb.hget(cid, uid) == 'creator':
                if user_photos_ids.total_count == 0:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_creator'].format(
                        ufulln, uun, uid, us=up['us']), parse_mode='HTML', reply_to_message_id=mid)
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(cid, photo=user_latest_photo_id, caption=lang(rdb.hget(uid, 'language_code'))['t_info_creator'].format(
                        ufulln, uun, uid, us=up['us']), reply_to_message_id=mid, parse_mode="HTML")
            elif rdb.hget(cid, uid) == 'administrator':
                if user_photos_ids.total_count == 0:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_admin'].format(
                        ufulln, uun, uid, us=up['us'], cbe=up['cbe'], ciu=up['ciu'], cru=up['cru'], cpu=up['cpu'], cpm=up['cpm'], cdm=up['cdm'], cci=up['cci']), parse_mode='HTML', reply_to_message_id=mid)
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(cid, photo=user_latest_photo_id, caption=lang(rdb.hget(uid, 'language_code'))['t_info_admin'].format(
                        ufulln, uun, uid, us=up['us'], cbe=up['cbe'], ciu=up['ciu'], cru=up['cru'], cpu=up['cpu'], cpm=up['cpm'], cdm=up['cdm'], cci=up['cci']), reply_to_message_id=mid, parse_mode="HTML")
            else:
                if user_photos_ids.total_count == 0:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_info_member'].format(
                        ufulln, uun, uid, us=up['us'], cbe=up['cbe'], ciu=up['ciu'], cru=up['cru'], cpu=up['cpu'], cpm=up['cpm'], cdm=up['cdm'], cci=up['cci']), parse_mode='HTML', reply_to_message_id=mid)
                else:
                    user_latest_photo_id = user_photos_ids.photos[0][0].file_id
                    bot.send_photo(cid, photo=user_latest_photo_id, caption=lang(rdb.hget(uid, 'language_code'))['t_info_member'].format(
                        ufulln, uun, uid, us=up['us'], cbe=up['cbe'], ciu=up['ciu'], cru=up['cru'], cpu=up['cpu'], cpm=up['cpm'], cdm=up['cdm'], cci=up['cci']), reply_to_message_id=mid, parse_mode="HTML")
    elif ctype in ['channel']:
        pass
    else:
        print('UNKOWN CHAT TYPE: ', ctype)
