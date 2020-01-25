from ..config import bot, bot_id, sudo_username, channel_username
from ..config import creators_ids, admins_ids, bots_ids, vusers_ids, vusers_info
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


# Ban user
# By replay to user 'ban'.
# @bot.message_handler(func=lambda message: 'ban' in message.text)
@bot.message_handler(func=lambda message:message.text == 'ban')
def ban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    user_id = message.from_user.id

    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
            chat_creator_name = x.user.username
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)
    print(message)
    if chat_type == 'group' or chat_type == 'supergroup':
        if message.reply_to_message:
            target_user_id = message.reply_to_message.from_user.id
            target_username = message.reply_to_message.from_user.username
            if user_id in creators_ids:
                if target_user_id in bots_ids:
                    bot.reply_to(message, text='I can\'t ban myself!!!')
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text='You can\'t ban yourself')
                elif target_user_id in admins_ids:
                    bot.reply_to(message, text='Unsupported Feature!')
                    # bot.restrict_chat_member(chat_id, target_user_id, until_date=None, can_send_messages=False,
                    #                          can_send_media_messages=False, can_send_other_messages=False,
                    #                          can_add_web_page_previews=False)
                    # bot.kick_chat_member(chat_id, target_user_id)
                    # bot.reply_to(message, text=f'Ban @{target_username} Done!')
                else:
                    bot.restrict_chat_member(chat_id, target_user_id, until_date=None, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False,
                                             can_add_web_page_previews=False)
                    bot.kick_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=f'Ban @{target_username} Done!')
            elif user_id in admins_ids:
                if target_user_id in bots_ids:
                    bot.reply_to(message, text=f'Only the Creator @{sudo_username} can ban me!')
                elif target_user_id in creators_ids:
                    bot.reply_to(message, text=f'You can\'t ban the Creator @{target_username}.')
                elif target_user_id in admins_ids:
                    if target_user_id in bots_ids:
                        bot.reply_to(message, text=f'Only the Creator @{sudo_username} can ban me!')
                    else:
                        bot.reply_to(message, text=f'Only the Creator {sudo_username}\ncan ban the admin {target_username}')
                else:
                    bot.restrict_chat_member(chat_id, target_user_id, until_date=None, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False,
                                             can_add_web_page_previews=False)
                    bot.kick_chat_member(chat_id, target_user_id)
                    bot.reply_to(message, text=f'Ban @{target_username} Done!')
            else:
                pass
        # elif message.entities:
        #     if message.entities[0].type == 'mention':
        #         if '@' in message.text:
        #             target_username = message.text[3:]
        #             bot.get_chat_member()

        else:
            pass


# Unban user
# By replay to user message str 'unban'.
@bot.message_handler(func=lambda message: message.text == 'unban')
def unban_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)

    user_id = message.from_user.id
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
            chat_creator_name = x.user.username
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)

    if chat_type == 'group' or chat_type == 'supergroup':
        # if creator send 'unban'.
        if user_id in creators_ids:
            if message.reply_to_message:
                target_user_id = message.reply_to_message.from_user.id
                target_username = message.reply_to_message.from_user.username
                if target_user_id in creators_ids or target_user_id in bot_id:
                    pass
                elif target_user_id in admins_ids:
                    bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(
                        message, text=f'Unban @{target_username} Done!')
                elif target_user_id not in creators_ids and target_user_id not in bot_id:
                    bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
                    bot.reply_to(
                        message, text=f'Unban @{target_username} Done!')

        # if admin send 'unban'.
        elif user_id in admins_ids:
            if message.reply_to_message:
                target_user_id = message.reply_to_message.from_user.id
                if target_user_id in creators_ids or target_user_id in bot_id:
                    pass
                elif target_user_id in admins_ids:
                    bot.reply_to(
                        message, text=f'Only Creator {chat_creator_name}\nCan Unban The Admin {target_username}')
                elif target_user_id not in creators_ids and target_user_id not in bot_id or target_user_id not in admins_ids:
                    target_username = message.reply_to_message.from_user.username
                    bot.restrict_chat_member(chat_id, target_user_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
                    bot.unban_chat_member(chat_id, target_user_id)
                    bot.reply_to(
                        message, text='Unban @{} Done!'.format(target_username))

        # if member send 'ban'.
        elif user_id not in creators_ids or user_id not in admins_ids:
            bot.reply_to(message, text='you are not admin!!!')


# Kick user
# By replay to user message str 'kick'.
@bot.message_handler(func=lambda message: message.text == 'kick')
# @bot.message_handler(regexp='kick')
def kick_user(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)

    user_id = message.from_user.id
    for x in chat_admins:
        if x.status == 'creator':
            creators_ids.append(x.user.id)
            chat_creator_name = x.user.username
        elif x.status == 'administrator':
            admins_ids.append(x.user.id)

    if chat_type == 'group' or chat_type == 'supergroup':
        # if creator send 'kick'.
        if user_id in creators_ids:
            if message.reply_to_message:
                target_user_id = message.reply_to_message.from_user.id
                target_username = message.reply_to_message.from_user.username
                if target_user_id in creators_ids:
                    bot.reply_to(message, text='You Can Not Kick Yourself!!!')
                elif target_user_id in bot_id:
                    bot.reply_to(message, text='I Can Not Kick Myself!!!')
                elif target_user_id in admins_ids:
                    bot.reply_to(message, text='Un Support Feature!')
                #     bot.restrict_chat_member(chat_id, target_user_id, until_date=None, can_send_messages=False,
                #                              can_send_media_messages=False, can_send_other_messages=False,
                #                              can_add_web_page_previews=False)
                #     bot.kick_chat_member(chat_id, target_user_id)
                #     bot.reply_to(
                #         message, text=f'Kick @{target_username} Done!')
                elif target_user_id not in creators_ids and target_user_id not in bot_id:
                    bot.kick_chat_member(chat_id, target_user_id)
                    bot.reply_to(
                        message, text=f'Kick @{target_username} Done!')

        # if admin send 'kick'.
        elif user_id in admins_ids:
            if message.reply_to_message:
                target_user_id = message.reply_to_message.from_user.id
                if target_user_id in creators_ids:
                    bot.reply_to(
                        message, text=f'You Can not Kick the Creator @{target_username}.')
                elif target_user_id in bot_id:
                    bot.reply_to(message, text='Only Creator Can Kick Me')
                elif target_user_id in admins_ids:
                    bot.reply_to(
                        message, text=f'Only Creator {chat_creator_name}\nCan Kick The Admin {target_username}')
                elif target_user_id not in creators_ids and target_user_id not in bot_id and target_user_id not in admins_ids:
                    target_username = message.reply_to_message.from_user.username
                    bot.kick_chat_member(
                        chat_id, target_user_id)
                    bot.reply_to(
                        message, text='Kick @{} Done!'.format(target_username))

        # if member send 'ban'
        elif user_id not in creators_ids or user_id not in admins_ids:
            bot.reply_to(message, text='you are not admin!!!')


# Kickme
# By send 'kickme'.
@bot.message_handler(func=lambda message: message.text == 'kickme')
# @bot.message_handler(regexp='kick')
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

    if chat_type == 'group' or chat_type == 'supergroup':
        # if creator send 'kickme'.
        if user_id in creators_ids:
            bot.reply_to(message, text=f'I Can Not Kick You @{user_name}!!!')

        # if admin send 'kick'.
        elif user_id in admins_ids:
            bot.reply_to(message, text='Un Support Feature!')
        #     bot.promote_chat_member(chat_id, user_id, can_change_info=False, can_post_messages=False, can_edit_messages=False, can_delete_messages=False,
        #     can_invite_users=False, can_restrict_members=False, can_pin_messages=False, can_promote_members=False)
        #     bot.kick_chat_member(chat_id, user_id)
        #     bot.reply_to(message, text=f'kick @{user_name} Done!')

        # if member send 'ban'
        elif user_id not in creators_ids or user_id not in admins_ids:
            bot.restrict_chat_member(chat_id, user_id, until_date, can_send_messages, can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
            bot.kick_chat_member(chat_id, user_id)
            bot.reply_to(message, text=f'kick @{user_name} Done!')


# Pin msg
# By repaly to msg 'pin'
@bot.message_handler(func=lambda message: message.text == 'pin')
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
            bot.reply_to(message, text=f'You {user_username} are not allowed to pin messages!!!')
        

# UNPIN
# By send 'unpin'
@bot.message_handler(func=lambda message: message.text == 'unpin')
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
        bot.reply_to(message, text=f'You {user_username} are not allowed to unpin messages!!!')