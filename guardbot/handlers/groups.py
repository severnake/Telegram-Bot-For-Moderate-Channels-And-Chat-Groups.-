from ..config import bot, bot_id, sudo_username, channel_username, lang
from ..config import creators_ids, admins_ids, bots_ids, vusers_ids, vusers_info
from ..utils.language import ch_lang
"""" Groups Management Handler """

until_date = None 
can_send_messages = True
can_send_media_messages = True
can_send_other_messages = True 

can_add_web_page_previews = True
can_change_info = False 
can_post_messages = False
can_edit_messages = False

can_delete_messages = False
can_invite_users = False
can_restrict_members = False
can_pin_messages = False

can_promote_members = False
disable_notification = False


# Ban user by replay to user msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_ban'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_ban'])
def ban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    vuntil_date = None
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
                if target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap2'])
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap3'])
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap2'])
                    else:
                        # bot.promote_chat_member(chat_id, target_user_id, can_change_info=False,
                        # can_post_messages=False,
                        #                         can_edit_messages=False, can_delete_messages=False,
                        #                         can_invite_users=False, can_restrict_members=False,
                        #                         can_pin_messages=False, can_promote_members=False,)
                        # bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False,
                        #                          can_send_media_messages=False, can_send_polls=False,
                        #                          can_send_other_messages=False, can_add_web_page_previews=False,
                        #                          can_change_info=False, can_invite_users=False,
                        #                          can_pin_messages=False)
                        # bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                        # admins_ids.pop(target_user_id)
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'])
                else:
                    bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False,
                                             can_send_media_messages=False, can_send_polls=False,
                                             can_send_other_messages=False, can_add_web_page_previews=False,
                                             can_change_info=False, can_invite_users=False, can_pin_messages=False)
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_username))
            elif user_id in admins_ids:
                if target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap4'].format(sudo_username))
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap5'].format(target_username))
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap4'].format(sudo_username))
                    else:
                        bot.reply_to(message,
                                     text=ch_lang(lang[-1])['t_ban_cap6'].format(sudo_username, target_username))
                else:
                    bot.restrict_chat_member(chat_id, target_user_id, vuntil_date, can_send_messages=False,
                                             can_send_media_messages=False, can_send_polls=False,
                                             can_send_other_messages=False, can_add_web_page_previews=False,
                                             can_change_info=False, can_invite_users=False, can_pin_messages=False)
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_ban_cap1'].format(target_username))
            else:
                pass
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
                if target_user_id in bots_ids:
                    # bot.unban_chat_member(chat_id, target_user_id)
                    # bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'])
                    pass
                elif target_user_id in creators_ids:
                    # bot.unban_chat_member(chat_id, target_user_id)
                    # bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'])
                    pass
                elif target_user_id in admins_ids:
                    # bot.unban_chat_member(chat_id, target_user_id)
                    # bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'])
                    pass
                else:
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_username))
            elif user_id in admins_ids:
                if target_user_id in bots_ids:
                    # bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_username))
                    pass
                elif target_user_id in creators_ids:
                    # bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_username))
                    pass
                elif target_user_id in admins_ids:
                    pass
                else:
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_unban_cap1'].format(target_username))
            else:
                # bot.reply_to(message, text='you are not admin!!!')
                pass
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
                if target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap2'].format(target_username))
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap3'].format(target_username))
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap2'].format(target_username))
                    else:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'].format(target_username))
                else:
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap1'].format(target_username))
            elif user_id in admins_ids:
                if target_user_id in bots_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap4'])
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap5'])
                    pass
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap5'])
                    else:
                        bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap7'])
                else:
                    bot.kick_chat_member(chat_id, target_user_id, vuntil_date)
                    bot.reply_to(message, text=ch_lang(lang[-1])['t_kick_cap1'].format(target_username))
            else:
                # bot.reply_to(message, text='you are not admin!!!')
                pass
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
    vuntil_date = 35
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if not message.reply_to_message:
        if chat_type == 'group' or chat_type == 'supergroup':
            if user_id in creators_ids:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'])
            elif user_id in admins_ids:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_sup_cap1'])
            else:
                bot.restrict_chat_member(chat_id, user_id, vuntil_date, can_send_messages=False,
                                         can_send_media_messages=False, can_send_polls=False,
                                         can_send_other_messages=False, can_add_web_page_previews=False,
                                         can_change_info=False, can_invite_users=False,
                                         can_pin_messages=False)
                bot.kick_chat_member(chat_id, user_id)
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
            bot.pin_chat_message(chat_id, msg_id)
        else:
            if can_pin_messages:
                bot.pin_chat_message(chat_id, msg_id)
            else:
                bot.reply_to(message, text=ch_lang(lang[-1])['t_pin'].format(user_username))
        

# Unpin by send msg
@bot.message_handler(commands=ch_lang(lang[-1])['t_unpin'])
@bot.message_handler(func=lambda message: message.text in ch_lang(lang[-1])['t_unpin'])
def unpin_msg(message):
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id
    user_username = message.from_user.username
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    if user_id in creators_ids:
        bot.unpin_chat_message(chat_id)
    elif user_id in admins_ids:
        bot.unpin_chat_message(chat_id)
    else:
        if can_pin_messages:
            bot.unban_chat_member(chat_id)
        else:
            bot.reply_to(message, text=ch_lang(lang[-1])['t_unpin'].format(sudo_username))
