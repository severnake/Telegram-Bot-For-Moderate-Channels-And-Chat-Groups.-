from plugins.botcfg import bot, bot_id
from plugins.botcfg import creators_ids, admins_ids

''' Groups Management Plugin 
        Methods:                 Status:                                 Usage:
            ban                     #only normal user                      # replay to user msg 'ban' 
            unban                   # all user                             # replay to user msg 'uban'
            kick                    #only normal user                      # replay to user msg 'kick'
            kickme                  #only normal user                      # send 'kickme'
            pin                     # all user                             # replay to msg 'pin'
            unpin                   # all user                             # send 'unpin'
        '''

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
# By replay to user message str 'ban'.
@bot.message_handler(func=lambda message: message.text == 'ban')
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

    if chat_type == 'group' or chat_type == 'supergroup':
        # if creator send 'ban'.
        if user_id in creators_ids:
            if message.reply_to_message:
                user_target_id = message.reply_to_message.from_user.id
                user_target_name = message.reply_to_message.from_user.username                
                if user_target_id in creators_ids:
                    bot.reply_to(message, text='You Can Not Ban Yourself') 
                elif user_target_id in bot_id:
                    bot.reply_to(message, text='I Can Not Ban Myself!!!')
                elif user_target_id in admins_ids:
                    bot.reply_to(message, text='Un Support Feature!')
                    # bot.restrict_chat_member(chat_id, user_target_id, until_date=None, can_send_messages=False,
                    #                          can_send_media_messages=False, can_send_other_messages=False, can_add_web_page_previews=False)
                    # bot.kick_chat_member(chat_id, user_target_id)
                    # bot.reply_to(
                    #     message, text=f'Ban @{user_target_name} Done!')
                elif user_target_id not in creators_ids and user_target_id not in bot_id:
                    bot.restrict_chat_member(chat_id, user_target_id, until_date=None, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False, can_add_web_page_previews=False) 
                    bot.kick_chat_member(chat_id, user_target_id)
                    bot.reply_to(
                        message, text=f'Ban @{user_target_name} Done!')

        # if admin send 'ban'.
        elif user_id in admins_ids:
            if message.reply_to_message:
                user_target_id = message.reply_to_message.from_user.id
                if user_target_id in creators_ids:
                    bot.reply_to(
                        message, text=f'You Can not Ban the Creator @{user_target_name}.')
                elif user_target_id in bot_id:
                    bot.reply_to(message, text='Only Creator Can Ban Me')
                elif user_target_id in admins_ids:
                    bot.reply_to(
                        message, text=f'Only Creator {chat_creator_name}\nCan Ban The Admin {user_target_name}')
                elif user_target_id not in creators_ids and user_target_id not in bot_id or user_target_id not in admins_ids:
                    user_target_name = message.reply_to_message.from_user.username
                    bot.restrict_chat_member(chat_id, user_target_id, until_date=None, can_send_messages=False,
                                             can_send_media_messages=False, can_send_other_messages=False, can_add_web_page_previews=False)
                    bot.kick_chat_member(
                        chat_id, user_target_id)
                    bot.reply_to(
                        message, text='Ban @{} Done!'.format(user_target_name))
        
        # if member send 'ban'.
        elif user_id not in creators_ids or user_id not in admins_ids:
            bot.reply_to(message, text='you are not admin!!!')


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
                user_target_id = message.reply_to_message.from_user.id
                user_target_name = message.reply_to_message.from_user.username                
                if user_target_id in creators_ids or user_target_id in bot_id:
                    pass
                elif user_target_id in admins_ids:
                    bot.restrict_chat_member(chat_id, user_target_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
                    bot.unban_chat_member(chat_id, user_target_id)
                    bot.reply_to(
                        message, text=f'Unban @{user_target_name} Done!')
                elif user_target_id not in creators_ids and user_target_id not in bot_id:
                    bot.restrict_chat_member(chat_id, user_target_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews) 
                    bot.reply_to(
                        message, text=f'Unban @{user_target_name} Done!')

        # if admin send 'unban'.
        elif user_id in admins_ids:
            if message.reply_to_message:
                user_target_id = message.reply_to_message.from_user.id
                if user_target_id in creators_ids or user_target_id in bot_id:
                    pass
                elif user_target_id in admins_ids:
                    bot.reply_to(
                        message, text=f'Only Creator {chat_creator_name}\nCan Unban The Admin {user_target_name}')
                elif user_target_id not in creators_ids and user_target_id not in bot_id or user_target_id not in admins_ids:
                    user_target_name = message.reply_to_message.from_user.username
                    bot.restrict_chat_member(chat_id, user_target_id, until_date, can_send_messages,
                                             can_send_media_messages, can_send_other_messages, can_add_web_page_previews)
                    bot.unban_chat_member(chat_id, user_target_id)
                    bot.reply_to(
                        message, text='Unban @{} Done!'.format(user_target_name))
        
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
                user_target_id = message.reply_to_message.from_user.id
                user_target_name = message.reply_to_message.from_user.username
                if user_target_id in creators_ids:
                    bot.reply_to(message, text='You Can Not Kick Yourself!!!')
                elif user_target_id in bot_id:
                    bot.reply_to(message, text='I Can Not Kick Myself!!!')
                elif user_target_id in admins_ids:
                    bot.reply_to(message, text='Un Support Feature!')
                #     bot.restrict_chat_member(chat_id, user_target_id, until_date=None, can_send_messages=False,
                #                              can_send_media_messages=False, can_send_other_messages=False, can_add_web_page_previews=False)
                #     bot.kick_chat_member(chat_id, user_target_id)
                #     bot.reply_to(
                #         message, text=f'Kick @{user_target_name} Done!')
                elif user_target_id not in creators_ids and user_target_id not in bot_id: 
                    bot.kick_chat_member(chat_id, user_target_id)
                    bot.reply_to(
                        message, text=f'Kick @{user_target_name} Done!')

        # if admin send 'kick'.
        elif user_id in admins_ids:
            if message.reply_to_message:
                user_target_id = message.reply_to_message.from_user.id
                if user_target_id in creators_ids:
                    bot.reply_to(
                        message, text=f'You Can not Kick the Creator @{user_target_name}.')
                elif user_target_id in bot_id:
                    bot.reply_to(message, text='Only Creator Can Kick Me')
                elif user_target_id in admins_ids:
                    bot.reply_to(
                        message, text=f'Only Creator {chat_creator_name}\nCan Kick The Admin {user_target_name}')
                elif user_target_id not in creators_ids and user_target_id not in bot_id and user_target_id not in admins_ids:
                    user_target_name = message.reply_to_message.from_user.username
                    bot.kick_chat_member(
                        chat_id, user_target_id)
                    bot.reply_to(
                        message, text='Kick @{} Done!'.format(user_target_name))

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
        

# Upin msg
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