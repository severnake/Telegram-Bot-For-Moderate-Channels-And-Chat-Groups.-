from ..config import bot, sudo_username, lang
from ..config import creators_ids, admins_ids, bots_ids
from ..utils.language import ch_lang
"""" Groups Management Handler """


# Ban user by replay to user msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_ban'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_ban'])
def ban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    can_restrict_members = bot.get_chat_member(chat_id, user_id).can_restrict_members
    vuntil_date = None
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap3'])
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap2'])
                    else:
                        print(target_user_id)
                        print(bots_ids)
                        bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                        admins_ids.pop(target_user_id)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_user_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap2'])
                else:
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_user_username))
            elif user_id in admins_ids:
                if target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap5'].format(sudo_username))
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap4'].format(sudo_username))
                    else:
                        if can_restrict_members:
                            bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_user_username))
                        else:
                            bot.reply_to(message,
                                         text=ch_lang(lang[-1])['t_ban_cap6'].format(sudo_username,
                                                                                     target_user_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap4'].format(target_user_username))
                else:
                    if can_restrict_members:
                        bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_user_username))
                    else:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap7'].format(target_user_username))
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap8'])
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
@bot.message_handler(commands=ch_lang(lang[-1])['t_unban'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_unban'])
def unban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    can_restrict_members = bot.get_chat_member(chat_id, user_id).can_restrict_members
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id not in creators_ids and target_user_id not in admins_ids and target_user_id not in \
                        bots_ids:
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_user_username))
            elif user_id in admins_ids:
                if target_user_id not in creators_ids and target_user_id not in admins_ids and target_user_id not in \
                        bots_ids:
                    if can_restrict_members:
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_user_username))
                    else:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap7'].format(target_user_username))
                else:
                    pass
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap8'])
        else:
            pass
    else:
        pass


# Kick user by replay to user msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_kick'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_kick'])
def kick_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    vuntil_date = 35
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap3'].format(target_username))
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'].format(target_username))
                    else:
                        bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'].format(target_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap2'].format(target_username))
                else:
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap1'].format(target_username))
            elif user_id in admins_ids:
                if target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap5'])
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap4'])
                    else:
                        bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                        bot.unban_chat_member(chat_id, target_user_id)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap1'].format(target_username))
                elif target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap4'])
                else:
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap1'].format(target_username))
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap8'])
        else:
            pass
    else:
        pass


# Kickme by send 'kickme' msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_kickme'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_kickme'])
def kickme_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    user_name = message.from_user.username
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if not message.reply_to_message:
        if chat_type == 'group' or chat_type == 'supergroup':
            if user_id in creators_ids or user_id in bots_ids:
                pass
            else:
                bot.kick_chat_member(chat_id, user_id)
                bot.unban_chat_member(chat_id, user_id)
                bot.reply_to(message, text=ch_lang(lang[-1])['t_kickme_cap1'].format(user_name))
    else:
        pass


# Pin msg by replay to msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_pin'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_pin'])
def pin_msg(message):
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(chat_id).permissions.can_pin_messages
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if message.reply_to_message:
        msg_id = message.reply_to_message.message_id
        if user_id in creators_ids:
            bot.pin_chat_message(chat_id, msg_id)
        elif user_id in admins_ids:
            if can_pin_messages:
                bot.pin_chat_message(chat_id, msg_id)
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_pin_cap1'].format(user_username))
        else:
            if can_pin_messages:
                bot.pin_chat_message(chat_id, msg_id)
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_pin_cap1'].format(user_username))


# Unpin by send msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_unpin'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_unpin'])
def unpin_msg(message):
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    user_username = message.from_user.username
    can_pin_messages = bot.get_chat(chat_id).permissions.can_pin_messages
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if user_id in creators_ids:
        bot.unpin_chat_message(chat_id)
    elif user_id in admins_ids:
        if can_pin_messages:
            bot.unpin_chat_message(chat_id)
        else:
            bot.reply_to(message, text=ch_lang(lang[-1])['t_unpin_cap1'].format(user_username))
    else:
        if can_pin_messages:
            bot.unpin_chat_message(chat_id)
        else:
            bot.reply_to(message, text=ch_lang(lang[-1])['t_unpin_cap1'].format(user_username))


# promote a member to admin
@bot.message_handler(commands=ch_lang(lang[-1])['t_promote'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_promote'])
def promote_member_to_admin(message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    can_promote_members = bot.get_chat_member(chat_id, user_id).can_promote_members
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'supergroup' or chat_type == 'group':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id in creators_ids:
                    pass
                elif target_user_id in admins_ids:
                    pass
                elif target_user_id in bots_ids:
                    pass
                else:
                    if chat_type == 'supergroup':
                        bot.promote_chat_member(chat_id, target_user_id, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True, can_pin_messages=True,
                                                can_promote_members=True)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(target_user_username))
                    elif chat_type == 'group':
                        bot.promote_chat_member(chat_id, target_user_id, can_change_info=True, can_delete_messages=True,
                                                can_invite_users=True, can_restrict_members=True,
                                                can_promote_members=True)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(target_user_username))
                    else:
                        pass
            elif user_id in admins_ids:
                if can_promote_members:
                    if target_user_id in creators_ids:
                        pass
                    elif target_user_id in admins_ids:
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
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(target_user_username))
                        elif chat_type == 'group':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=True,
                                                    can_delete_messages=True,
                                                    can_invite_users=True, can_restrict_members=True,
                                                    can_promote_members=True)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(target_user_username))
                        else:
                            pass
            else:
                pass
    else:
        pass


# demote a member to admin
@bot.message_handler(commands=ch_lang(lang[-1])['t_demote'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_demote'])
def demote_member_to_admin(message):
    chat_id = message.chat.id
    chat_type = message.chat.type
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    can_promote_members = bot.get_chat_member(chat_id, user_id).can_promote_members
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'supergroup' or chat_type == 'group':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id in creators_ids:
                    pass
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        pass
                    else:
                        if chat_type == 'supergroup':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_pin_messages=False,
                                                    can_promote_members=False)
                            admins_ids.pop(target_user_id)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_demote_cap1'].format(
                                target_user_username))
                        elif chat_type == 'group':
                            bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                    can_delete_messages=False,
                                                    can_invite_users=False, can_restrict_members=False,
                                                    can_promote_members=False)
                            admins_ids.pop(target_user_id)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_demote_cap1'].format(
                                target_user_username))
                        else:
                            pass
                elif target_user_id in bots_ids:
                    pass
                else:
                    pass
            elif user_id in admins_ids:
                if can_promote_members:
                    if target_user_id in creators_ids:
                        pass
                    elif target_user_id in admins_ids:
                        if target_user_id in bots_ids:
                            pass
                        else:
                            if chat_type == 'supergroup':
                                bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_pin_messages=False,
                                                        can_promote_members=True)
                                admins_ids.pop(target_user_id)
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(
                                    target_user_username))
                            elif chat_type == 'group':
                                bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                                                        can_delete_messages=False,
                                                        can_invite_users=False, can_restrict_members=False,
                                                        can_promote_members=False)
                                admins_ids.pop(target_user_id)
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_promote_cap1'].format(
                                    target_user_username))
                            else:
                                pass
            else:
                pass
    else:
        pass


# user can_send_messages by replay to user msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_can_send_messages'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_can_send_messages'])
def user_can_send_messages(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    can_restrict_members = bot.get_chat_member(chat_id, user_id).can_restrict_members
    print(message.text)
    if int in message.text:
        vuntil_date = message.text[-2:]
    else:
        vuntil_date = 0
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_user_username = message.reply_to_message.from_user.username
            en = ch_lang(lang[-1])['t_enable']
            if en == message.text[-18]:
                if user_id in creators_ids:
                    if target_user_id in creators_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap3'])
                    elif target_user_id in admins_ids:
                        if target_user_id in bots_ids:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap2'])
                        else:
                            bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=True)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                target_user_username))
                    elif target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap2'])
                    else:
                        bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=True)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                            target_user_username))
                elif user_id in admins_ids:
                    if target_user_id in creators_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap5'].format(sudo_username))
                    elif target_user_id in admins_ids:
                        if target_user_id in bots_ids:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap4'].format(
                                sudo_username))
                        else:
                            if can_restrict_members:
                                bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                    target_user_username))
                            else:
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap6'].format(
                                    sudo_username, target_user_username))
                    elif target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap4'].format(
                            target_user_username))
                    else:
                        if can_restrict_members:
                            bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                target_user_username))
                        else:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap7'].format(
                                target_user_username))
                else:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap8'])
            di = ch_lang(lang[-1])['t_disable']
            if di in message.text[:-2]:
                if user_id in creators_ids:
                    if target_user_id in creators_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap3'])
                    elif target_user_id in admins_ids:
                        if target_user_id in bots_ids:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap2'])
                        else:
                            bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                target_user_username))
                    elif target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap2'])
                    else:
                        bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                            target_user_username))
                elif user_id in admins_ids:
                    if target_user_id in creators_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap5'].format(sudo_username))
                    elif target_user_id in admins_ids:
                        if target_user_id in bots_ids:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap4'].format(
                                sudo_username))
                        else:
                            if can_restrict_members:
                                bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                    target_user_username))
                            else:
                                bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap6'].format(
                                    sudo_username, target_user_username))
                    elif target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap4'].format(
                            target_user_username))
                    else:
                        if can_restrict_members:
                            bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False)
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap1'].format(
                                target_user_username))
                        else:
                            bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap7'].format(
                                target_user_username))
                else:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_can_send_messages_cap8'])
        else:
            pass
    else:
        pass
