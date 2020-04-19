from ..config import bot, sun, cun, bids
from ..utils.language import lang
from ..utils.redisdb import rdb

"""" Groups Management Handler """


@bot.message_handler(content_type=['new_chat_members'])
def new_chat_members(message):
    """
    Add user status to rdb
    """
    cid = message.chat.id
    for new_chat_member in message.new_chat_members:
        rdb.hset(cid, new_chat_member.id, 'member')
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.user.status)


@bot.message_handler(content_type=['left_chat_member'])
def left_chat_member(message):
    """
    if chat member left and chat member in administrator list then delete from rdb.
    """
    cid = message.chat.id
    uid = message.from_user.id
    if rdb.hexists(cid, uid):
        rdb.hdel(cid, uid)


# Ban user by replay to user msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_ban'])
def ban_user(message):
    mid = message.message_id
    ctype = message.chat.type
    cid = message.chat.id
    uid = message.from_user.id
    if ctype == 'group' or ctype == 'supergroup':
        until_date = None
        for x in bot.get_chat_administrators(cid):
            rdb.hset(cid, x.user.id, x.user.status)
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            tun = message.reply_to_message.from_user.username
            if rdb.hget(cid, uid) == 'creator':
                if rdb.hget(cid, tid) == 'creator':
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_ban_cap3'], reply_to_message_id=mid)
                elif rdb.hget(cid, tid) == 'administrator':
                    if tid in bids:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_ban_cap2'], reply_to_message_id=mid)
                    else:
                        bot.kick_chat_member(
                            cid, tid, until_date)
                        rdb.hdel(cid, tid)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_ban_cap1'].format(tun), reply_to_message_id=mid)
                elif tid in bids:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_ban_cap2'], reply_to_message_id=mid)
                else:
                    bot.kick_chat_member(cid, tid, until_date)
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_ban_cap1'].format(tun), reply_to_message_id=mid)
            elif rdb.hget(cid, uid) == 'administrator':
                if rdb.hget(cun, tid) == 'creator':
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_ban_cap5'].format(sun), reply_to_message_id=mid)
                elif rdb.hget(cid, tid) == 'administrator':
                    if tid in bids:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_ban_cap4'].format(sun), reply_to_message_id=mid)
                    else:
                        if bot.get_chat_member(cid, uid).can_restrict_members:
                            bot.kick_chat_member(
                                cid, tid, until_date)
                            rdb.hdel(cid, tid)
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                             't_ban_cap1'].format(tun), reply_to_message_id=mid)
                        else:
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                             't_ban_cap6'].format(sun, tun), reply_to_message_id=mid)
                elif tid in bids:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_ban_cap4'].format(tun), reply_to_message_id=mid)
                else:
                    if bot.get_chat_member(cid, uid).can_restrict_members:
                        bot.kick_chat_member(
                            cid, tid, until_date)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_ban_cap1'].format(tun), reply_to_message_id=mid)
                    else:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_ban_cap7'].format(tun), reply_to_message_id=mid)
            else:
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                 't_piv_admin'], reply_to_message_id=mid)
        # elif message.entities:
        #     if message.entities[0].type == 'mention':
        #         if '@' in message.text:
        #             target_username = message.text[3:]
        #             bot.get_chat_member()

        else:
            pass
    else:
        pass


# Unban user by replay to user msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_unban'])
def unban_user(message):
    mid = message.message_id
    ctype = message.chat.type
    cid = message.chat.id
    uid = message.from_user.id
    if ctype == 'group' or ctype == 'supergroup':
        for x in bot.get_chat_administrators(cid):
            rdb.hset(cid, x.user.id, x.status)
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            tun = message.reply_to_message.from_user.username
            if rdb.hget(cid, uid) == 'creator':
                if tid not in rdb.hgetall(cid) and tid not in bids:
                    bot.unban_chat_member(cid, tid)
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                        't_unban_cap1'].format(tun), reply_to_message_id=mid)
            elif rdb.hget(cid, uid) == 'administrator':
                if tid not in rdb.hgetall(cid) and tid not in bids:
                    if bot.get_chat_member(cid, uid).can_restrict_members:
                        bot.unban_chat_member(cid, tid)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                            't_unban_cap1'].format(tun), reply_to_message_id=mid)
                    else:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                            't_unban_cap7'].format(tun), reply_markup=mid)
                else:
                    pass
            else:
                bot.send_message(cid, text=lang(
                    rdb.hget(uid, 'language_code'))['t_piv_admin'], reply_to_message_id=mid)
        else:
            pass
    else:
        pass


# Kick user by replay to user msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_kick'])
def kick_user(message):
    mid = message.message_id
    ctype = message.chat.type
    cid = message.chat.id
    uid = message.from_user.id
    until_date = 35
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if ctype == 'group' or ctype == 'supergroup':
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            target_username = message.reply_to_message.from_user.username
            if rdb.hget(cid, uid) == 'creator':
                if rdb.hget(cid, tid) == 'creator':
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                        't_kick_cap3'].format(target_username), reply_to_message_id=mid)
                elif rdb.hget(cid, tid) == 'administrator':
                    if tid in bids:
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                            't_kick_cap2'].format(target_username), reply_to_message_id=mid)
                    else:
                        bot.kick_chat_member(
                            cid, tid, until_date)
                        bot.unban_chat_member(cid, tid)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                            't_sup_cap1'].format(target_username), reply_to_message_id=mid)
                elif tid in bids:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                        't_kick_cap2'].format(target_username), reply_to_message_id=mid)
                else:
                    bot.kick_chat_member(cid, tid, until_date)
                    bot.unban_chat_member(cid, tid)
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                        't_kick_cap1'].format(target_username), reply_to_message_id=mid)
            elif rdb.hget(cid, uid) == 'administrator':
                if rdb.hget(cid, tid) == 'creator':
                    bot.send_message(cid, text=lang(
                        rdb.hget(uid, 'language_code'))['t_kick_cap5'], reply_to_message_id=mid)
                elif rdb.hget(cid, tid) == 'administrator':
                    if tid in bids:
                        bot.send_message(cid, text=lang(
                            rdb.hget(uid, 'language_code'))['t_kick_cap4'], reply_to_message_id=mid)
                    else:
                        bot.kick_chat_member(
                            cid, tid, until_date)
                        bot.unban_chat_member(cid, tid)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_kick_cap1'].format(target_username), reply_to_message_id=mid)
                elif tid in bids:
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_kick_cap4'], reply_to_message_id=mid)
                else:
                    bot.kick_chat_member(cid, tid, until_date)
                    bot.unban_chat_member(cid, tid)
                    bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                     't_kick_cap1'].format(target_username), reply_to_message_id=mid)
            else:
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                 't_piv_admin'], reply_to_message_id=mid)
        else:
            pass
    else:
        pass


# Kickme by send 'kickme' msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_kickme'])
def kickme_user(message):
    mid = message.message_id
    ctype = message.chat.type
    cid = message.chat.id
    uid = message.from_user.id
    user_name = message.from_user.username
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if not message.reply_to_message:
        if ctype == 'group' or ctype == 'supergroup':
            if rdb.hexists(cid, uid):
                pass
            else:
                bot.kick_chat_member(cid, uid)
                bot.unban_chat_member(cid, uid)
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                    't_kickme_cap1'].format(user_name), reply_to_message_id=mid)
    else:
        pass


# Pin msg by replay to msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_pin'])
def pin_msg(message):
    mid = message.message_id
    cid = message.chat.id
    uid = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(cid).permissions.can_pin_messages
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if message.reply_to_message:
        mid = message.reply_to_message.message_id
        if rdb.hget(cid, uid) == 'creator':
            bot.pin_chat_message(cid, mid)
        elif rdb.hget(cid, uid) == 'administrator':
            if can_pin_messages:
                bot.pin_chat_message(cid, mid)
            else:
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                 't_pin_cap1'].format(user_username), reply_to_message_id=mid)
        else:
            if can_pin_messages:
                bot.pin_chat_message(cid, mid)
            else:
                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                 't_pin_cap1'].format(user_username), reply_to_message_id=mid)


# Unpin by send msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_unpin'])
def unpin_msg(message):
    mid = message.message_id
    cid = message.chat.id
    uid = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(cid).permissions.can_pin_messages
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if rdb.hget(cid, uid) == 'creator':
        bot.unpin_chat_message(cid)
    elif rdb.hget(cid, uid) == 'administrator':
        if can_pin_messages:
            bot.unpin_chat_message(cid)
        else:
            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                             't_unpin_cap1'].format(user_username), reply_to_message_id=mid)
    else:
        if can_pin_messages:
            bot.unpin_chat_message(cid)
        else:
            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                             't_unpin_cap1'].format(user_username), reply_to_message_id=mid)


# promote a member to admin
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_promote'])
def promote_member_to_admin(message):
    mid = message.message_id
    cid = message.chat.id
    ctype = message.chat.type
    uid = message.from_user.id
    can_promote_members = bot.get_chat_member(cid, uid).can_promote_members
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if ctype == 'supergroup' or ctype == 'group':
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            tun = message.reply_to_message.from_user.username
            if rdb.hget(cid, uid) == 'creator':
                if rdb.hget(cid, tid) == 'creator':
                    pass
                elif rdb.hget(cid, tid) == 'administrator':
                    pass
                elif tid in bids:
                    pass
                else:
                    if ctype == 'supergroup':
                        bot.promote_chat_member(cid, tid, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                                can_promote_members=True)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_promote_cap1'].format(tun), reply_to_message_id=mid)
                    elif ctype == 'group':
                        bot.promote_chat_member(cid, tid, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True,
                                                can_promote_members=True)
                        bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                         't_promote_cap1'].format(tun), reply_to_message_id=mid)
                    else:
                        pass
            elif rdb.hget(cid, uid) == 'administrator':
                if can_promote_members:
                    if rdb.hget(cid, tid) == 'creator':
                        pass
                    elif rdb.hget(cid, tid) == 'administrator':
                        pass
                    elif tid in bids:
                        pass
                    else:
                        if ctype == 'supergroup':
                            bot.promote_chat_member(cid, tid, can_change_info=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True, can_restrict_members=True,
                                                    can_pin_messages=True,
                                                    can_promote_members=True)
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                             't_promote_cap1'].format(tun), reply_to_message_id=mid)
                        elif ctype == 'group':
                            bot.promote_chat_member(cid, tid, can_change_info=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True, can_restrict_members=True,
                                                    can_promote_members=True)
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))[
                                             't_promote_cap1'].format(tun), reply_to_message_id=mid)
                        else:
                            pass
            else:
                pass
    else:
        pass


# demote a member to admin
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_demote'])
def demote_member_to_admin(message):
    mid = message.message_id
    cid = message.chat.id
    ctype = message.chat.type
    uid = message.from_user.id
    can_promote_members = bot.get_chat_member(cid, uid).can_promote_members
    for x in bot.get_chat_administrators(cid):
        rdb.hset(cid, x.user.id, x.status)
    if ctype == 'supergroup' or ctype == 'group':
        if message.reply_to_message:
            tid = message.reply_to_message.from_user.id
            tun = message.reply_to_message.from_user.username
            if rdb.hget(cid, uid) == 'creator':
                if rdb.hget(cid, tid) == 'creator':
                    pass
                elif rdb.hget(cid, tid) == 'administrator':
                    if tid in bids:
                        pass
                    else:
                        if ctype == 'supergroup':
                            bot.promote_chat_member(cid, tid, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_pin_messages=False,
                                                    can_promote_members=False)
                            rdb.hdel(cid, tid)
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_demote_cap1'].format(
                                tun), reply_to_message_id=mid)
                        elif ctype == 'group':
                            bot.promote_chat_member(cid, tid, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_promote_members=False)
                            rdb.hdel(cid, tid)
                            bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_demote_cap1'].format(
                                tun), reply_to_message_id=mid)
                        else:
                            pass
                elif tid in bids:
                    pass
                else:
                    pass
            elif rdb.hget(cid, uid) == 'administrator':
                if can_promote_members:
                    if rdb.hget(cid, tid) == 'creator':
                        pass
                    elif rdb.hget(cid, tid) == 'administrator':
                        if tid in bids:
                            pass
                        else:
                            if ctype == 'supergroup':
                                bot.promote_chat_member(cid, tid, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_pin_messages=False,
                                                        can_promote_members=True)
                                rdb.hdel(cid, uid)
                                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_promote_cap1'].format(
                                    tun), reply_to_message_id=mid)
                            elif ctype == 'group':
                                bot.promote_chat_member(cid, tid, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_promote_members=False)
                                rdb.hdel(cid, uid)
                                bot.send_message(cid, text=lang(rdb.hget(uid, 'language_code'))['t_promote_cap1'].format(
                                    tun), reply_to_message_id=mid)
                            else:
                                pass
            else:
                pass
    else:
        pass


# chat permissions


# user permissions
# can_send_messages by replay to user msg
# @bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_user_can_send_messages'])
# def user_can_send_messages(message):
#     cid = message.chat.id
#     ctype = message.chat.type
#     uid = message.from_user.id
#     if ctype in ['group', 'supergroup']:
#         chat_admins = bot.get_chat_administrators(cid)
#         for x in chat_admins:
#             if x.status == 'creator':
#                 creators_ids.append(x.user.id)
#             elif x.status == 'administrator':
#                 admins_ids.append(x.user.id)
#         if message.reply_to_message:
#             tid = message.reply_to_message.from_user.id
#             tun = message.reply_to_message.from_user.username
#             en = lang(rdb.hget(uid, 'language_code'))['t_enable']
#             if en == message.text[18:24]:
#                 until_date = message.text[26:]
#                 if 's' in until_date:
#                     until_date = until_date[:uid]
#                 elif 'm' in until_date:
#                     until_date = until_date[:uid]
#                     until_date = until_date * 60
#                 elif 'h' in until_date:
#                     until_date = until_date[:uid]
#                     until_date = 60 * (until_date * 60)
#                 else:
#                     until_date = int(until_date)
#                 if rdb.hget(cid, uid) == 'creator':
#                     if rdb.hget(cid, tid) == 'creator':
#                         pass
#                     elif rdb.hget(cid, tid) == 'administrator':
#                         if tid in bids:
#                             pass
#                         else:
#                             bot.restrict_chat_member(cid, tid, until_date, can_send_messages=True)
#                             rdb.hdel(cid, uid)
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 tun))
#                     elif tid in bids:
#                         pass
#                     else:
#                         bot.restrict_chat_member(cid, tid, until_date, can_send_messages=True)
#                         bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                             tun))
#                 elif rdb.hget(cid, uid) == 'administrator':
#                     can_restrict_members = bot.get_chat_member(cid, uid).can_restrict_members
#                     if rdb.hget(cid, tid) == 'creator':
#                         pass
#                     elif rdb.hget(cid, tid) == 'administrator':
#                         if tid in bids:
#                             pass
#                         else:
#                             if can_restrict_members:
#                                 bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                                 bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                     tun))
#                             else:
#                                 bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                     sun, tun))
#                     elif tid in bids:
#                         pass
#                     else:
#                         if can_restrict_members:
#                             bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 tun))
#                         else:
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                 tun))
#                 else:
#                     bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_piv_admin'])
#             di = lang(rdb.hget(uid, 'language_code'))['t_disable']
#             if di in message.text[18:25]:
#                 until_date = message.text[26:]
#                 if 's' in until_date:
#                     until_date = until_date[:uid]
#                 elif 'm' in until_date:
#                     until_date = until_date[:uid]
#                     until_date = until_date * 60
#                 elif 'h' in until_date:
#                     until_date = until_date[:uid]
#                     until_date = 60 * (until_date * 60)
#                 else:
#                     until_date = int(until_date)
#                 if rdb.hget(cid, uid) == 'creator':
#                     if rdb.hget(cid, tid) == 'creator':
#                         pass
#                     elif rdb.hget(cid, tid) == 'administrator':
#                         if tid in bids:
#                             pass
#                         else:
#                             bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                             rdb.hdel(cid, uid)
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 tun))
#                     elif tid in bids:
#                         pass
#                     else:
#                         bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                         bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                             tun))
#                 elif rdb.hget(cid, uid) == 'administrator':
#                     can_restrict_members = bot.get_chat_member(cid, uid).can_restrict_members
#                     if rdb.hget(cid, tid) == 'creator':
#                         pass
#                     elif rdb.hget(cid, tid) == 'administrator':
#                         if tid in bids:
#                             pass
#                         else:
#                             if can_restrict_members:
#                                 bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                                 bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                     tun))
#                             else:
#                                 bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                     sun, tun))
#                     elif tid in bids:
#                         pass
#                     else:
#                         if can_restrict_members:
#                             bot.restrict_chat_member(cid, tid, until_date, can_send_messages=False)
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 tun))
#                         else:
#                             bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                 tun))
#                 else:
#                     bot.reply_to(message, text=lang(rdb.hget(uid, 'language_code'))['t_piv_admin'])
#         else:
#             pass
#     else:
#         pass
