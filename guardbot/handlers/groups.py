from ..config import bot, sudo_username, channel_username, bots_ids
from ..utils.language import lang
from ..utils.redisdb import rdb

"""" Groups Management Handler """

@bot.message_handler(content_type=['new_chat_members'])
def new_chat_members(message):
    """
    Add user status to rdb
    """
    chat_id = message.chat.id
    for new_chat_member in message.new_chat_members:
        rdb.hset(chat_id, new_chat_member.id, 'member')
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.user.status)


@bot.message_handler(content_type=['left_chat_member'])
def left_chat_member(message):
    """
    if chat member left and chat member in administrator list then delete from rdb.
    """
    chat_id = message.chat.id 
    user_id = message.from_user.id
    if rdb.hexists(chat_id, user_id):
        rdb.hdel(chat_id, user_id)


# Ban user by replay to user msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_ban'])
def ban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_type == 'group' or chat_type == 'supergroup':
        until_date = None
        for x in bot.get_chat_administrators(chat_id):
            rdb.hset(chat_id, x.user.id, x.user.status)
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if rdb.hget(chat_id, user_id) == 'creator':
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_ban_cap3'])
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=lang(
                            rdb.hget(user_id, 'language_code'))['t_ban_cap2'])
                    else:
                        bot.kick_chat_member(
                            chat_id, target_user_id, until_date)
                        rdb.hdel(chat_id, target_user_id)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_ban_cap1'].format(target_user_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=lang(
                        rdb.hget(user_id, 'language_code'))['t_ban_cap2'])
                else:
                    bot.kick_chat_member(chat_id, target_user_id, until_date)
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_ban_cap1'].format(target_user_username))
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if rdb.hget(channel_username, target_user_id) == 'creator':
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_ban_cap5'].format(sudo_username))
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_ban_cap4'].format(sudo_username))
                    else:
                        if bot.get_chat_member(chat_id, user_id).can_restrict_members:
                            bot.kick_chat_member(
                                chat_id, target_user_id, until_date)
                            rdb.hdel(chat_id, target_user_id)
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                         't_ban_cap1'].format(target_user_username))
                        else:
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                         't_ban_cap6'].format(sudo_username, target_user_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_ban_cap4'].format(target_user_username))
                else:
                    if bot.get_chat_member(chat_id, user_id).can_restrict_members:
                        bot.kick_chat_member(
                            chat_id, target_user_id, until_date)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_ban_cap1'].format(target_user_username))
                    else:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_ban_cap7'].format(target_user_username))
            else:
                bot.reply_to(message, text=lang(
                    rdb.hget(user_id, 'language_code'))['t_piv_admin'])
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
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    if chat_type == 'group' or chat_type == 'supergroup':
        for x in bot.get_chat_administrators(chat_id):
            rdb.hset(chat_id, x.user.id, x.status)
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if rdb.hget(chat_id, user_id) == 'creator':
                if target_user_id not in rdb.hgetall(chat_id) and target_user_id not in bots_ids:
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_unban_cap1'].format(target_user_username))
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if target_user_id not in rdb.hgetall(chat_id) and target_user_id not in bots_ids:
                    if bot.get_chat_member(chat_id, user_id).can_restrict_members:
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_unban_cap1'].format(target_user_username))
                    else:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_unban_cap7'].format(target_user_username))
                else:
                    pass
            else:
                bot.reply_to(message, text=lang(
                    rdb.hget(user_id, 'language_code'))['t_piv_admin'])
        else:
            pass
    else:
        pass


# Kick user by replay to user msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_kick'])
def kick_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    until_date = 35
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_username = message.reply_to_message.from_user.username
            if rdb.hget(chat_id, user_id) == 'creator':
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_kick_cap3'].format(target_username))
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_kick_cap2'].format(target_username))
                    else:
                        bot.kick_chat_member(
                            chat_id, target_user_id, until_date)
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_sup_cap1'].format(target_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_kick_cap2'].format(target_username))
                else:
                    bot.kick_chat_member(chat_id, target_user_id, until_date)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_kick_cap1'].format(target_username))
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    bot.reply_to(message, text=lang(
                        rdb.hget(user_id, 'language_code'))['t_kick_cap5'])
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=lang(
                            rdb.hget(user_id, 'language_code'))['t_kick_cap4'])
                    else:
                        bot.kick_chat_member(
                            chat_id, target_user_id, until_date)
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_kick_cap1'].format(target_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=lang(
                        rdb.hget(user_id, 'language_code'))['t_kick_cap4'])
                else:
                    bot.kick_chat_member(chat_id, target_user_id, until_date)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                 't_kick_cap1'].format(target_username))
            else:
                bot.reply_to(message, text=lang(
                    rdb.hget(user_id, 'language_code'))['t_piv_admin'])
        else:
            pass
    else:
        pass


# Kickme by send 'kickme' msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_kickme'])
def kickme_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_name = message.from_user.username
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if not message.reply_to_message:
        if chat_type == 'group' or chat_type == 'supergroup':
            if rdb.hexists(chat_id, user_id):
                pass
            else:
                bot.kick_chat_member(chat_id, user_id)
                bot.unban_chat_member(chat_id, user_id)
                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_kickme_cap1'].format(user_name))
    else:
        pass


# Pin msg by replay to msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_pin'])
def pin_msg(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(chat_id).permissions.can_pin_messages
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if message.reply_to_message:
        msg_id = message.reply_to_message.message_id
        if rdb.hget(chat_id, user_id) == 'creator':
            bot.pin_chat_message(chat_id, msg_id)
        elif rdb.hget(chat_id, user_id) == 'administrator':
            if can_pin_messages:
                bot.pin_chat_message(chat_id, msg_id)
            else:
                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                             't_pin_cap1'].format(user_username))
        else:
            if can_pin_messages:
                bot.pin_chat_message(chat_id, msg_id)
            else:
                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                             't_pin_cap1'].format(user_username))


# Unpin by send msg
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_unpin'])
def unpin_msg(message):
    chat_id = message.chat.id
    user_id = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(chat_id).permissions.can_pin_messages
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if rdb.hget(chat_id, user_id) == 'creator':
        bot.unpin_chat_message(chat_id)
    elif rdb.hget(chat_id, user_id) == 'administrator':
        if can_pin_messages:
            bot.unpin_chat_message(chat_id)
        else:
            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                         't_unpin_cap1'].format(user_username))
    else:
        if can_pin_messages:
            bot.unpin_chat_message(chat_id)
        else:
            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                         't_unpin_cap1'].format(user_username))


# promote a member to admin
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_promote'])
def promote_member_to_admin(message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    user_id = message.from_user.id
    can_promote_members = bot.get_chat_member(chat_id, user_id).can_promote_members
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if chat_type == 'supergroup' or chat_type == 'group':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if rdb.hget(chat_id, user_id) == 'creator':
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    pass
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    pass
                elif target_user_id in bots_ids:
                    pass
                else:
                    if chat_type == 'supergroup':
                        bot.promote_chat_member(chat_id, target_user_id, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                                can_promote_members=True)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_promote_cap1'].format(target_user_username))
                    elif chat_type == 'group':
                        bot.promote_chat_member(chat_id, target_user_id, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True,
                                                can_promote_members=True)
                        bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                     't_promote_cap1'].format(target_user_username))
                    else:
                        pass
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if can_promote_members:
                    if rdb.hget(chat_id, target_user_id) == 'creator':
                        pass
                    elif rdb.hget(chat_id, target_user_id) == 'administrator':
                        pass
                    elif target_user_id in bots_ids:
                        pass
                    else:
                        if chat_type == 'supergroup':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True, can_restrict_members=True,
                                                    can_pin_messages=True,
                                                    can_promote_members=True)
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                         't_promote_cap1'].format(target_user_username))
                        elif chat_type == 'group':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True, can_restrict_members=True,
                                                    can_promote_members=True)
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))[
                                         't_promote_cap1'].format(target_user_username))
                        else:
                            pass
            else:
                pass
    else:
        pass


# demote a member to admin
@bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_demote'])
def demote_member_to_admin(message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    user_id = message.from_user.id
    can_promote_members = bot.get_chat_member(chat_id, user_id).can_promote_members
    for x in bot.get_chat_administrators(chat_id):
        rdb.hset(chat_id, x.user.id, x.status)
    if chat_type == 'supergroup' or chat_type == 'group':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if rdb.hget(chat_id, user_id) == 'creator':
                if rdb.hget(chat_id, target_user_id) == 'creator':
                    pass
                elif rdb.hget(chat_id, target_user_id) == 'administrator':
                    if target_user_id in bots_ids:
                        pass
                    else:
                        if chat_type == 'supergroup':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_pin_messages=False,
                                                    can_promote_members=False)
                            rdb.hdel(chat_id, target_user_id)
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_demote_cap1'].format(
                                target_user_username))
                        elif chat_type == 'group':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_promote_members=False)
                            rdb.hdel(chat_id, target_user_id)
                            bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_demote_cap1'].format(
                                target_user_username))
                        else:
                            pass
                elif target_user_id in bots_ids:
                    pass
                else:
                    pass
            elif rdb.hget(chat_id, user_id) == 'administrator':
                if can_promote_members:
                    if rdb.hget(chat_id, target_user_id) == 'creator':
                        pass
                    elif rdb.hget(chat_id, target_user_id) == 'administrator':
                        if target_user_id in bots_ids:
                            pass
                        else:
                            if chat_type == 'supergroup':
                                bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_pin_messages=False,
                                                        can_promote_members=True)
                                rdb.hdel(chat_id, user_id)
                                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_promote_cap1'].format(
                                    target_user_username))
                            elif chat_type == 'group':
                                bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_promote_members=False)
                                rdb.hdel(chat_id, user_id)
                                bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_promote_cap1'].format(
                                    target_user_username))
                            else:
                                pass
            else:
                pass
    else:
        pass


# user permissions
# can_send_messages by replay to user msg
# @bot.message_handler(func=lambda message: message.text in lang(rdb.hget(message.from_user.id, 'language_code'))['t_user_can_send_messages'])
# def user_can_send_messages(message):
#     chat_id = message.chat.id
#     chat_type = message.chat.type
#     user_id = message.from_user.id
#     if chat_type in ['group', 'supergroup']:
#         chat_admins = bot.get_chat_administrators(chat_id)
#         for x in chat_admins:
#             if x.status == 'creator':
#                 creators_ids.append(x.user.id)
#             elif x.status == 'administrator':
#                 admins_ids.append(x.user.id)
#         if message.reply_to_message:
#             target_user_id = message.reply_to_message.from_user.id
#             target_user_username = message.reply_to_message.from_user.username
#             en = lang(rdb.hget(user_id, 'language_code'))['t_enable']
#             if en == message.text[18:24]:
#                 until_date = message.text[26:]
#                 if 's' in until_date:
#                     until_date = until_date[:user_id]
#                 elif 'm' in until_date:
#                     until_date = until_date[:user_id]
#                     until_date = until_date * 60
#                 elif 'h' in until_date:
#                     until_date = until_date[:user_id]
#                     until_date = 60 * (until_date * 60)
#                 else:
#                     until_date = int(until_date)
#                 if rdb.hget(chat_id, user_id) == 'creator':
#                     if rdb.hget(chat_id, target_user_id) == 'creator':
#                         pass
#                     elif rdb.hget(chat_id, target_user_id) == 'administrator':
#                         if target_user_id in bots_ids:
#                             pass
#                         else:
#                             bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=True)
#                             rdb.hdel(chat_id, user_id)
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 target_user_username))
#                     elif target_user_id in bots_ids:
#                         pass
#                     else:
#                         bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=True)
#                         bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                             target_user_username))
#                 elif rdb.hget(chat_id, user_id) == 'administrator':
#                     can_restrict_members = bot.get_chat_member(chat_id, user_id).can_restrict_members
#                     if rdb.hget(chat_id, target_user_id) == 'creator':
#                         pass
#                     elif rdb.hget(chat_id, target_user_id) == 'administrator':
#                         if target_user_id in bots_ids:
#                             pass
#                         else:
#                             if can_restrict_members:
#                                 bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                                 bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                     target_user_username))
#                             else:
#                                 bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                     sudo_username, target_user_username))
#                     elif target_user_id in bots_ids:
#                         pass
#                     else:
#                         if can_restrict_members:
#                             bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 target_user_username))
#                         else:
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                 target_user_username))
#                 else:
#                     bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_piv_admin'])
#             di = lang(rdb.hget(user_id, 'language_code'))['t_disable']
#             if di in message.text[18:25]:
#                 until_date = message.text[26:]
#                 if 's' in until_date:
#                     until_date = until_date[:user_id]
#                 elif 'm' in until_date:
#                     until_date = until_date[:user_id]
#                     until_date = until_date * 60
#                 elif 'h' in until_date:
#                     until_date = until_date[:user_id]
#                     until_date = 60 * (until_date * 60)
#                 else:
#                     until_date = int(until_date)
#                 if rdb.hget(chat_id, user_id) == 'creator':
#                     if rdb.hget(chat_id, target_user_id) == 'creator':
#                         pass
#                     elif rdb.hget(chat_id, target_user_id) == 'administrator':
#                         if target_user_id in bots_ids:
#                             pass
#                         else:
#                             bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                             rdb.hdel(chat_id, user_id)
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 target_user_username))
#                     elif target_user_id in bots_ids:
#                         pass
#                     else:
#                         bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                         bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                             target_user_username))
#                 elif rdb.hget(chat_id, user_id) == 'administrator':
#                     can_restrict_members = bot.get_chat_member(chat_id, user_id).can_restrict_members
#                     if rdb.hget(chat_id, target_user_id) == 'creator':
#                         pass
#                     elif rdb.hget(chat_id, target_user_id) == 'administrator':
#                         if target_user_id in bots_ids:
#                             pass
#                         else:
#                             if can_restrict_members:
#                                 bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                                 bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                     target_user_username))
#                             else:
#                                 bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                     sudo_username, target_user_username))
#                     elif target_user_id in bots_ids:
#                         pass
#                     else:
#                         if can_restrict_members:
#                             bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages=False)
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap1'].format(
#                                 target_user_username))
#                         else:
#                             bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_user_can_send_messages_cap7'].format(
#                                 target_user_username))
#                 else:
#                     bot.reply_to(message, text=lang(rdb.hget(user_id, 'language_code'))['t_piv_admin'])
#         else:
#             pass
#     else:
#         pass
