from plugins.cfgbot import bot

''' groups management plugin '''

# Ban user
#By commands method.
@bot.message_handler(commands=['ban'])
def ban_user_cmd(message):
    pass

#By text method.
@bot.message_handler(func=lambda message: message.text == 'ban')
def ban_user_str(message):
    pass