from guardbot.config import bot


def start():
    from guardbot.handlers import channels
    from guardbot.handlers import groups
    from guardbot.handlers import private
    bot.polling(True)
