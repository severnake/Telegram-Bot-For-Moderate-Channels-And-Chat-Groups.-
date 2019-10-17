from plugins.cfgbot import bot

''' groups management plugin 
        Methods:                 Status:            Usage:
            answerCallbackQuery      #not yet          #
            answerInlineQuery        #not yet          #

            exportChatInviteLink     #not yet          #

            deleteMessage            #not yet          #
            deleteChatPhoto          #not yet          #
            
            forwardMessage           #not yet          #
            
            getChat                  #not yet          #
            getChatAdministrators    #not yet          #
            getChatMembersCount      #not yet          #
            getChatMember            #not yet          #
            getFile                  #not yet          #
            getMe
            getUserProfilePhotos     #not yet
            getUpdates               #not yet          #

            kickChatMember           # Kick user       # kick @username

            leaveChat                #not yet          #

            pinChatMessage           #not yet          # pin 'msg'
            promoteChatMember        #not yet          #

            restrictChatMember       # Ban user        # ban @username

            sendAudio                #not yet          #
            sendChatAction           #not yet          #
            sendDocument             #not yet          #
            sendLocation             #not yet          #
            sendMessage              #not yet          #
            sendPhoto                #not yet          #
            sendPoll                 #not yet          #
            sendSticker              #not yet          #
            sendVideo                #not yet          #
            sendVideoNote            #not yet          #
            setChatDescription       #not yet          #
            setChatPhoto             #not yet          #
            setChatTitle             #not yet          #

            unbanChatMember          #not yet          #
            unpinChatMessage         #not yet          #

        '''
# help
help_msg_admin = 'working..'
help_msg_member = 'not yet'
# By message.text method.

@bot.message_handler(func= lambda message: message.text == 'help')
def reply_help_str(message):
    chat_type = message.chat.type
    chat_id = message.chat.id
    chat_admins = bot.get_chat_administrators(chat_id)
    chat_admins_ids = []

    user_id = message.from_user.id
    for x in chat_admins:
        chat_admins_ids.append(x.user.id)

    if chat_type == 'group' or chat_type == 'supergroup':
        if user_id in chat_admins_ids:
            bot.reply_to(message, text=help_msg_admin)
            print(user_id)
            print(chat_admins_ids)
        elif user_id not in chat_admins_ids:
            bot.reply_to(message, text=help_msg_member)
            print(chat_admins_ids)


# Ban user
# By message.text method.
@bot.message_handler(func=lambda message: message.text == 'ban')
def ban_user_str(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        pass
    else:
        return None


# Unban user
# By text method.
@bot.message_handler(func=lambda message: message.text == 'unban')
def unban_user_str(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        pass
    else:
        return None

# Kick user
# By text method.
@bot.message_handler(func=lambda message: message.text == 'kick')
def kick_user_str(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        pass
    else:
        return None


# Pin message
# By text method.
@bot.message_handler(func=lambda message: message.text == 'pin')
def pin_msg_str(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        pass
    else:
        return None


# Unpin message
# By text method.
@bot.message_handler(func=lambda message: message.text == 'unpin')
def unpin_msg_str(message):
    if message.chat.type == 'group' or message.chat.type == 'supergroup':
        pass
    else:
        return None
